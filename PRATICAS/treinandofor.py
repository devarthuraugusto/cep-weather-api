import locale
import time

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')  # Define o locale para português do Brasil


inicio = time.time()

tempo_local = time.ctime(inicio)

print(f"Tempo{tempo_local}")
'''for i in range(100000):
    pass

print("Iniciando a pausa...")
time.sleep(3)
print("Cabo a pausa")
fim = time.time()

print(f"O código levou {fim - inicio:.2f} segundos pra rodar")'''

'''time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(inicio))''' #formata a data e hora de acordo com o formato especificado

