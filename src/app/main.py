from fastapi import FastAPI
import joblib
import pandas as pd
import uvicorn
from pydantic import BaseModel
from config.config import config


class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


app = FastAPI()
model = joblib.load(config["train"]["model_path"])


@app.post("/predict")
def predict(data: IrisInput):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)
    return {"prediction": int(prediction[0])}


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=config["deployment"]["app_host"],
        port=config["deployment"]["app_port"],
    )
