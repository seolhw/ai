from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def catch_all_get(request: Request, full_path: str = None):
    return {
        "message": "GET request caught by通配符路由",
        "requested_path": full_path,
        "full_url": str(request.url),
        "method": request.method,
        "headers": dict(request.headers),
        "query_params": dict(request.query_params)
    }

# @app.get("/")
# @app.get('/hello1')
# def read_root():
#     return {"Hello": "World1"}


# @app.get('/hello2')
# def read_root2():
#     return {"Hello": "World2"}
