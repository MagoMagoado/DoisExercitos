import globais
import main
import envia_vermelho
import envia_azul
import impossibilidade_azul as imp_azul
import random as rd

def executar(cor):

    tempo_soldado = 0
    tempo_soldado = tempo_soldado + rd.randrange(3600, 4200)
    captura = 0 #0 não foi capturado//1 foi capturado

    porcentagem_captura = int(input('\nQual a porcentagem de captura?: '))
    if(porcentagem_captura >= 45):
        print('{}Soldado abençoado{}, não foi capturado!'.format(globais.effect.cyan, globais.effect.end))
        globais.tempo_total = globais.tempo_total + tempo_soldado

        if (cor == 'vermelho'):
            globais.tempo_total_vermelho = globais.tempo_total_vermelho + tempo_soldado
            if(globais.vermelho_em_transito == True):
                globais.tempo_ultimo_vermelho = tempo_soldado
            envia_vermelho.retorno_captura(tempo_soldado, captura)
        else:
            globais.tempo_total_azul = globais.tempo_total_azul + tempo_soldado
            if(globais.azuis_fracassados == 0 and globais.vermelho_em_transito == True and tempo_soldado>=globais.tempo_ultimo_vermelho):
                print('\ntempo do soldado azul foi: {}{}{}. O último soldado vermelho foi {}{}{}.'.format(globais.effect.bold, tempo_soldado, globais.effect.end, globais.effect.bold, globais.tempo_ultimo_vermelho, globais.effect.end))
                print('{}Azul chegou ao exército vermelho ao mesmo tempo que o vermelho chegou ao azul, que azar!{}'.format(globais.effect.yellow, globais.effect.end))
                print('Novo soldado {}azul{} é enviado para confirmar horário'.format(globais.effect.blue, globais.effect.end))
                #reseta variáveis para 0
                globais.teste_hr_max_vermelho = 0
                globais.tempo_ultimo_vermelho = 0
                globais.azuis_fracassados = 0
                globais.vermelho_em_transito = False
                envia_azul.executar()
            if(globais.vermelho_em_transito == True and (globais.azuis_fracassados+tempo_soldado)>=globais.tempo_ultimo_vermelho):
                print('\ntempo dos soldados azuis tentanto atravessar foi: {}{}{}. O último soldado vermelho foi {}{}{}.'.format(globais.effect.bold, globais.azuis_fracassados, globais.effect.end, globais.effect.bold, globais.tempo_ultimo_vermelho, globais.effect.end))
                print('{}Azul chegou ao exército vermelho ao mesmo tempo que o vermelho chegou ao azul, que azar!{}'.format(globais.effect.yellow, globais.effect.end))
                print('Novo soldado {}azul{} é enviado para confirmar horário'.format(globais.effect.blue, globais.effect.end))
                #reseta variável para 0
                globais.teste_hr_max_vermelho = 0
                globais.tempo_ultimo_vermelho = 0
                globais.vermelho_em_transito = False
                envia_azul.executar()
            else:
                #essas variaveis resetam por que significa que azul chegou antes do vermelho e confirmou ataque
                globais.tempo_ultimo_vermelho = 0
                globais.vermelho_em_transito = False                
                envia_azul.retorno_captura(tempo_soldado, captura)

    else:
        print('{}Soldado desgraçado{}, foi capturado!\n'.format(globais.effect.yellow, globais.effect.end))
        captura = 1
        if (cor == 'vermelho'):
            tempo_soldado = 12601
            globais.tempo_total = globais.tempo_total + tempo_soldado
            globais.tempo_total_vermelho = globais.tempo_total_vermelho + tempo_soldado

            globais.teste_hr_max_azul = globais.teste_hr_max_azul + tempo_soldado
            if(globais.teste_hr_max_azul > 4200 and globais.azul_primeiro_envio == True):
                globais.teste_hr_max_azul = 0
                print('Passou 4201s desde a ida do último azul...')
                print('outro soldado {}azul{} deve ser enviado...'.format(globais.effect.blue, globais.effect.end))
                envia_azul.executar()
            
            else:
                envia_vermelho.retorno_captura(tempo_soldado, captura)

        else:
            #se o tempo de soldados capturados azuis igualar o tempo de chegada do ultimo vermelho, os dois chegam ao mesmo tempo
            if(globais.vermelho_em_transito == True):
                globais.azuis_fracassados = globais.azuis_fracassados + 4201
            tempo_soldado = 4201
            globais.tempo_total = globais.tempo_total + tempo_soldado
            globais.tempo_total_azul = globais.tempo_total_azul + tempo_soldado
            
            globais.teste_hr_max_vermelho = globais.teste_hr_max_vermelho + tempo_soldado
            if(globais.vermelho_em_transito == True and globais.azuis_fracassados >= globais.tempo_ultimo_vermelho):
                globais.vermelho_em_transito = True
                print('\nTempo dos soldados azuis tentando atravessar o campo foi de: {}{}{}. O último soldado vermelho foi {}{}{}.'.format(globais.effect.bold, globais.azuis_fracassados, globais.effect.end, globais.effect.bold, globais.tempo_ultimo_vermelho, globais.effect.end))
                print('Vermelho chegou ao campo do exército azul e pergunta...\n')
                #reseta variável para 0
                globais.teste_hr_max_vermelho = 0
                globais.vermelho_em_transito = False
                globais.tempo_ultimo_vermelho = 0
                globais.azuis_fracassados = 0 
                if(imp_azul.executa() == 0):
                    print('Exercito azul entrará em ação!')
                    #envia o valor azul para chamar
                    main.enviar('azul')

                #se azul recusou
                else:
                    print('outro soldado {}vermelho{} deve ser enviado para propor outra hora...'.format(globais.effect.red, globais.effect.end))
                    envia_vermelho.executar()

            elif(globais.teste_hr_max_vermelho > 12600):
                globais.vermelho_em_transito = True
                #reseta variável para 0
                globais.teste_hr_max_vermelho = 0
                globais.tempo_ultimo_vermelho = 0
                globais.azuis_fracassados = 0 

                print('Passou 12601s desde a ida do último vermelho...')
                print('outro soldado {}vermelho{} deve ser enviado...'.format(globais.effect.red, globais.effect.end))
                envia_vermelho.executar()
            else:                
                envia_azul.retorno_captura(tempo_soldado, captura)

if (__name__ == "__main__"):
    #se rodar diretamente esse arquivo, executa a main
    main.enviar('vermelho')