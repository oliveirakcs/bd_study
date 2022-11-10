import uvicorn

if __name__ == "__main__":

    config = uvicorn.Config(
        "mainobs:app", host="127.0.0.1", port=5005, reload=True)
    server = uvicorn.Server(config=config)
    server.run()

    # uvicorn.run("main:app", reload=True, host="127.0.0.1",
    #             port=5000, log_level="info")
