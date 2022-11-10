from fastapi import FastAPI

"""
pyinstaller .\service.py --onefile -y -n servicetest --uac-admin
"""

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "PAPAI"}
