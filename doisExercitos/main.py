import globais
import envia_vermelho
import envia_azul

def enviar(turno):

    ###############Envia a tropa##############
    if (turno == 'vermelho'):
        envia_vermelho.executar()
    else:
        envia_azul.executar()
    ##########################################

if (__name__ == "__main__"):    
    print('\n{}BEM VINDO AO DILEMA DOS DOIS EXÉRCITOS{}'.format(globais.effect.bold, globais.effect.end))
    #começa enviando o vermelho, com 5 soldados
    enviar('vermelho')