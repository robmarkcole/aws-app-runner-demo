from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.config import Config

# from starlette_exporter import PrometheusMiddleware, handle_metrics

import logging, sys
import uvicorn
from os import getenv

logging.basicConfig(
    stream=sys.stdout, level=eval("logging." + getenv("LOG_LEVEL", "INFO"))
)
logging.debug("Log level is set to DEBUG.")


async def homepage(request):
    return JSONResponse({"hello": "world"})


app = Starlette(
    debug=True,
    routes=[
        Route("/", homepage),
    ],
)

# app.add_middleware(PrometheusMiddleware)
# app.add_route("/metrics", handle_metrics)

config = Config()

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=int(getenv("PORT", 8000)),
        log_level=getenv("LOG_LEVEL", "info"),
        debug=getenv("DEBUG", False),
        proxy_headers=True,
    )
