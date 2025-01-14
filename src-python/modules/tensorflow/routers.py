from fastapi import APIRouter, HTTPException
import tensorflow as tf

from modules.tensorflow.models import GPUInfo

router = APIRouter(
    prefix="/tensorflow",  # All routes will be prefixed with /items
    tags=["tensorflow"],  # For API documentation grouping
    responses={404: {"description": "Not found"}},  # Default responses
)

@router.get("/info", operation_id='GetTensorflowInfo', response_model=GPUInfo)
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