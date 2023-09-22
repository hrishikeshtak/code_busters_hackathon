import traceback

import uvicorn

from src.common.helper import Helper


def start_api_service():
    Helper.print_message("Starting API Server")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        access_log=False,
        workers=1,
        timeout_keep_alive=60,
        reload=True,
    )


if __name__ == "__main__":
    try:
        start_api_service()
    except Exception:
        Helper.print_message(
            "Exception in main method: {}".format(traceback.format_exc()),
            level="error",
        )
