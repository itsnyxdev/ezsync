db = db.getSiblingDB('ezsync');
db.createUser({
   user: process.env.MONGO_USER,
   pwd: process.env.MONGO_PASSWORD,
   roles: [
       {
           role: "dbOwner",
           db: "ezsync"
       }
   ]
});
const now = Date.now();

db.categories.insertMany([
  { name: "Software Development", createdAt: now },
  { name: "Web Development", createdAt: now },
  { name: "Mobile Development", createdAt: now },
  { name: "UX/UI Design", createdAt: now },
  { name: "Data Science & Analytics", createdAt: now },
  { name: "Artificial Intelligence & Machine Learning", createdAt: now },
  { name: "Cybersecurity", createdAt: now },
  { name: "Cloud Computing & DevOps", createdAt: now },
  { name: "Network & Systems Administration", createdAt: now },
  { name: "IT Support & Helpdesk", createdAt: now },
  { name: "Quality Assurance & Testing", createdAt: now },
  { name: "Database Administration & Data Engineering", createdAt: now },
  { name: "Product Management", createdAt: now },
  { name: "Project Management", createdAt: now },
  { name: "Hardware Engineering & Embedded Systems", createdAt: now },
  { name: "Game Development & AR/VR", createdAt: now }
]);

db.categories.createIndex(
    {
        name: 1
    },
    {
        unique: true,
        name: "nameIdx"
    }
);

db.createCollection("jobs", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["slug", "title", "location", "company", "levelType", "jobId", "categoryId", "modifiedAt"],
            properties: {
                slug: {
                    bsonType: "string",
                    maxLength: 120
                },
                title: {
                    bsonType: "string",
                    maxLength: 256
                },
                description: {
                    bsonType: "string"
                },
                location: {
                    bsonType: "object",
                    required: ["city", "country"],
                    properties: {
                        city: {
                            bsonType: "string",
                            maxLength: 128
                        },
                        country: {
                            bsonType: "string",
                            maxLength: 128
                        }
                    }
                },
                company: {
                    bsonType: "string"
                },
                jobId: {
                    bsonType: "objectId"
                },
                categoryId: {
                    bsonType: "objectId"
                },
                modifiedAt: {
                    bsonType: "date"
                },
                levelType: {
                    bsonType: "array",
                    items: {
                        bsonType: "string",
                        enum: ["entry", "mid", "senior"]
                    },
                    minItems: 1
                }
            }
        }
    }
});


db.jobs.createIndex(
    {
            slug: 1
    },
    {
        name: "jobsSlugIdx"
    }
)


db.jobs.createIndex(
    {
            categoryId: 1
    },
    {
        name: "jobsCategoryIdx"
    }
)

db.jobs.createIndex(
    {
            modifiedAt: -1
    },
    {
        name: "jobsModifictionIdx"
    }
);


