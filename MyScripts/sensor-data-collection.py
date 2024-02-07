import os

# ID único do sensor DS18B20
sensor_id = '28-00000xxxxxxx' # Substitua pelo ID do seu sensor

# Caminho para o dispositivo do sensor DS18B20
sensor_path = f'/sys/bus/w1/devices/{sensor_id}/w1_slave'

# Função para ler a temperatura do sensor
def ler_temperatura():
 try:
    with open(sensor_path, 'r') as sensor_file:
        linhas = sensor_file.readlines()
        segunda_linha = linhas[1].strip()
        temperatura_str = segunda_linha.split('=')[1]
        temperatura_celsius = float(temperatura_str) / 1000.0
    return temperatura_celsius
 except Exception as e:
    print(f"Erro ao ler temperatura: {str(e)}")
 return None

# Coleta e exibe a temperatura
temperatura = ler_temperatura()
if temperatura is not None:
 print(f'Temperatura: {temperatura}°C')
