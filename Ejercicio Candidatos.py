votos = int(input("Ingrese cantidad de votos: "))
candidatos = []
a = 0

for a in range (votos):
  candidatos.append (input())

nombres = set(candidatos)
votos_candidatos = list(nombres)
votos_nombre = list(nombres)

print (nombres)

a = 0

for a in range(len(votos_candidatos)):
  votos_candidatos[a] = 0
votos_candidatos[a] = 0
print (candidatos)

a = 0

for a in range(len(nombres)):
  if votos_nombre[a] in candidatos:
    votos_candidatos[a] += 1
if votos_nombre[a] in candidatos:
    votos_candidatos[a] += 1


ganador = votos_nombre.count(votos_candidatos)
  
print (ganador)