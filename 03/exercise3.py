def boas_vindas():
    print(f'Bem-vindo a loja do Luís Beck!')


adicional = []

#retonar o valor com base no peso
def base_peso(peso):
    if peso < 3:
        return 40
    elif peso >=3 and peso < 10:
        return 50
    elif peso >=10 and peso < 30:
        return 60
    else:
        return 70
    
#retornar o multiplicador com base no pelo
def multiplicador_pelo(pelo):
    if pelo == 'c':
        return 1
    elif pelo == 'm':
        return 1.5
    else:
        return 2
    
#retronar o valor de serviço adicional
def valor_extra(servico):
    if servico == 1:
        return 10
    elif servico == 2:
        return 12
    elif servico == 3:
        return 15
    else:
        return 0
    
#retornar o valor final do calculo extra
def calculo_extra():
    valor_final = 0
    for valor in adicional:
        valor_final += valor

    return valor_final

#garantir que e peso esteja dentro do valor aceito
def cachorro_peso():
    peso = 0
    while 1 > peso or peso >= 50:
        try:
            peso = float(input('Entre com o peso do cachorro>> '))
            if (1 > peso or peso >= 50):
                print('Não aceitamos cachorros tão grandes')
        except(ValueError):
            print('Você digitou um valor não numérico. Tente novamente')
    
    valor_base = base_peso(peso)
    return valor_base

#garantir que o pelo seja atendido pelo petshop
def cachorro_pelo():
    pelo = " "
    while pelo not in 'cml':
        print('''Entre com o pelo do cachorro
        c - Pelo Curto
        m - Pelo Médio
        l - Pelo Longo''')
        pelo = str(input('>> ')).strip().lower()
        if (pelo not in 'cml'):
            print('Pelo inválido. Tente novamente.')

    multiplicador = multiplicador_pelo(pelo)
    return multiplicador

#printar os serviços adicionais
def opcoes_adicionais():
    print('''Deseja adicionar mais algum serviço?
    1 - Corte de Unhas - R$10,00
    2 - Escovar Dentes - R$12,00
    3 - Limpeza de Orelhas - R$15,00
    0 - Não desejo mais nada''')

#verifiar os inputs das opções extras
def cachorro_extra():
    while True:
        opcoes_adicionais()
        extra = int(input('>> '))

        while extra < 0 or extra > 3:
            try:
                opcoes_adicionais()
                extra = int(input('>> '))
                if extra < 0 or extra > 3:
                    print('Opção inválida! Tente novamente')
            except(ValueError):
                print('Você digitou um valor não numérico. Tente novamente')

        if extra == 0:
            valor_total = calculo_extra()
            return valor_total
        
        extra_valor = valor_extra(extra)
        adicional.append(extra_valor)

#realizar o calculo do serviço
def calculo(base, multiplicador, extra):
    return base * multiplicador + extra


def main():
    boas_vindas()
    base = cachorro_peso()
    multiplicador = cachorro_pelo()
    extra = cachorro_extra()
    
    print(F'Total a pagar(R$): {calculo(base, multiplicador, extra):.{2}f} (peso: {base}) * pelo: {multiplicador} + adicional(is): {extra}')


if __name__ == '__main__':
    main()