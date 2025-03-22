from fastapi import FastAPI
from config.database import Base, engine
from routes import router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Claim-based AI App"}
