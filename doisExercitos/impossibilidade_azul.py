import globais
import main
import envia_vermelho
import envia_azul
import random as rd

def executa():
    porcentagem_impossibilidade = int(input('Exercito azul vai aceitar ataque?: '))
    if(porcentagem_impossibilidade>1):
        print('Azul aceitou fazer o ataque, {}avante!{}\n'.format(globais.effect.cyan, globais.effect.end))
        return 0

    else:
        print('Azul recusou o ataque, espera momento oportuno...')
        return 1

if (__name__ == "__main__"):
    #se rodar diretamente esse arquivo, executa a main
    main.enviar('vermelho')