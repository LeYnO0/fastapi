from pydantic import BaseModel, UUID4, Field
from typing import List


class Params(BaseModel):
    param_1: str
    param_2: int


class TaskAdd(BaseModel):
    uuid: UUID4
    task: str
    params: List[Params]


class TaskUpdate(BaseModel):
    uuid: UUID4
    new_task: str
    new_params: List[Params]
