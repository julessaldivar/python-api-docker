from fastapi import FastAPI, Response, status, Query
from pydantic import BaseModel
import random


app = FastAPI()

# frog facts list
frog_facts = [
    {"id": 0, "fact": "Frogs absorb water through their skin, so they don't need to drink."},
    {"id": 1, "fact": "A group of frogs is called an army."},
    {"id": 2, "fact": "Frogs can lay as many as  4,000 eggs in frogspawn."},
    {"id": 3, "fact": "Frogs radiate non-binary energy."},
    {"id": 4, "fact": "There are over 6,000 species frogs."},
    {"id": 5, "fact": "Frogs can jump over 20 times their own body length."}



]


class Fact(BaseModel):
    id: int
    fact: str


@app.get("/fact")
async def get_random_fact():
    random_fact = random.choice(frog_facts)
    return random_fact


@app.get("/fact/")
async def get_fact_by_query(id: int = Query(..., description="Index of the frog fact" )):
    if id < 0 or id >= len(frog_facts):
        Response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": "Fact not found"}
    return frog_facts[id]


@app.get("/fact/{id}")
async def get_fact_by_path(id: int):
    if id < 0 or id >= len(frog_facts):
        Response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": "Fact not found"}
    return frog_facts[id]


@app.post("/fact")
async def add_fact(new_fact: Fact):
    new_id = len(frog_facts)
    fact = {"id": new_id, "fact": new_fact.fact}
    frog_facts.append(fact)
    return fact