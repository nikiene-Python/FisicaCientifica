import math
import numpy as np
import matplotlib.pyplot as plt

# Velocidade do projetil no eixo X
def VelocidadeX ( angulo = 0 , velocidadeInicial = 0.0 ):
    anguloA = math.radians( angulo )
    return velocidadeInicial * math.cos(anguloA)

# Velocidade do projetil no eixo Y
def VelocidadeY ( angulo = 0 , velocidadeInicial = 0.0 , gravidade = 9.81 , tempo = 0.0 , aFavorDaGravidade = True ):
    anguloA = math.radians( angulo )
    velocidade = velocidadeInicial * math.sin( anguloA )
    if aFavorDaGravidade:
        return velocidade - gravidade * tempo
    return velocidade

# Posição do projetil em relação ao eixo X
def PosicaoX ( posicaoInicial = 0.0 , velocidade = 0.0 , tempo = 0.0 ):
    return posicaoInicial + velocidade * tempo

# Posição do projetil em relação ao eixo Y
def PosicaoY ( posicaoInicial = 0.0 , velocidade = 0.0 , gravidade = 9.81 , tempo = 0.0 ):
    return posicaoInicial + ( velocidade * tempo ) - ( ( gravidade * ( tempo ** 2 ) ) / 2 )

# Velocidade total, na forma vetorial
def VelocidadeTotal ( velocidadeEixoX = 0.0 , velocidadeEixoY = 0.0 ):
    velocidadeTotal = math.sqrt ( ( ( velocidadeEixoX ** 2 ) + ( velocidadeEixoY ** 2 ) ) )
    return velocidadeTotal

# Angulo instantâneo do projetil
def Angulo ( VelocidadeX = 0.0 , VelocidadeY = 0.0 ):
    return math.atan( VelocidadeY / VelocidadeX )

# Força resistiva -> Coeficiente de arrasto da esfera * Densidade do ar * Área de seção Transversal * Velocidade inicial
def ForcaResistiva ( coeficienteArrasto = 0.47 , densidadeDoAr = 1.225 , areaSecaoTransversal = 0.8 , velocidadeInicial = 0 ):
    return 0.5 * coeficienteArrasto * densidadeDoAr * areaSecaoTransversal * ( velocidadeInicial ** 2 )

# Componente de aceleração do eixo X
def AceleracaoX ( forcaResistiva , massaDoObjeto , angulo ):
    return - ( forcaResistiva * np.cos ( angulo ) ) / massaDoObjeto

# Componente de aceleração do eixo Y
def AceleracaoY ( forcaResistiva = 0.0 , massaDoObjeto = 0.0 , gravidade = 9.81 , angulo = 0.0 ):
    return - gravidade - ( forcaResistiva * np.sin ( angulo ) ) / massaDoObjeto

# ---------------------------------------------------------------------------------------------------------------------- #

angulo = 75
velocidadeInicial = 15
tempoInicial = 0
tempoFinal = 3

# print(" --------------------------------------------------------------")
# print(" |  TEMPO  |   X   |   Y   |  VelX  |  VelY  |  VelT  |  ANG  |")
# print(" --------------------------------------------------------------")

# for i in np.linspace ( tempoInicial , tempoFinal , dtype=float , num = 10 ):
#     velocidadeX = VelocidadeX ( angulo = angulo , velocidadeInicial = velocidadeInicial )
#     velocidadeY = VelocidadeY ( angulo = angulo , velocidadeInicial = velocidadeInicial , tempo = i )
#     velocidadeTotal = VelocidadeTotal ( velocidadeEixoX = velocidadeX , velocidadeEixoY = velocidadeY )

#     posicaoX = PosicaoX ( velocidade = velocidadeX , tempo = i )
#     posicaoY = PosicaoY ( velocidade = VelocidadeY ( angulo = angulo , velocidadeInicial = velocidadeInicial , aFavorDaGravidade = False ) , tempo = i )
#     angulo = Angulo ( VelocidadeX = velocidadeX , VelocidadeY = velocidadeY )

#     print( "{tempo:8.3f} {posicaoX:8.3f} {posicaoY:8.3f} {velocidadeX:8.3f} {velocidadeY:8.3f} {velocidadeTotal:8.3f} {angulo:8.3f}".format (
#         tempo = i,
#         posicaoX = posicaoX,
#         posicaoY = posicaoY,
#         velocidadeX = velocidadeX,
#         velocidadeY = velocidadeY,
#         velocidadeTotal = velocidadeTotal,
#         angulo = np.degrees( angulo )
#     ))

x = np.array( [ 0 ] )
y = np.array( [ 0 ] )
velocidadeTotal = np.array( [ 0 ] )


for i in np.linspace ( tempoInicial , tempoFinal , dtype=float , num = 100 ):
    velocidadeX = VelocidadeX ( angulo = angulo , velocidadeInicial = velocidadeInicial )
    velocidadeY = VelocidadeY ( angulo = angulo , velocidadeInicial = velocidadeInicial , tempo = i )

    posicaoX = PosicaoX ( velocidade = velocidadeX , tempo = i )
    posicaoY = PosicaoY ( velocidade = VelocidadeY ( angulo = angulo , velocidadeInicial = velocidadeInicial , aFavorDaGravidade = False ) , tempo = i )

    if posicaoY < 0:
        break

    x = np.append ( x , posicaoX )
    y = np.append ( y , posicaoY )
    velocidadeTotal = np.append ( velocidadeTotal , VelocidadeTotal ( velocidadeEixoX = velocidadeX , velocidadeEixoY = velocidadeY ) )

    forcaResistiva = ForcaResistiva ( velocidadeInicial =  velocidadeTotal )

    aceleracaoX = AceleracaoX ( forcaResistiva = forcaResistiva, angulo = angulo )
    aceleracaoY = AceleracaoY ( forcaResistiva = forcaResistiva, angulo = angulo )


fig , ax = plt.subplots ( )
fig.set_size_inches( 10 , 7 )
ax.plot ( x , y )
ax.set_title ( "Trajetória do Projetil" )
ax.set_xlabel ( "Posição X" )
ax.set_ylabel ( "Posição Y" )
plt.xticks( range ( 0 , 15 ) )
plt.yticks( range ( 0 , 20 , 1 ) )
plt.show ( )