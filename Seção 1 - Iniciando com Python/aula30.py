#boas praticas de codigos

velocidade = 64 #velocidade atual do carro
local_carro = 101 #local em que o carro esta

RADAR_1 = 60 #velocidade maxima do radar\
LOCAL_1 = 100 #local onde o radar 1 esta
RADAR_RANGE = 1 #a distancia onde o radar pega

vel_carro_passou_radar_1 = velocidade > RADAR_1
carro_passsou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
                        local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1 = carro_passsou_radar_1 and vel_carro_passou_radar_1

if vel_carro_passou_radar_1:
    print('Carro passou da velocidade do radar 1')

if carro_passsou_radar_1:
    print('Carro passo em radar 1')

if carro_passsou_radar_1:
    print('Carro multado em radar 1')