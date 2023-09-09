from fastapi import FastAPI
from pydantic import BaseModel
import datetime


class Response(BaseModel):
    slack_name: str
    current_day: str
    utc_time: str
    track: str
    github_file_url: str
    github_repo_url: str
    status_code: int


app = FastAPI(
    title="Stage One Task: Create and Host an endpoint",
    version="1.0.0",
)
repo = "https://github.com/prmpsmart/hng_task_2"


@app.get("/api", status_code=200)
async def api(slack_name: str, track: str) -> Response:
    now = datetime.datetime.now()
    return {
        "slack_name": slack_name,
        "current_day": now.strftime("%A"),
        "utc_time": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "track": track,
        "github_file_url": f"{repo}/blob/main/main.py",
        "github_repo_url": f"{repo}",
        "status_code": 200,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        use_colors=True,
        host="127.0.0.1",
        port=8000,
        reload=0,
    )
