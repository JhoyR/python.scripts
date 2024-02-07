import os
import hashlib
from time import time
# Diretório a ser monitorado
monitor_directory = "/caminho//diretorio" # Coloque o caminho do seu diretório aqui.

# Dário para armazenar os hashes dos arquivos
file_hashes =icializar_hashes_arquivos(monitor_directory)

# Tempo da última varredura do diretório
prev_scan_time = time()

def inicializar_hashes_arquivos(directory):
   """
   Inicializa o dicionário de hashes com os valores atuais de todos os arquivos no diretório fornecido.
   """
   file_hashes = {}
   for root, _, files in os.walk(directory):
       for file in files:
           file_path = os.path.join(root, file)
           file_hashes[file_path] = calcular_hash_arquivo(file_path)
   return file_hashes


def calcular_hash_arquivo(file_path):
   """
   Calcula o hash MD5 do arquivo fornecido.
   """
   hasher = hashlib.md5()
   with open(file_path, 'rb') as f:
       while True:
           block = f.read(8192)
           if not block:
               break
           hasher.update(block)
   return hasher.hexdigest()


def obter_arquivos_alterados(prev_file_hashes, current_file_hashes):
   """
   Compara dois dicionários de hashes de arquivos e retorna uma lista de arquivos com hashes alterados.
   """
   arquivos_alterados = []
   for file_path, current_hash in current_file_hashes.items():
       if file_path not in prev_file_hashes or prev_file_hashes[file_path] != current_hash:
           arquivos_alterados.append(file_path)
   return arquivos_alterados


def imprimir_arquivos_alterados(arquivos_alterados):
   """
   Imprime a lista de arquivos alterados.
   """
   if arquivos_alterados:
       print("Os seguintes arquivos foram alterados:")
       for file_path in arquivos_alterados:
           print(f"- {file_path}")
   else:
       print("Nenhum arquivo foi alterado.")


while True:
   try:
       # Obtém o estado atual dos arquivos no diretório monitorado
       current_file_hashes = {file_path: calcular_hash_arquivo(file_path) for file_path in obter_arquivos_em_diretorio(monitor_directory)}

       # Verifica se houve alterações
       arquivos_alterados = obter_arquivos_alterados(file_hashes, current_file_hashes)

       # Imprime a lista de arquivos alterados
       imprimir_arquivos_alterados(arquivos_alterados)

       # Atualiza o dicionário de hashes de arquivos
       file_hashes = current_file_hashes

       # Aguarda um tempo antes de varrer o diretório novamente
       time.sleep(5)

   except Exception as e:
       print(f"Erro: {e}")