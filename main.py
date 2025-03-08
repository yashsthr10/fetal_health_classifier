from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pandas as pd
import pickle
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates directory
templates = Jinja2Templates(directory="templates")

# Loading the trained model
try:
    with open('model/model.pkl', 'rb') as f:
        model = pickle.load(f,encoding='bytes')
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def post_form(request: Request):
    try:
        form = await request.form()
        data = dict(form)
        new_data = {key: [float(value)] for key, value in data.items()}
        new_data_df = pd.DataFrame(data=new_data)
        new_data_array = new_data_df.to_numpy()
        
        if model is not None:
            prediction = model.predict(new_data_array)
            prediction = prediction[0]
            
            if prediction == 0:
                prediction = 'Normal'
            elif prediction == 1:
                prediction = 'Suspect'
            else:
                prediction = 'Pathological'
        else:
            prediction = "Error: Model not loaded"
            
        return templates.TemplateResponse("output.html", {
            "request": request,
            "prediction": prediction
        })
        
    except Exception as e:
        print(f"Error during prediction: {str(e)}")
        return templates.TemplateResponse("output.html", {
            "request": request,
            "prediction": f"Error: {str(e)}"
        })
    