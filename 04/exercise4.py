lista_colaboradores = []
id_global = 0

def boas_vindas():
    print(f'Bem-vindo ao Controle de Colaboradores do Luís Beck!')


def cadastrar_colaboradores(id_colab):
    nome = str(input('Digite o nome>> '))
    setor = str(input('Digite o setor>> '))
    salario = float(input('Digite o salário R$'))

    colaborador = {'id': id_colab,
                   'nome': nome,
                   'setor': setor,
                   'salario': setor}
    
    lista_colaboradores.append(colaborador)
