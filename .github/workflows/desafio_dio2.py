#Calculadora de partidas Rankeadas
#O Que deve ser utilizado**

#- Variáveis
#- Operadores
#- Laços de repetição
#- Estruturas de decisões
#- Funções

## Objetivo:

#Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
#depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

#Se vitórias for menor do que 10 = Ferro
#Se vitórias for entre 11 e 20 = Bronze
#Se vitórias for entre 21 e 50 = Prata
#Se vitórias for entre 51 e 80 = Ouro
#Se vitórias for entre 81 e 90 = Diamante
#Se vitórias for entre 91 e 100= Lendário
#Se vitórias for maior ou igual a 101 = Imortal

## Saída

#Ao final deve se exibir uma mensagem:
#"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**"

def partidas(vitorias, derrotas):
    saldo = vitorias - derrotas
    if saldo <= 10:
        classe = 'Ferro'
    elif saldo >= 11 and saldo <= 20:
        classe = 'Bronze'
    elif saldo >= 21 and saldo <=50:
        classe = 'Prata'
    elif saldo >=51 and saldo <= 80:
        classe = 'Ouro'
    elif saldo >=81 and saldo <= 90:
        classe = 'Diamante'
    elif saldo >= 91 and saldo <= 100:
        classe = 'Lendário'
    elif saldo >= 101:
        classe = 'Imortal'
    print(f'O herói tem um saldo de {saldo} vitórias e está no nível de {classe}.')

partidas(200, 180)