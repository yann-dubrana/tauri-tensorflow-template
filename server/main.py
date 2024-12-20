import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import tensorflow as tf
import platform
import psutil
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import cpuinfo


# Pydantic Models
class GPUInfo(BaseModel):
    version: str = Field(..., description="TensorFlow version")
    gpu_available: bool = Field(..., description="Whether GPU is available")
    gpu_devices: List[str] = Field(default_factory=list, description="List of available GPU devices")
    cpu_devices: List[str] = Field(default_factory=list, description="List of available CPU devices")
    built_with_cuda: bool = Field(..., description="Whether TensorFlow was built with CUDA")
    eager_execution: bool = Field(..., description="Whether eager execution is enabled")


class OSInfo(BaseModel):
    system: str = Field(..., description="Operating system name")
    release: str = Field(..., description="OS release version")
    version: str = Field(..., description="OS version")
    machine: str = Field(..., description="Machine architecture")


class CPUCores(BaseModel):
    physical: int = Field(..., description="Number of physical CPU cores")
    logical: int = Field(..., description="Number of logical CPU cores")


class CPUFrequency(BaseModel):
    current: Optional[float] = Field(None, description="Current CPU frequency in MHz")
    min: Optional[float] = Field(None, description="Minimum CPU frequency in MHz")
    max: Optional[float] = Field(None, description="Maximum CPU frequency in MHz")


class CPUInfo(BaseModel):
    brand: str = Field(..., description="CPU brand name")
    cores: CPUCores
    frequency: CPUFrequency


class MemoryInfo(BaseModel):
    total: int = Field(..., description="Total memory in bytes")
    available: int = Field(..., description="Available memory in bytes")
    used: int = Field(..., description="Used memory in bytes")
    percentage: float = Field(..., description="Memory usage percentage")


class SystemInfo(BaseModel):
    os: OSInfo
    cpu: CPUInfo
    memory: MemoryInfo
    python_version: str = Field(..., description="Python version")


class HealthCheck(BaseModel):
    status: str = Field(..., description="Health status of the API")

# FastAPI Application
app = FastAPI(
    title="TensorFlow System Info API",
    description="API to get system and TensorFlow information",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/tensorflow/info", operation_id='GetTensorflowInfo', response_model=GPUInfo)
async def get_tensorflow_info():
    try:
        return GPUInfo(
            version=tf.__version__,
            gpu_available=len(tf.config.list_physical_devices('GPU')) > 0,
            gpu_devices=[device.name for device in tf.config.list_physical_devices('GPU')],
            cpu_devices=[device.name for device in tf.config.list_physical_devices('CPU')],
            built_with_cuda=tf.test.is_built_with_cuda(),
            eager_execution=tf.executing_eagerly()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/system/info", operation_id='GetSystemInfo', response_model=SystemInfo)
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


@app.get("/health", operation_id="GetServerHealth", response_model=HealthCheck)
async def health_check():
    return HealthCheck(status="healthy")


def run_server():
    """Function to run the tensorflow-server-x86_64-pc-windows-msvc, called by the executable"""
    config = uvicorn.Config(
        app=app,
        host="127.0.0.1",
        port=63421,
        log_level="info",
        loop="asyncio"
    )
    server = uvicorn.Server(config)
    server.run()


if __name__ == "__main__":
    run_server()
