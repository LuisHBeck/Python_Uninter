# função para verificar o desconto a ser aplicado
def verificar_desconto(qnt):
    if qnt < 200:
        return 0
    elif qnt >= 200  or qnt < 1000:
        return 0.05
    elif qnt >= 1000 or qnt < 200:
        return 0.1
    else:
        return 0.15
    
#função para retornar o valor final
def valor_final(valor_unitario, qnt):
    desconto = verificar_desconto(qnt)
    valor_sem_desconto = valor_unitario * qnt
    valor_com_desconto = valor_sem_desconto - (valor_sem_desconto * desconto)

    return valor_sem_desconto, valor_com_desconto

    
def boas_vindas():
    print(f'Bem-vindo a loja do Luís Beck!')

# função para redeceber as entradas
def entradas():
    valor = float(input('Entre com o valor do produto>> '))
    quantidade = float(input('Entre com a quantidade do produto>> '))
    valor_sem_desconto, valor_com_desconto = valor_final(valor, quantidade)
    saidas(valor_sem_desconto, valor_com_desconto)

#função para as saídas 
def saidas(sem_desconto, com_desconto):
    print(f'O valor SEM desconto: R${sem_desconto:.{2}f}')
    print(f'O valor COM desconto: R${com_desconto:.{2}f}')

#função principal para executar a sequência de funçôes do código
def main():
    boas_vindas()
    entradas()

# boas praticas para rodar a aplicação
if __name__ == '__main__':
    main()