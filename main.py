from fastapi import FastAPI
import uvicorn

import  connection

app = FastAPI()

@app.get("/")
def server_start():
    return "API Started!"


@app.get("/test-connection")
def test_connection():
    try:
        return connection.test()
    except Exception as message:
        return message

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, host='0.0.0.0', reload=True, access_log=False)