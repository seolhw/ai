from fastapi import FastAPI, Request

app = FastAPI()

mount_chainlit(app=app, target="_app.py", path="/")

# @app.get("/")
# async def catch_all_get(request: Request, full_path: str = None):
#     return {
#         "message": "GET request caught by通配符路由",
#         "requested_path": full_path,
#         "full_url": str(request.url),
#         "method": request.method,
#         "headers": dict(request.headers),
#         "query_params": dict(request.query_params)
#     }
