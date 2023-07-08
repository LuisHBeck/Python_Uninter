# biblioteca para formatação de tabelas
from prettytable import PrettyTable

valores = []

#formatando a tabela com prettytable (lib)
def tabela_cardapio():
    table = PrettyTable()
    table.field_names = ['N° DE BOLAS', 'Sabor Tradicional (tr)',
                        'Sabor Premium (pr)', 'Sabor especial (es)']

    table.add_row([1, 'R$ 6,00', 'R$ 7,00', 'R$ 8,00'])
    table.add_row([2, 'R$10,00', 'R$12,00', 'R$14,00'])
    table.add_row([3, 'R$14,00', 'R$17,00', 'R$20,00'])

    print(table)

# verificando o input de numero de bolas e o sabor e retornando o valor
def valor_sorvete(numero, sabor):
    if numero == 1:
        if sabor == 'tr':
            return 6
        elif sabor == 'pr':
            return 7
        else:
            return 8
    elif numero == 2:
        if sabor == 'tr':
            return 10
        elif sabor == 'pr':
            return 12
        else:
            return 14
    else:
        if sabor == 'tr':
            return 14
        elif sabor == 'pr':
            return 17
        else:
            return 20

# função para guardar os valores unitários
def valor_pedido_unitario(sabor, numero):
    preco = valor_sorvete(numero, sabor)
    valores.append(preco)

# função para calcular o valor final do pedido
def valor_final():
    preco_final = 0
    for preco in valores:
        preco_final += preco

    return preco_final

# função para garantir o input correto dos sabores disponiveis
def verificar_sabores():
    sabor = " "
    while sabor not in 'trpres':
        sabor = str(input('Entre com o sabor desejado (tr/es/pr)>> ')).strip().lower()
        if (sabor not in 'trpres'):
            print('Sabor inválido. Tente novamente.')

    return sabor

# função para garantir o input correto dos numero de bolas disponiveis
def verificar_numero_bolas():
    numero = 0
    while 1 > numero or numero > 3:
        try:
            numero = int(input('Entre com o número de bolas de sorvete desejado (1/2/3)>> '))
            if 1 > numero or numero > 3:
                print('Número de bolas de sorvete inválido. Tente novamente')
        except:
            print('Número de bolas de sorvete inválido. Tente novamente')

    return numero

# função para veririficar se terá um novo pedido
def verificar_continuidade():
    continuar = " "
    while continuar not in 'sn':
        continuar = str(input('Deseja mais algum sorvete? (s/n)>> '))
        if continuar in 'nao':
            break
        else:
            main()

# função principal para chamar todas em sequencia
def main():
    sabor = verificar_sabores()
    numero = verificar_numero_bolas()
    valor_pedido_unitario(sabor, numero)
    verificar_continuidade()
    valor_final()

# boa pratica para execução do programa 
if __name__ == '__main__':
    print('Bem-vindo a Sorveteria do Luís Beck')
    tabela_cardapio()
    main()
    final = valor_final()
    print(f'O valor total a ser pago: R${final:.2f}')