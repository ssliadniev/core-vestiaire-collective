import logging

import uvicorn
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

import config as conf
from solution.channel.fastapi.controller import router

logging.basicConfig(level=logging.DEBUG)

app = FastAPI()
app.include_router(router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    logging.info("Starting vestiaire collective service...")
    uvicorn.run(
        app="solution.channel.fastapi.main:app",
        host=conf.HOST,
        port=conf.PORT,
        log_level=conf.LOGGER_LEVEL,
        reload=conf.DEBUG,
    )
    logging.info("Vestiaire collective service started")
