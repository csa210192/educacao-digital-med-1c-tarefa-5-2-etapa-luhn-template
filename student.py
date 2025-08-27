#Letícia Bastos, Marina Ministério, Carolina Schettino

numero = input().strip()
digitos = [int(x) for x in numero]
digitos.reverse()

impares_somados = sum(digitos[0::2])
pares_somados = 0
for d in digitos[1::2]:
  dobro = d * 2
  if dobro > 9:
    dobro -= 0
  pares_somados =+ dobro

total = impares_somados = pares_somados
if total %10 == 0:
  print ("Cartão válido")
else:
  print ("Cartão inválido")
