from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Sample(BaseModel):
    id :int
    name: str
    email : str
    
marks:List[Sample] = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/marks")
def read_marks():
    return marks

@app.post("/marks")
def add_marks(sample:Sample):
    marks.append(sample)
    return {"message": "Sample added successfully"}

@app.put("/marks/{sample_id}")
def update_marks(sample_id: int,updated_sample:Sample):
    for index,sample in enumerate(marks):
        if sample.id == sample_id:
            marks[index] = updated_sample
            return {"message": "Sample updated successfully"}
    return {"message": "Sample not found"}

@app.delete("/marks/{sample_id}")
def delete_marks(sample_id:int):
    for index,sample in enumerate(marks):
        if sample.id == sample_id:
            marks.pop(index)
            return {sample_id: "Sample deleted successfully"}
        return {"error": "Sample not found"}