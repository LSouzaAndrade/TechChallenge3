from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
import pandas as pd
import joblib
import os

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, 'Models', 'model_svr.pkl')
scaler_path = os.path.join(current_dir, 'Models', 'scaler.pkl')
loaded_model = joblib.load(model_path)
loaded_scaler = joblib.load(scaler_path)
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
    df = pd.DataFrame([data.model_dump()])
    df = df[['Hours_Studied', 'Attendance', 'Parental_Involvement',
       'Access_to_Resources', 'Extracurricular_Activities', 'Sleep_Hours',
       'Previous_Scores', 'Motivation_Level', 'Internet_Access',
       'Tutoring_Sessions', 'Family_Income', 'Teacher_Quality', 'School_Type',
       'Peer_Influence', 'Physical_Activity', 'Learning_Disabilities',
       'Parental_Education_Level', 'Distance_from_Home', 'Gender']]
    df_scaled = loaded_scaler.transform(df.values)
    result = loaded_model.predict(df_scaled)
    return {"prediction": round(result[0], 0)}