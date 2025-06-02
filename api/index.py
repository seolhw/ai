import os
from chainlit.utils import mount_chainlit
from fastapi import FastAPI

app = FastAPI()

# 获取当前脚本所在的目录
base_dir = os.path.dirname(os.path.abspath(__file__))

# 构建 _app.py 的路径
app_file_path = os.path.join(base_dir, "_app.py")


mount_chainlit(app=app, target=app_file_path, path="/")
