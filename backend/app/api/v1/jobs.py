from typing import List, Annotated

from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.params import Query

from app.dependencies import get_authenticated_user
from app.models import User
from app.models.document import Category, Job
from app.schemas.job import CategoryResponse, JobResponse, JobsResponse, JobsFilterRequest

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("/categories", response_model=List[CategoryResponse])
async def get_all_categories(user: User = Depends(get_authenticated_user)):
    categories = await Category.find_all().to_list()
    return categories


@router.get("/", response_model=JobsResponse)
async def get_jobs(filters: Annotated[JobsFilterRequest, Query()], user: User = Depends(get_authenticated_user)):
    try:
        query_filters = {}

        page = filters.page
        limit = filters.limit
        category_id = filters.category_id
        level = filters.level
        location = filters.location
        search = filters.search

        if category_id:
            query_filters["category_id"] = category_id

        if level:
            query_filters["levels"] = {"$in": [level]}

        if location:
            query_filters["location"] = {"$regex": location, "$options": "i"}

        if search:
            query_filters["$or"] = [
                {"title": {"$regex": search, "$options": "i"}},
            ]

        skip = (page - 1) * limit
        total_items = await Job.find(query_filters).count()
        jobs = await Job.find(query_filters).skip(skip).limit(limit).to_list()
        total_pages = (total_items + limit - 1) // limit

        job_responses = [
            JobResponse(
                slug=job.slug,
                link=job.link,
                title=job.title,
                location=job.location,
                company=job.company,
                levels=job.levels,
                modified_at=job.modified_at,
                category_id=job.category_id,
                job_id=job.job_id
            )
            for job in jobs
        ]

        return JobsResponse(
            data=job_responses,
            meta={
                "currentPage": page,
                "totalPages": total_pages,
                "totalItems": total_items,
                "itemsPerPage": limit,
                "hasNextPage": page < total_pages,
                "hasPrevPage": page > 1,
            },
        )

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch jobs",
        )


@router.get("/{job_id}", response_model=JobResponse)
async def get_job_by_id(job_id: PydanticObjectId, user: User = Depends(get_authenticated_user)):
    try:
        job = await Job.get(job_id)

        if not job:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Job not found"
            )

        return job

    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch job",
        )