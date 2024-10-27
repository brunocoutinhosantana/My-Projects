def vota(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'


print('-'*30)
atual = int(input('Em que ano você nasceu? '))
print(vota(atual))
