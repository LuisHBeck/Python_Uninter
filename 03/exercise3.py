import inquirer

def boas_vindas():
    print(f'Bem-vindo a loja do Luís Beck!')


def base_peso(peso):
    if peso < 3:
        return 40
    elif peso >=3 and peso < 10:
        return 50
    elif peso >=10 and peso < 30:
        return 60
    else:
        return 70
    

def multiplicador_pelo(pelo):
    if pelo == 'c':
        return 1
    elif pelo == 'm':
        return 1.5
    else:
        return 2
    

def valor_extra(extra):
    if extra == 1:
        return 10
    elif extra == 2:
        return 12
    elif extra == 3:
        return 15
    else:
        return 0

def cachorro_peso():
    peso = 0
    while 1 > peso or peso >= 50:
        try:
            peso = float(input('Entre com o peso do cachorro>> '))
            if (1 > peso or peso >= 50):
                print('Peso inválido! Tente novamente')
        except(ValueError):
            print('Você digitou um valor não numérico. Tente novamente')
    
    valor_base = base_peso(peso)
    return valor_base


def cachorro_pelo():
    pelo = " "
    while pelo not in 'cml':
        print('''c - Pelo Curto
                 m - Pelo Médio
                 l - Pelo Longo''')
        pelo = str(input('>> ')).strip().lower()
        if (pelo not in 'cml'):
            print('Pelo inválido. Tente novamente.')

    multiplicador = multiplicador_pelo(pelo)
    return multiplicador


def cachorro_extra():
    extra = 0
    while 0 > extra or extra > 3:
        try:
            print('''1 - Corte de Unhas - R$10,00
                     2 - Escovar Dentes - R$12,00
                     3 - Limpeza de Orelhas - R$15,00
                     0 - Não desejo mais nada''')
            extra = int(input('>> '))
            if (0 > extra or extra > 3):
                print('Opção inválida! Tente novamente')
        except(ValueError):
            print('Você digitou um valor não numérico. Tente novamente')

    vlr_extra = valor_extra(extra)
    return vlr_extra


def verificar_adicional():
    questions = [
        inquirer.List('adicional',
                        message="Deseja adicionar mais algum serviço?",
                        choices=['Corte de Unhas - R$10,00',
                                'Escovar Dentes - R$12,00',
                                'Limpeza de Orelhas - R$15,00',
                                'Não desejo mais nada'])
        ]
    answers = inquirer.prompt(questions)
    return answers['pelo']


cachorro_peso()