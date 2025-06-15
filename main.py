from fastapi import FastAPI

app = FastAPI()

# Endpoint or the routes
@app.get("/")
def home():
    return {"Data": "Test"}

