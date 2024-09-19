from fastapi import FastAPI, Request  
from fastapi.middleware.cors import CORSMiddleware
from newapp import predictDisease 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],   
)

@app.post("/api")
async def get_disease_prediction(request: Request):
    body = await request.json()
    # print(body,"body of new.py")
    symptoms = body.get('symptoms', '')
    if isinstance(symptoms, list):
        symptoms = ', '.join(symptoms)  # Join list elements into a single string

    print(symptoms, "sts")
    if not symptoms:
        return {"error": "No symptoms provided"}
    
    # Get prediction from predictDisease function
    result = predictDisease(symptoms)
    return {"result"}