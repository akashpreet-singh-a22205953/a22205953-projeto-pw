import zipfile
import os

def unzip_to_static_meteo(zip_path, extract_to):
    # Verificar se a pasta de destino existe, caso contrário, criá-la
    if not os.path.exists(extract_to):
        os.makedirs(extract_to)

    # Abrir e descompactar o arquivo ZIP
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    print(f"Arquivos descompactados em: {extract_to}")

# Caminho do arquivo ZIP
zip_path = 'static/meteo/icons_ipma_weather.zip'

# Diretório de destino
extract_to = 'meteo/static/meteo/svg/'

unzip_to_static_meteo(zip_path, extract_to)
