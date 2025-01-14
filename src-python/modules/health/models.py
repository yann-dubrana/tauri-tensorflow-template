from pydantic import BaseModel, Field


class HealthCheck(BaseModel):
    color: str  = Field(..., description="Color of status of the API")
    status: str = Field(..., description="Health status of the API")
