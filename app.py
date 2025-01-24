from fastapi import APIRouter, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from inference import model
import pandas as pd


node = APIRouter()

templates = Jinja2Templates(directory='templates')

@node.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


@node.post("/", response_class=HTMLResponse)
async def post_form(request: Request):
    form = await request.form()
    data = dict(form)
    new_data = {key: [float(value)] for key, value in data.items()}
    new_data = pd.DataFrame(data=new_data)
    new_data = new_data.to_numpy()
    prediction = model.predict(new_data)
    prediction = prediction[0]

    if prediction == 0:
        prediction = 'Normal'
    elif prediction == 1:
        prediction = 'Suspect'
    else:
        prediction = 'Pathological'


    return templates.TemplateResponse("output.html", {
        "request": request,
        "prediction": prediction
    })


