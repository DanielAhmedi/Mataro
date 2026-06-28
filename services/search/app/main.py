from fastapi import FastAPI

app=FastAPI(title="Search Service",
description="This is a search service for the application.",
version="1.0.0")
@app.get("/health")
def health_check():
    return {"status": "healthy"}