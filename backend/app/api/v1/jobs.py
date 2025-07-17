from typing import List

from fastapi import APIRouter, Depends

from app.dependencies import get_authenticated_user
from app.models import User
from app.models.document import Category, Job
from app.schemas.job import CategoryResponse, JobResponse

router = APIRouter(prefix="/jobs", tags=["jobs"])

@router.get("/categories", response_model=List[CategoryResponse])
async def get_all_categories(user: User = Depends(get_authenticated_user)):
    data = await Category.find_all().to_list()
    return data

@router.get("/", response_model=List[JobResponse])
async def jobs_test():
    data = await Job.find_all().to_list()
    return data