from fastapi import APIRouter
from modules.health.models import HealthCheck

router = APIRouter(
    prefix="/health",  # All routes will be prefixed with /items
    tags=["health"],  # For API documentation grouping
    responses={404: {"description": "Not found"}},  # Default responses
)


@router.get("", operation_id="GetServerHealth", response_model=HealthCheck)
async def health_check():
    return HealthCheck(status="healthy", color="green")
