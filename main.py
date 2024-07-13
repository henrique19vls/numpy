import numpy as np 

temperaturas = np.array([22,21,19,18.5,20.3,25,1])

media_temperatura = np.mean(temperaturas)
print(f"Media das temperaturas: {media_temperatura:2f}ºc")

max_temperatura = np.max(temperaturas)
min_temperatura = (temperaturas)
print(f"Temperatura maxima: {max_temperatura}ºc")
print(f"Temperatura minima: {max_temperatura}ºc")

altas_temperaturas = temperaturas[temperaturas > 21]
print(f"temperaturas acima de 21ºc: {altas_temperaturas}")

