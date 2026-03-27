import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('OPENWHEATER_KEY') #API_KEY

def buscar_clima(cidade):
    print(f"Buscando clima para {cidade}...")
    
    
    url = "https://api.openweathermap.org/data/2.5/weather" #URL DA API
    params = {
        'q': cidade,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'pt_br'
    }

    try:#Fazendo a requisição para a API
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 404: #Verificando se a cidade existe ou não
            print(f'❌ Cidade {cidade} não encontrada. Tente novamente!')
            return None
        

        if response.status_code == 401:#verificando se a chave de API é válida ou não
            print('❌ Chave de API inválida. Verifique sua chave e tente novamente!')
            return None
        
        if response.status_code == 200:#Verificando se a resposta da API  deu certo
            data = response.json()
            return data
        else:
            print(f"ERRO: {response.status_code} - {response.text}")
            return None
        
    except requests.exceptions.ConnectionError:#Verificando se há conexão com a internet
        print("Sem conexão com a internet.")
        return None

    except Exception as e:#Tratando outros erros 
        print(f"Ocorreu um erro: {e}")
        return None



def mostrar_clima(data): # Valores que serão mostrados para o usuário sobre o clima da cidade pesquisada
    cidade = data['name']
    pais = data['sys']['country']
    temperatura = data['main']['temp']
    sensacao_termica = data['main']['feels_like']
    temperatura_min = data['main']['temp_min']
    temperatura_max = data['main']['temp_max']
    descricao = data['weather'][0]['description']
    umidade = data['main']['humidity']
    vento = data['wind']['speed']

    emoji = "☀️"
    
    desc_lower = descricao.lower()

    if "chuva" in desc_lower:
        emoji = "🌧️"
    elif "nublado" in desc_lower:
        emoji = "☁️"
    elif "limpo" in desc_lower:
        emoji = "☀️"
    elif "neve" in desc_lower:
        emoji = "❄️"
    elif "tempestade" in desc_lower:
        emoji = "⛈️"

    print("\n" + "="*40)
    print(f"{emoji} Clima em {cidade.upper()}, {pais.upper()} ")
    print("="*40)
    print(f"Temperatura: {temperatura:.1f}°C")
    print(f"Sensação Térmica: {sensacao_termica:.1f}°C")
    print(f"Temperatura Mínima: {temperatura_min:.1f}°C")
    print(f"Temperatura Máxima: {temperatura_max:.1f}°C")
    print(f"Descrição: {descricao.capitalize()}")
    print(f"Umidade: {umidade}%")
    print(f"Velocidade do Vento: {vento} m/s")
    print("="*40)

