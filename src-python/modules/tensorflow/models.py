from typing import List

from pydantic import BaseModel, Field


class GPUInfo(BaseModel):
    version: str = Field(..., description="TensorFlow version")
    gpu_available: bool = Field(..., description="Whether GPU is available")
    gpu_devices: List[str] = Field(description="List of available GPU devices")
    cpu_devices: List[str] = Field(description="List of available CPU devices")
    built_with_cuda: bool = Field(..., description="Whether TensorFlow was built with CUDA")
    eager_execution: bool = Field(..., description="Whether eager execution is enabled")
