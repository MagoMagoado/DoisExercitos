#vars globais
quant_vermelho = 5
quant_azul = 10
tempo_soldado = 0
tempo_total_vermelho = 0
tempo_total_azul = 0
tempo_total = 0

#continua sendo falso até o azul enviar pelo menos 1 vez
azul_primeiro_envio = False

#essas variáveis fazem o teste se vermelho e azul chegaram ao mesmo tempo para passar mensagem
vermelho_em_transito = False
tempo_ultimo_vermelho = 0
azuis_fracassados = 0

teste_hr_max_vermelho = 0
teste_hr_max_azul = 0

#efeitos de cor
class effect:
        bold = '\033[1m'
        red = '\033[91m'
        blue = '\033[94m'
        cyan = '\033[96m'
        yellow = '\033[93m'
        green = '\033[92m'
        end = '\033[0m'