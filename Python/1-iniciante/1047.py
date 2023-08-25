inicio, inicio2, fim, fim2 = map(int, input().split(" "))

if (inicio == fim and inicio2 == fim2) or inicio > fim:
    fim += 24

hora_inicio = inicio * 60 + inicio2
hora_final = fim * 60 + fim2

duracao = hora_final - hora_inicio

horas = duracao // 60
minutos = duracao % 60

if horas < 0:
    horas = 24 + horas

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")