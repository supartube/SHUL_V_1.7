from pydantic import BaseModel, Field
from typing import Optional, Any

class TaskRequest(BaseModel):
    command: str = Field(min_length=3, max_length=5000)
    mode: str = Field(default="standard", pattern="^(standard|research|software|security_lab)$")

class TaskResponse(BaseModel):
    task_id: int
    status: str
    message: str

class SecurityScanRequest(BaseModel):
    target: str = Field(min_length=1, max_length=253)
    authorization_confirmed: bool = False
