# main.py
import uvicorn
import multiprocessing
from server import*

if __name__ == "__main__":
    multiprocessing.freeze_support()
    config = uvicorn.Config(
        "server:app", host="127.0.0.1", port=5000, reload=True)
    server = uvicorn.Server(config=config)

    server.run()

    # uvicorn.run("server: app", host="127.0.0.1",
    #             port=5000, reload=True)
