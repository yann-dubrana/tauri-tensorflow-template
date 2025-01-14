import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules.health.routers import router as health_router
from modules.system.routers import router as system_router
from modules.tensorflow.routers import router as tensorflow_router

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

app.include_router(health_router)
app.include_router(system_router)
app.include_router(tensorflow_router)


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
