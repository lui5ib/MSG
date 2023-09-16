from fastapi import FastAPI, Request, File, UploadFile
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.excel_processing import process_excel  # Importa la función
import pandas as pd
import io

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process/")
async def process_file(file: UploadFile):
    # Crear una copia temporal del archivo que sea seekable
    file_data = io.BytesIO(file.file.read())

    # Leer el archivo Excel desde la copia temporal
    excel_data = pd.read_excel(file_data, sheet_name='Ventas')

    # Llamar a la función process_excel para procesar los datos
    process_excel(excel_data)

    # Puedes devolver una respuesta con los datos procesados
    return {"message": "Archivo Excel procesado correctamente"}

if __name__ == "__main__":
    pass
