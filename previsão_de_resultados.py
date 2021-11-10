import requests
def banco_de_dados():
    dados = requests.get("https://previsao-de-resultados-default-rtdb.firebaseio.com/.json")
    sp_golf = dados.json()['sp']['gols_feitos']
    sp_gols = dados.json()['sp']['gols_sofridos']
    print (sp_golf)
    print (sp_gols)
banco_de_dados()
