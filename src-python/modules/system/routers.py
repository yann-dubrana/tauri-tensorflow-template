import platform
import psutil
from cpuinfo import cpuinfo
from fastapi import HTTPException, APIRouter

from modules.system.models import SystemInfo, OSInfo, CPUInfo, CPUCores, CPUFrequency, MemoryInfo

router = APIRouter(
    prefix="/system",  # All routes will be prefixed with /items
    tags=["system"],  # For API documentation grouping
    responses={404: {"description": "Not found"}},  # Default responses
)


@router.get("/info", operation_id='GetSystemInfo', response_model=SystemInfo)
async def get_system_info():
    try:
        cpu_info = cpuinfo.get_cpu_info()
        memory = psutil.virtual_memory()
        cpu_freq = psutil.cpu_freq()

        return SystemInfo(
            os=OSInfo(
                system=platform.system(),
                release=platform.release(),
                version=platform.version(),
                machine=platform.machine()
            ),
            cpu=CPUInfo(
                brand=cpu_info.get('brand_raw', 'Unknown'),
                cores=CPUCores(
                    physical=psutil.cpu_count(logical=False),
                    logical=psutil.cpu_count(logical=True)
                ),
                frequency=CPUFrequency(
                    current=cpu_freq.current if cpu_freq else None,
                    min=cpu_freq.min if cpu_freq else None,
                    max=cpu_freq.max if cpu_freq else None
                )
            ),
            memory=MemoryInfo(
                total=memory.total,
                available=memory.available,
                used=memory.used,
                percentage=memory.percent
            ),
            python_version=platform.python_version()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
