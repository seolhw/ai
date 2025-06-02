from fastapi import FastAPI

app = FastAPI({
    prefix: '/api'
})


@app.get("/")
@app.get('/hello1')
def read_root():
    return {"Hello": "World1"}


@app.get('hello2')
def read_root2():
    return {"Hello": "World2"}
