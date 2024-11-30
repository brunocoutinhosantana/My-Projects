import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title='Selecione uma pasta que você queira organizar os arquivos')

lista_arquivos = os.listdir(caminho)

locais = {
    'Imagens': ['.png', '.jpg'],
    'Planilhas': ['.xlsx'],
    'PDFs': ['.pdf'],
    'Csv': ['.csb'],
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f'{caminho}/{arquivo}')
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f'{caminho}/{pasta}'):
                os.makedirs(f'{caminho}/{pasta}')
            os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}')
