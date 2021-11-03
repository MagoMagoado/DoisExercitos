import main
import impossibilidade_azul as imp_azul
import globais
import captura
import random as rd

def executar():

    print('total do vermelhos: {}'.format(globais.quant_vermelho))
    globais.quant_vermelho = globais.quant_vermelho - 1
    print('{} **VERMELHO ENVIADO** {}'.format(globais.effect.red, globais.effect.end))
    captura.executar('vermelho')
        
#depois de retornar de captura
def retorno_captura(tempo_vermelho, captura):
    if(globais.quant_vermelho == 0):
        print('{}Você perdeu a guerra!\nquantidade insuficiente de soldados{}'.format(globais.effect.bold, globais.effect.end))
        print('Tempo total: {}'.format(globais.tempo_total))
        print('Tempo total vermelho: {}'.format(globais.tempo_total_vermelho))
        print('Tempo total azul: {}'.format(globais.tempo_total_azul))
        print('Estiveram em campo: {} soldados vermelhos e {} soldados azuis.\n'.format(5 - globais.quant_vermelho, 10 - globais.quant_azul))
    else:
        if (captura == 0):
            print('O tempo do soldado foi: {}\n'.format(tempo_vermelho))

            #se azul aceitou ataque
            if(globais.vermelho_em_transito == True):
                main.enviar('azul')
            else:
                if(imp_azul.executa() == 0):
                    print('Exercito azul entrará em ação!')
                    #envia o valor azul para chamar
                    main.enviar('azul')

                #se azul recusou
                else:
                    print('outro soldado {}vermelho{} deve ser enviado para propor outra hora...'.format(globais.effect.red, globais.effect.end))
                    executar()

        else:
            if(globais.azul_primeiro_envio == False):
                print('Passou 12601 segundos...')
                print('outro soldado {}vermelho{} deve ser enviado...'.format(globais.effect.red, globais.effect.end))
                executar()
            else:
                print('Exercito azul entrará em ação!')
                #envia o valor azul para chamar
                #main.enviar(quant_soldado, quem é o time atual, quem vai ser o turno)
                main.enviar('azul')

if (__name__ == "__main__"):
    #se rodar diretamente esse arquivo, executa a main
    main.enviar('vermelho')
