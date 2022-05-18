import bancoDados as bd
import sistema_servicos as ss
def pedido_tosa(dia, horario, valor):
    agendar = open(bd.diretorio, 'a')
    agendar.writelines("Tosa"+'\n')
    agendar.writelines("Dia:"+dia+'\n')
    agendar.writelines("Hora:"+horario+'\n')
    agendar.writelines('Valor R$'+valor+'\n')
