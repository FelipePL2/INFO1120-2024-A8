#prueba
from docx import Document
import os

power = Document()

power.add_heading("Titulo", 0)

filename = "word.docx"
power.save(filename)

if os.name == 'nt':
    os.startfile(filename)
elif os.name == 'posix':
    os.system(f'open {filename}')
else:
    print(f"No se puede abrir automáticamente el archivo en este sistema operativo: {os.name}")
