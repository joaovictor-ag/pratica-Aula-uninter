def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def existeArq(nomeArq):
    try:

        a = open(nomeArq, 'rt')
        a.close()

    except FileNotFoundError:
        return False

    else:
        return  True

def CriarArq(nomeArq):
    try:
        a = open(nomeArq, 'wt+')
        a.close()
    except:
        print('Erro Na Criação do Arquivo')
    else:
        print('Aquivo {} Foi criado com Sucesso!\n'.format(nomeArq))

def listarArq(nomeArq):
    try:
        a = open(nomeArq, 'rt')
    except:
        print('Erro ao Ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()
def cadastrarJogo(nomeArq, nomeJogo, nomeVideoGame):
    try:
        a = open(nomeArq, 'at')
    except:
        print('Erro ao abrir o Arquivo')
    else:
        a.write('{}; {}\n'.format(nomeJogo,nomeVideoGame))
    finally:
        a.close()



arquivo = 'games.txt'
if existeArq(arquivo):
    print('Arquivo Localizado!')
else:
    print('Arquivo Inexistente')
    CriarArq(arquivo)

nomesVideoGameValidos = ['PlayStation 1', 'PlayStation 2', 'PlayStation 3', 'PlayStation 4', 'Xbox One', 'Xbox Series', 'Nintendo Switch', 'PC']

while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar Cadastros')
    print('3 - Sair')

    op = valida_int('Escolha a opção desejada: ', 1, 3)
    if op == 1:
        print('Opção de Cadastrar um novo item selecionada...\n')
        nomeJogo = input('Nome Do Jogo: ')
        nomeVideoGame = input('Nome do VideoGame: ')
        while nomeVideoGame not in nomesVideoGameValidos:
            nomeVideoGame = input('VideoGame inválido! Digite um nome válido: ')
        cadastrarJogo(arquivo, nomeJogo, nomeVideoGame)


    elif op == 2:
        print('Opção de listar selecionada...\n')
        listarArq(arquivo)


    elif op == 3:
        print('Encerrando o Programa...')
        break