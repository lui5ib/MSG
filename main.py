from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.excel_processing import process_excel  # Importa la función
import pandas as pd
import io
from pydantic import BaseModel  # Importa BaseModel de Pydantic
#import tempfile


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Define un modelo Pydantic para el formulario
class FormInput(BaseModel):
    message: str  # Define un campo 'message' de tipo str

# ...

@app.post("/process/")
async def process_file(file: UploadFile, message: str = Form (...)):
    # Ahora 'form' contendrá los datos del formulario deserializados

    # Crear una copia temporal del archivo que sea seekable
    file_data = io.BytesIO(file.file.read())

    # Leer el archivo Excel desde el DataFrame obtenido
    excel_data = pd.read_excel(file_data, sheet_name='Ventas')

    # Llamar a la función process_excel para procesar los datos y enviar el mensaje personalizado
    process_excel(excel_data, message)

    # Puedes devolver una respuesta con los datos procesados
    return {"message": "Archivo Excel procesado correctamente"}


if __name__ == "__main__":
    pass
