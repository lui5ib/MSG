import pandas as pd
import webbrowser as web
import pyautogui as pg
import time

def process_excel(file):
    # Procesa el archivo Excel y envía mensajes de WhatsApp aquí
    # Utiliza el código que proporcionaste

    url_excel= r"C:\Users\---5---\Desktop\Clientes.xlsx"
    #img=Image.open(r"C:\Users\---5---\Desktop\descargar.jpeg")
    data = pd.read_excel(url_excel, sheet_name='Ventas')
    data.head(3)

    for i in range(len(data)):
        celular = data.loc[i,'Celular'].astype(str) # Convertir a string para que se añada al mensaje
        nombre = data.loc[i,'Nombre']
        producto = data.loc[i,'Producto']
        
        # Crear mensaje personalizado
        mensaje = "Hola, " + nombre + "! Gracias por comprar " + producto + " con nosotros 🙌"
        
        # Abrir una nueva pestaña para entrar a WhatsApp Web
        # Opción 1: Si te abre WhastApp Web directamente en Google Chrome
        web.open("https://web.whatsapp.com/send?phone=" + celular)
        
        # Opción 2: Si te abre WhastApp Web en Microsoft Edge, especificar que lo abra en Chrome
        #chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        # web.get(chrome_path).open("https://web.whatsapp.com/send?phone=" + celular + "&text=" + mensaje)
        
        time.sleep(5)           # Esperar 5 segundos a que cargue
        #pg.click(1230,964)      # Hacer click en la caja de texto
        pg.typewrite(mensaje)
        time.sleep(2)           # Esperar 2 segundos 
        pg.press('enter')       # Enviar mensaje 
        time.sleep(3)           # Esperar 3 segundos a que se envíe el mensaje
        pg.hotkey('ctrl', 'w')  # Cerrar la pestaña
        time.sleep(2)

        #return f"Se enviaron {messages_sent} mensajes de WhatsApp."

if __name__ == "__main__":
    # Puedes realizar pruebas locales aquí si lo deseas
    pass
