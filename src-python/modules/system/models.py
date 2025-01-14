from typing import Optional

from pydantic import BaseModel, Field


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
