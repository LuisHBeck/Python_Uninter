#import de bibliotecas utilizadas 
#inquirer para receber opções e os para acessar funções do terminal
#pip install inquirer
import inquirer, os

lista_colaboradores = []
id_global = 0

def boas_vindas():
    print(f'Bem-vindo ao Controle de Colaboradores do Luís Beck!')
    print()

#receber o input e retornar a opção escolhida com a lib inquirer do menu principal
def menu_principal():
    menu_escolhas = [
            inquirer.List('menu',
                            message="Escolha a opção desejada:",
                            choices=['1 - Cadastrar Colaborador',
                                     '2 - Consultar Colaborador(es)',
                                     '3 - Remover Colaborador',
                                     '4 - Sair'],
                            ),
            ]
    resposta = inquirer.prompt(menu_escolhas)
    return resposta['menu']

#chamar as funções escolhidas no menu principal
def menu_execução():
    opcao = menu_principal()

    if opcao == '1 - Cadastrar Colaborador':
        cadastrar_colaboradores(id_global)
    elif opcao == '2 - Consultar Colaborador(es)':
        consultar_colaborador()
    elif opcao == '3 - Remover Colaborador':
        remover_colaborador()
    else:
        print('Muito obrigado!')
        quit()

#lógica para cadastar um colaborador
def cadastrar_colaboradores(id_colab):
    # os.system("cls")
    global id_global
    id_colaborador = id_colab + 1
    nome = str(input('Digite o nome>> '))
    setor = str(input('Digite o setor>> '))
    salario = float(input('Digite o salário R$'))

    colaborador = {'id': id_colaborador,
                   'nome': nome,
                   'setor': setor,
                   'salario': salario}
    
    lista_colaboradores.append(colaborador)
    id_global += 1

    menu_execução()

#lógica para a consulta de um colaboardor
def consultar_colaborador():
    while True:
        opcao = [
                inquirer.List('escolha',
                                message="Escolha a opção desejada:",
                                choices=['1 - Consultar todos',
                                        '2 - Consultar por ID',
                                        '3 - Consultar por setor',
                                        '4 - Retornar'],
                                ),
                ]
        resposta = inquirer.prompt(opcao)
        
        if resposta['escolha'] == "1 - Consultar todos":
            # os.system("cls")
            for colaborador in lista_colaboradores:
                for k, v in colaborador.items():
                    print(f'{k}: {v}')
                print('—'*20)
        
        elif resposta['escolha'] == '2 - Consultar por ID': 
            # os.system("cls")
            existe = False
            id_consulta = int(input('Digite o id do colaborador>> '))

            for colaborador in lista_colaboradores:
                if colaborador['id'] == id_consulta:
                    existe = True
                    for k,v in colaborador.items():
                        print(f'{k}: {v}')
                    print('—'*20)    

            if existe == False:
                print('Colaborador não encontrado!')

        elif resposta['escolha'] == '3 - Consultar por setor':
            # os.system("cls")
            existe = False
            setor_consulta = str(input('Digite o setor do(os) colaborador(es)>> '))

            for colaborador in lista_colaboradores:
                if colaborador['setor'] == setor_consulta:
                    existe = True
                    for k,v in colaborador.items():
                        print(f'{k}: {v}')
                    print('—'*20)

            if existe == False:
                print('Setor não encontrado!')   

        else:
            break
    menu_execução()

#lógica para a remoção de um colaborador
def remover_colaborador():
    # os.system("cls")
    existe = False
    id_colaborador = int(input('Digite o id do colaborador a ser removido>> '))

    for colaborador in lista_colaboradores:
        if colaborador['id'] == id_colaborador:
            existe = True
            lista_colaboradores.remove(colaborador)

    if existe == False:
        print('Colaborador não encontrado')

    menu_execução()


def main():
    boas_vindas()
    menu_execução()


if __name__ == '__main__':
    main()
