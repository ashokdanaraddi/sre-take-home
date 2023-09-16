import hashlib
import logging
import os
import asyncio
from aiohttp import web
from typing import List
from fastapi import FastAPI, Header, Request, Response
from aioprometheus import REGISTRY, Counter, render, Service, Timer, CONTENT_TYPE_LATEST
import socket

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


# Create a Prometheus Service
service = Service()

# Define Prometheus metrics with labels
request_duration = Gauge("request_duration_seconds", "Request duration in seconds",
                          ["application_version", "pod_ip", "node_ip"])
response_status_codes = Counter("response_status_codes_total", "Response status codes count",
                                 ["application_version", "pod_ip", "node_ip", "status_code"])
user_hashes_generated = Counter("user_hashes_generated_total", "Cumulative user hashes generated",
                                 ["application_version", "pod_ip", "node_ip"])

# Define an HTTP handler for the /metrics endpoint
async def metrics_handler(request):
    response = web.Response(text=render(service), content_type=CONTENT_TYPE_LATEST)
    return response

# Simulate collecting metrics
async def collect_metrics():
    while True:
        # Simulate collecting metrics
        # This section should be replaced with actual metric collection logic
        await asyncio.sleep(10)
        application_version = "1.0.0" # Get the application version
        pod_ip = "192.168.1.100" # Get the pod id
        node_ip = "10.0.0.1" # get the node IP
        request_duration.labels(application_version, pod_ip, node_ip).set(0.5)  # Example duration
        response_status_codes.labels(application_version, pod_ip, node_ip, "200").inc(10)  # Example count
        user_hashes_generated.labels(application_version, pod_ip, node_ip).inc(5)  # Example count


app.router.add_get('/metrics', metrics_handler)

"""
@app.get("/metrics")
async def handle_metrics(
    request: Request,  # pylint: disable=unused-argument
    accept: List[str] = Header(None),
) -> Response:
    content, http_headers = render(REGISTRY, accept)
    return Response(content=content, media_type=http_headers["Content-Type"])
"""
