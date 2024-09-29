from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class StudentData(BaseModel):
    Gender: int
    Extracurricular_Activities: int
    Learning_Disabilities: int
    Hours_Studied: int
    Physical_Activity: int
    Sleep_Hours: int
    Attendance: int
    Previous_Scores: int
    Tutoring_Sessions: int
    Motivation_Level: int
    Internet_Access: int
    School_Type: int
    Parental_Involvement: int
    Access_to_Resources: int
    Family_Income: int
    Teacher_Quality: int
    Peer_Influence: int
    Parental_Education_Level: int
    Distance_from_Home: int

@app.post("/")
async def model_predict(data: StudentData) -> Dict[str, int]:
    result = {key: value * 2 for key, value in data.model_dump().items()}
    return result