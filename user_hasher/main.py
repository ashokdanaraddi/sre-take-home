import hashlib
import logging
import os
from typing import List
from fastapi import FastAPI, Header, Request, Response
from aioprometheus import REGISTRY, Counter, render

# Instantiate the app
app = FastAPI()

# Setup logging
logger = logging.getLogger("uvicorn.error")

# Load and log APP_VERSION
APP_VERSION = os.environ.get("APP_VERSION", "prod")
logger.info(f"APP_VERSION={APP_VERSION}")

USER_SALT = os.environ.get("USER_SALT")
logger.info(f"USER_SALT={USER_SALT}")

@app.get("/version")
async def version():
    return {"version": APP_VERSION}


@app.get("/user_hash")
async def user_hash(user_id: str):
    return hashlib.sha1(
        (user_id + os.environ.get("USER_SALT", {USER_SALT})).encode()
    ).hexdigest()


@app.get("/metrics")
async def handle_metrics(
    request: Request,  # pylint: disable=unused-argument
    accept: List[str] = Header(None),
) -> Response:
    content, http_headers = render(REGISTRY, accept)
    return Response(content=content, media_type=http_headers["Content-Type"])

