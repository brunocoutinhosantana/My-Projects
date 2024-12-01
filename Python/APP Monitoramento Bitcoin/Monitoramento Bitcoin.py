from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import request
import json

# cores ---------------
co0 = "#444466"  # Preta / black
co1 = "#feffff"  # branca / white 
co2 = "#6f9fbd"  # azul / blue
fundo = "#484f60"  # background

# criando janela
janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)

# dividindo as janelas em 2 frames
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_cima = Frame(janela, width=320, height=50, bg=co1, pady=0, padx=0, relief='flat')
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=320, height=330, bg=fundo, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=2, column=0, sticky=NW)

# funcao para pegar dados


def info():
    api_link = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CAOA%2CBRL"

    # HTTP request
    response = request.get(api_link)

    # convertendo os daos em dicionario
    dados = response.json()

    # valor em USD
    valor_usd = float(dados['USD'])
    valor_formatado_usd = "${:,.3f}".format(valor_usd)
    l_preco_usd['text'] = valor_formatado_usd

    # valor em EURO
    valor_euro = float(dados['EUR'])
    valor_formatado_euro = "€{:,.3f}".format(valor_euro)
    l_preco_euro['text'] = valor_formatado_euro

    # valor em REAIS
    valor_real = float(dados['BRL'])
    valor_formatado_real = "R${:,.3f}".format(valor_real)
    l_preco_real['text'] = valor_formatado_real

    frame_baixo.after(1000, info)


# configurando o frame cima
imagem = Image.open('icons8-bitcoin-40.png')
imagem = imagem.resize((30, 30), Image.ANTIALIAS)
imagem = ImageTk.PhotoImage(imagem)

l_icon = Label(frame_cima, image=imagem, compound=LEFT, bg=co1, relief=FLAT)
l_icon.place(x=10, y=10)

l_nome = Label(frame_cima, text='Bitcoin Price Tracker', bg=co1, fg=co2, relief=FLAT, anchor='center', font=('Arial 20'))
l_icon.place(x=50, y=5)

# configurando o frame baixo

l_preco_usd = Label(frame_baixo, text='', bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_preco_usd.place(x=10, y=50)

l_preco_euro = Label(frame_baixo, text='', bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_preco_euro.place(x=10, y=130)

l_preco_real = Label(frame_baixo, text='', bg=fundo, fg=co1, relief=FLAT, anchor='center', font=('Arial 12'))
l_preco_real.place(x=10, y=160)

info()

janela.mainloop()
