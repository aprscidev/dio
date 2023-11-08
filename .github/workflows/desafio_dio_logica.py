#Desafio DIO - Classificador de nível de herói
#O que deve ser utilizado: variáveis, operadores, laços de repetição, estruturas de decisões

#Objetivo
#Crie uma variável para armazenar o nome e a qunatidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:
#Se XP for menor do que 1.000 = Ferro
#Se XP for entre 1.001 e 2.000 = Bronze
#Se XP for entre 2.001 e 5.000 = Prata
#Se XP for entre 6.001 e 7.000 = Ouro
#Se XP for entre 7.001 e 8.000 = Platina
#Se XP for entre 8.001 e 9.000 = Ascendente
#Se XP for entre 9.001 e 10.000= Imortal
#Se XP for maior ou igual a 10.001 = Radiante

#Saída
#Ao final deve se eibir uma mensagem
#"O Herói de nome **{nome}** está no nível de **{nivel}**"


nome = str(input('Digite o nome do herói: ')).upper().strip()
xp = int(input('Digite a quantidade de XP do herói: '))
nomexp = " "

#Condições

if xp <= 1000:
    nomexp = "Ferro"
elif xp > 1001 and xp <= 2000:
    nomexp = "Bronze"
elif xp > 2001 and xp <= 5000:
    nomexp = "Prata"
elif xp > 6001 and xp <= 7000:
    nomexp = "Ouro"
elif xp > 7001 and xp <= 8000:
    nomexp = "Platina"
elif xp > 8001 and xp <= 9000:
    nomexp = "Ascendente"
elif xp > 9001 and xp <= 10000:
    nomexp = "Imortal"
elif xp >= 10001:
    nomexp = "Radiante"

heroi = (nome, xp, nomexp)  # Variável do tipo lista para armazenar nome e XP do herói

print(f'O Herói de nome {heroi[0]} está no nível de {heroi[2]}.')
print('--FIM--')

