import main
import globais
import captura
import random as rd

def executar():
    globais.azul_primeiro_envio = True

    print('total do azul: {}'.format(globais.quant_azul))
    globais.quant_azul = globais.quant_azul - 1
    print('{} **AZUL ENVIADO** {}'.format(globais.effect.blue, globais.effect.end))
    captura.executar('azul')
        
#depois de retornar de captura
def retorno_captura(tempo_azul, captura):

    if(globais.quant_azul == 0):
        print('{}Você perdeu a guerra!\nquantidade insuficiente de soldados{}'.format(globais.effect.bold, globais.effect.end))
        print('Tempo total: {}'.format(globais.tempo_total))
        print('Tempo total vermelho: {}'.format(globais.tempo_total_vermelho))
        print('Tempo total azul: {}'.format(globais.tempo_total_azul))
        print('Estiveram em campo: {} soldados vermelhos e {} soldados azuis.\n'.format(5 - globais.quant_vermelho, 10 - globais.quant_azul))
    else:
        if (captura == 0):
            print('O tempo do soldado foi: {}\n'.format(tempo_azul))
            print('{}AZUL CHEGOU E SINALIZADOR FOI DISPARADO!{}'.format(globais.effect.bold, globais.effect.end))
            print('{}VITÓRIA{}\n'.format(globais.effect.green, globais.effect.end)
            )
            print('Tempo total: {}'.format(globais.tempo_total))
            print('Tempo total vermelho: {}'.format(globais.tempo_total_vermelho))
            print('Tempo total azul: {}'.format(globais.tempo_total_azul))
            print('Estiveram em campo: {} soldados vermelhos e {} soldados azuis.\n'.format(5 - globais.quant_vermelho, 10 - globais.quant_azul))

        else:
            print('Passou 4201 segundos...')
            print('outro soldado {}azul{} deve ser enviado...'.format(globais.effect.blue, globais.effect.end))
            executar()

if (__name__ == "__main__"):
    #se rodar diretamente esse arquivo, executa a main
    main.enviar('vermelho')
