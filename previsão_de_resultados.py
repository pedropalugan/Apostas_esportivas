import requests
from tkinter import *


#interface gráfica


dados = requests.get ("https://previsao-de-resultados-default-rtdb.firebaseio.com/.json")
dados = dados.json()

#condições para o 1° time
def primeiro_time():
    if time1.get() == "ame-mg" or time1.get() == "america mineiro" or time1.get() == "ame-mineiro" or time1.get() == "américa mineiro" or time1.get() == "américa-mg" or time1.get() == "america-mg" or time1.get() == "america-mineiro":
        nome_time1["text"] = "AMÉRICA-MG"
        jogos_time1["text"] = "JOGOS: {:.0f}".format(dados['ame']['jogos'])
        gols_feitos_time1["text"] = "GOLS FEITOS: {:.0f}".format(dados['ame']['gols_feitos'])
        gols_sofridos_time1["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['ame']['gols_sofridos'])
        golf_por_jogo_time1 = (dados['ame']['gols_feitos'])/(dados['ame']['jogos'])
        gols_feitos_jogo_time1["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time1)
        gols_por_jogo_time1 = (dados['ame']['gols_sofridos'])/(dados['ame']['jogos'])
        gols_sofridos_jogo_time1["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time1)
    elif time1.get() == "atl-mg" or time1.get() == "atletico mineiro" or time1.get() == "atl-mineiro" or time1.get() == "atlético mineiro" or time1.get() == "atlético-mg" or time1.get() == "atletico-mg" or time1.get() == "atletico mineiro":
        nome_time1["text"] = "ATLÉTICO-MG"
        jogos_time1["text"] = "JOGOS: {:.0f}".format(dados['atl-mg']['jogos'])
        gols_feitos_time1["text"] = "GOLS FEITOS: {:.0f}".format(dados['atl-mg']['gols_feitos'])
        gols_sofridos_time1["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['atl-mg']['gols_sofridos'])
        golf_por_jogo_time1 = (dados['atl-mg']['gols_feitos'])/(dados['atl-mg']['jogos'])
        gols_feitos_jogo_time1["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time1)
        gols_por_jogo_time1 = (dados['atl-mg']['gols_sofridos'])/(dados['atl-mg']['jogos'])
        gols_sofridos_jogo_time1["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time1)
    elif time1.get() == "atl-go" or time1.get() == "atletico goianiense" or time1.get() == "atlético goianiense" or time1.get() == "atlético-go" or time1.get() == "atletico-go" or time1.get() == "atletico-go":
        nome_time1["text"] = "ATLÉTICO-GO"
        jogos_time1["text"] = "JOGOS: {:.0f}".format(dados['atl-go']['jogos'])
        gols_feitos_time1["text"] = "GOLS FEITOS: {:.0f}".format(dados['atl-go']['gols_feitos'])
        gols_sofridos_time1["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['atl-go']['gols_sofridos'])
        golf_por_jogo_time1 = (dados['atl-go']['gols_feitos'])/(dados['atl-go']['jogos'])
        gols_feitos_jogo_time1["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time1)
        gols_por_jogo_time1 = (dados['atl-go']['gols_sofridos'])/(dados['atl-go']['jogos'])
        gols_sofridos_jogo_time1["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time1)
    elif time1.get() == "atl-pr" or time1.get() == "atletico paranaense" or time1.get() == "atl-paranaense" or time1.get() == "atlético paranaense" or time1.get() == "atlético-pr" or time1.get() == "atletico-pr" or time1.get() == "atletico-pr":
        nome_time1["text"] = "ATLÉTICO-PR"
        jogos_time1["text"] = "JOGOS: {:.0f}".format(dados['atl-pr']['jogos'])
        gols_feitos_time1["text"] = "GOLS FEITOS: {:.0f}".format(dados['atl-pr']['gols_feitos'])
        gols_sofridos_time1["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['atl-pr']['gols_sofridos'])
        golf_por_jogo_time1 = (dados['atl-pr']['gols_feitos'])/(dados['atl-pr']['jogos'])
        gols_feitos_jogo_time1["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time1)
        gols_por_jogo_time1 = (dados['atl-pr']['gols_sofridos'])/(dados['atl-pr']['jogos'])
        gols_sofridos_jogo_time1["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time1)
    elif time1.get() == "bah" or time1.get() == "BAH" or time1.get() == "Bahia" or time1.get() == "bahia" or time1.get() == "BAHIA":
        nome_time1["text"] = "BAHIA"
        jogos_time1["text"] = "JOGOS: {:.0f}".format(dados['bah']['jogos'])
        gols_feitos_time1["text"] = "GOLS FEITOS: {:.0f}".format(dados['bah']['gols_feitos'])
        gols_sofridos_time1["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['bah']['gols_sofridos'])
        golf_por_jogo_time1 = (dados['bah']['gols_feitos'])/(dados['bah']['jogos'])
        gols_feitos_jogo_time1["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time1)
        gols_por_jogo_time1 = (dados['bah']['gols_sofridos'])/(dados['bah']['jogos'])
        gols_sofridos_jogo_time1["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time1)
    elif time1.get() == "bgt" or time1.get() == "BGT" or time1.get() == "Bragantino" or time1.get() == "bragantino" or time1.get() == "BRAGANTINO":
        nome_time1["text"] = "BRAGANTINO"
        jogos_time1["text"] = "JOGOS: {:.0f}".format(dados['bgt']['jogos'])
        gols_feitos_time1["text"] = "GOLS FEITOS: {:.0f}".format(dados['bgt']['gols_feitos'])
        gols_sofridos_time1["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['bgt']['gols_sofridos'])
        golf_por_jogo_time1 = (dados['bgt']['gols_feitos'])/(dados['bgt']['jogos'])
        gols_feitos_jogo_time1["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time1)
        gols_por_jogo_time1 = (dados['bgt']['gols_sofridos'])/(dados['bgt']['jogos'])
        gols_sofridos_jogo_time1["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time1)
    elif time1.get() == "cea" or time1.get() == "CEA" or time1.get() == "ceara" or time1.get() == "ceará" or time1.get() == "Ceara" or time1.get() == "Ceará" or time1.get() == "CEARA" or time1.get() == "CEARÁ":
        nome_time1["text"] = "CEARÁ"
        jogos_time1["text"] = "JOGOS: {:.0f}".format(dados['cea']['jogos'])
        gols_feitos_time1["text"] = "GOLS FEITOS: {:.0f}".format(dados['cea']['gols_feitos'])
        gols_sofridos_time1["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['cea']['gols_sofridos'])
        golf_por_jogo_time1 = (dados['cea']['gols_feitos'])/(dados['cea']['jogos'])
        gols_feitos_jogo_time1["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time1)
        gols_por_jogo_time1 = (dados['cea']['gols_sofridos'])/(dados['cea']['jogos'])
        gols_sofridos_jogo_time1["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time1)
    elif time1.get() == "cor" or time1.get() == "COR" or time1.get() == "corinthians" or time1.get() == "Corinthians" or time1.get() == "CORINTHIANS":
        nome_time1["text"] = "CORINTHIANS"
        jogos_time1["text"] = "JOGOS: {:.0f}".format(dados['cor']['jogos'])
        gols_feitos_time1["text"] = "GOLS FEITOS: {:.0f}".format(dados['cor']['gols_feitos'])
        gols_sofridos_time1["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['cor']['gols_sofridos'])
        golf_por_jogo_time1 = (dados['cor']['gols_feitos'])/(dados['cor']['jogos'])
        gols_feitos_jogo_time1["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time1)
        gols_por_jogo_time1 = (dados['cor']['gols_sofridos'])/(dados['cor']['jogos'])
        gols_sofridos_jogo_time1["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time1)
    elif time1.get() == "cui" or time1.get() == "CUI"or time1.get() == "cuiaba" or time1.get() == "cuiabá" or time1.get() == "Cuiaba" or time1.get() == "Cuiabá" or time1.get() == "CUIABA" or time1.get() == "CUIABÁ":
        nome_time1["text"] = "CUIABÁ"
        jogos_time1["text"] = "JOGOS: {:.0f}".format(dados['cui']['jogos'])
        gols_feitos_time1["text"] = "GOLS FEITOS: {:.0f}".format(dados['cui']['gols_feitos'])
        gols_sofridos_time1["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['cui']['gols_sofridos'])
        golf_por_jogo_time1 = (dados['cui']['gols_feitos'])/(dados['cui']['jogos'])
        gols_feitos_jogo_time1["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time1)
        gols_por_jogo_time1 = (dados['cui']['gols_sofridos'])/(dados['cui']['jogos'])
        gols_sofridos_jogo_time1["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time1)
    elif time1.get() == "fla" or time1.get() == "FLA" or time1.get() == "flamengo" or time1.get() == "Flamengo" or time1.get() == "FLAMENGO":
        nome_time1["text"] = "FLAMENGO"
        jogos_time1["text"] = "JOGOS: {:.0f}".format(dados['fla']['jogos'])
        gols_feitos_time1["text"] = "GOLS FEITOS: {:.0f}".format(dados['fla']['gols_feitos'])
        gols_sofridos_time1["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['fla']['gols_sofridos'])
        golf_por_jogo_time1 = (dados['fla']['gols_feitos'])/(dados['fla']['jogos'])
        gols_feitos_jogo_time1["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time1)
        gols_por_jogo_time1 = (dados['fla']['gols_sofridos'])/(dados['fla']['jogos'])
        gols_sofridos_jogo_time1["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time1)
    elif time1.get() == "flu" or time1.get() == "FLU" or time1.get() == "fluminense" or time1.get() == "Fluminense" or time1.get() == "FLUMINENSE":
        nome_time1["text"] = "FLUMINENSE"
        jogos_time1["text"] = "JOGOS: {:.0f}".format(dados['flu']['jogos'])
        gols_feitos_time1["text"] = "GOLS FEITOS: {:.0f}".format(dados['flu']['gols_feitos'])
        gols_sofridos_time1["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['flu']['gols_sofridos'])
        golf_por_jogo_time1 = (dados['flu']['gols_feitos'])/(dados['flu']['jogos'])
        gols_feitos_jogo_time1["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time1)
        gols_por_jogo_time1 = (dados['flu']['gols_sofridos'])/(dados['flu']['jogos'])
        gols_sofridos_jogo_time1["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time1)
    elif time1.get() == "for" or time1.get() == "FOR" or time1.get() == "fortaleza" or time1.get() == "Fortaleza" or time1.get() == "FORTALEZA":
        nome_time1["text"] = "FORTALEZA"
        jogos_time1["text"] = "JOGOS: {:.0f}".format(dados['for']['jogos'])
        gols_feitos_time1["text"] = "GOLS FEITOS: {:.0f}".format(dados['for']['gols_feitos'])
        gols_sofridos_time1["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['for']['gols_sofridos'])
        golf_por_jogo_time1 = (dados['for']['gols_feitos'])/(dados['for']['jogos'])
        gols_feitos_jogo_time1["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time1)
        gols_por_jogo_time1 = (dados['for']['gols_sofridos'])/(dados['for']['jogos'])
        gols_sofridos_jogo_time1["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time1)
    elif time1.get() == "gre" or time1.get() == "gre" or time1.get() == "gremio" or time1.get() == "grêmio" or time1.get() == "Gremio" or time1.get() == "GREMIO" or time1.get() == "Grêmio" or time1.get() == "GRÊMIO":
        nome_time1["text"] = "GRÊMIO"
        jogos_time1["text"] = "JOGOS: {:.0f}".format(dados['gre']['jogos'])
        gols_feitos_time1["text"] = "GOLS FEITOS: {:.0f}".format(dados['gre']['gols_feitos'])
        gols_sofridos_time1["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['gre']['gols_sofridos'])
        golf_por_jogo_time1 = (dados['gre']['gols_feitos'])/(dados['gre']['jogos'])
        gols_feitos_jogo_time1["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time1)
        gols_por_jogo_time1 = (dados['gre']['gols_sofridos'])/(dados['gre']['jogos'])
        gols_sofridos_jogo_time1["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time1)
    elif time1.get() == "int" or time1.get() == "internacional" or time1.get() == "INT" or time1.get() == "Internacional" or time1.get() == "INTERNACIONAL":
        nome_time1["text"] = "INTERNACIONAL"
        jogos_time1["text"] = "JOGOS: {:.0f}".format(dados['int']['jogos'])
        gols_feitos_time1["text"] = "GOLS FEITOS: {:.0f}".format(dados['int']['gols_feitos'])
        gols_sofridos_time1["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['int']['gols_sofridos'])
        golf_por_jogo_time1 = (dados['int']['gols_feitos'])/(dados['int']['jogos'])
        gols_feitos_jogo_time1["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time1)
        gols_por_jogo_time1 = (dados['int']['gols_sofridos'])/(dados['int']['jogos'])
        gols_sofridos_jogo_time1["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time1)
    elif time1.get() == "juv" or time1.get() == "juventude" or time1.get() == "JUV" or time1.get() == "Juventude" or time1.get() == "JUVENTUDE":
        nome_time1["text"] = "JUVENTUDE"
        jogos_time1["text"] = "JOGOS: {:.0f}".format(dados['juv']['jogos'])
        gols_feitos_time1["text"] = "GOLS FEITOS: {:.0f}".format(dados['juv']['gols_feitos'])
        gols_sofridos_time1["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['juv']['gols_sofridos'])
        golf_por_jogo_time1 = (dados['juv']['gols_feitos'])/(dados['juv']['jogos'])
        gols_feitos_jogo_time1["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time1)
        gols_por_jogo_time1 = (dados['juv']['gols_sofridos'])/(dados['juv']['jogos'])
        gols_sofridos_jogo_time1["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time1)
    elif time1.get() == "pal" or time1.get() == "palmeiras" or time1.get() == "PAL" or time1.get() == "Palmeiras" or time1.get() == "PALMEIRAS":
        nome_time1["text"] = "PALMEIRAS"
        jogos_time1["text"] = "JOGOS: {:.0f}".format(dados['pal']['jogos'])
        gols_feitos_time1["text"] = "GOLS FEITOS: {:.0f}".format(dados['pal']['gols_feitos'])
        gols_sofridos_time1["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['pal']['gols_sofridos'])
        golf_por_jogo_time1 = (dados['pal']['gols_feitos'])/(dados['pal']['jogos'])
        gols_feitos_jogo_time1["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time1)
        gols_por_jogo_time1 = (dados['pal']['gols_sofridos'])/(dados['pal']['jogos'])
        gols_sofridos_jogo_time1["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time1)
    elif time1.get() == "san" or time1.get() == "santos" or time1.get() == "SAN" or time1.get() == "Santos" or time1.get() == "SANTOS":
        nome_time1["text"] = "SANTOS"
        jogos_time1["text"] = "JOGOS: {:.0f}".format(dados['san']['jogos'])
        gols_feitos_time1["text"] = "GOLS FEITOS: {:.0f}".format(dados['san']['gols_feitos'])
        gols_sofridos_time1["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['san']['gols_sofridos'])
        golf_por_jogo_time1 = (dados['san']['gols_feitos'])/(dados['san']['jogos'])
        gols_feitos_jogo_time1["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time1)
        gols_por_jogo_time1 = (dados['san']['gols_sofridos'])/(dados['san']['jogos'])
        gols_sofridos_jogo_time1["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time1)
    elif time1.get() == "sp" or time1.get() == "spfc" or time1.get() == "SP" or time1.get() == "Sao Paulo" or time1.get() == "SAO PAULO" or time1.get() == "SÃO PAULO" or time1.get() == "são paulo" or time1.get() == "São Paulo" or time1.get() == "sao paulo":
        nome_time1["text"] = "SÃO PAULO"
        jogos_time1["text"] = "JOGOS: {:.0f}".format(dados['sp']['jogos'])
        gols_feitos_time1["text"] = "GOLS FEITOS: {:.0f}".format(dados['sp']['gols_feitos'])
        gols_sofridos_time1["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['sp']['gols_sofridos'])
        golf_por_jogo_time1 = (dados['sp']['gols_feitos'])/(dados['sp']['jogos'])
        gols_feitos_jogo_time1["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time1)
        gols_por_jogo_time1 = (dados['sp']['gols_sofridos'])/(dados['sp']['jogos'])
        gols_sofridos_jogo_time1["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time1)
    elif time1.get() == "spt" or time1.get() == "sport" or time1.get() == "SPT" or time1.get() == "SPORT" or time1.get() == "Sport":
        nome_time1["text"] = "SPORT"
        jogos_time1["text"] = "JOGOS: {:.0f}".format(dados['spt']['jogos'])
        gols_feitos_time1["text"] = "GOLS FEITOS: {:.0f}".format(dados['spt']['gols_feitos'])
        gols_sofridos_time1["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['spt']['gols_sofridos'])
        golf_por_jogo_time1 = (dados['spt']['gols_feitos'])/(dados['spt']['jogos'])
        gols_feitos_jogo_time1["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time1)
        gols_por_jogo_time1 = (dados['spt']['gols_sofridos'])/(dados['spt']['jogos'])
        gols_sofridos_jogo_time1["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time1)





#CONDIÇÕES PARA O 2° TIME



def segundo_time():
    if time2.get() == "ame-mg" or time2.get() == "america mineiro" or time2.get() == "ame-mineiro" or time2.get() == "américa mineiro" or time2.get() == "américa-mg" or time2.get() == "america-mg" or time2.get() == "america-mineiro":
        nome_time2["text"] = "AMÉRICA-MG"
        jogos_time2["text"] = "JOGOS: {:.0f}".format(dados['ame']['jogos'])
        gols_feitos_time2["text"] = "GOLS FEITOS: {:.0f}".format(dados['ame']['gols_feitos'])
        gols_sofridos_time2["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['ame']['gols_sofridos'])
        golf_por_jogo_time2 = (dados['ame']['gols_feitos'])/(dados['ame']['jogos'])
        gols_feitos_jogo_time2["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time2)
        gols_por_jogo_time2 = (dados['ame']['gols_sofridos'])/(dados['ame']['jogos'])
        gols_sofridos_jogo_time2["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time2)
    elif time2.get() == "atl-mg" or time2.get() == "atletico mineiro" or time2.get() == "atl-mineiro" or time2.get() == "atlético mineiro" or time2.get() == "atlético-mg" or time2.get() == "atletico-mg" or time2.get() == "atletico mineiro":
        nome_time2["text"] = "ATLÉTICO-MG"
        jogos_time2["text"] = "JOGOS: {:.0f}".format(dados['atl-mg']['jogos'])
        gols_feitos_time2["text"] = "GOLS FEITOS: {:.0f}".format(dados['atl-mg']['gols_feitos'])
        gols_sofridos_time2["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['atl-mg']['gols_sofridos'])
        golf_por_jogo_time2 = (dados['atl-mg']['gols_feitos'])/(dados['atl-mg']['jogos'])
        gols_feitos_jogo_time2["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time2)
        gols_por_jogo_time2 = (dados['atl-mg']['gols_sofridos'])/(dados['atl-mg']['jogos'])
        gols_sofridos_jogo_time2["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time2)
    elif time2.get() == "atl-go" or time2.get() == "atletico goianiense" or time2.get() == "atlético goianiense" or time2.get() == "atlético-go" or time2.get() == "atletico-go" or time2.get() == "atletico-go":
        nome_time2["text"] = "ATLÉTICO-GO"
        jogos_time2["text"] = "JOGOS: {:.0f}".format(dados['atl-go']['jogos'])
        gols_feitos_time2["text"] = "GOLS FEITOS: {:.0f}".format(dados['atl-go']['gols_feitos'])
        gols_sofridos_time2["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['atl-go']['gols_sofridos'])
        golf_por_jogo_time2 = (dados['atl-go']['gols_feitos'])/(dados['atl-go']['jogos'])
        gols_feitos_jogo_time2["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time2)
        gols_por_jogo_time2 = (dados['atl-go']['gols_sofridos'])/(dados['atl-go']['jogos'])
        gols_sofridos_jogo_time2["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time2)
    elif time2.get() == "atl-pr" or time2.get() == "atletico paranaense" or time2.get() == "atl-paranaense" or time2.get() == "atlético paranaense" or time2.get() == "atlético-pr" or time2.get() == "atletico-pr" or time1.get() == "atletico-pr":
        nome_time2["text"] = "ATLÉTICO-PR"
        jogos_time2["text"] = "JOGOS: {:.0f}".format(dados['atl-pr']['jogos'])
        gols_feitos_time2["text"] = "GOLS FEITOS: {:.0f}".format(dados['atl-pr']['gols_feitos'])
        gols_sofridos_time2["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['atl-pr']['gols_sofridos'])
        golf_por_jogo_time2 = (dados['atl-pr']['gols_feitos'])/(dados['atl-pr']['jogos'])
        gols_feitos_jogo_time2["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time2)
        gols_por_jogo_time2 = (dados['atl-pr']['gols_sofridos'])/(dados['atl-pr']['jogos'])
        gols_sofridos_jogo_time2["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time2)
    elif time2.get() == "bah" or time1.get() == "BAH" or time2.get() == "Bahia" or time2.get() == "bahia" or time2.get() == "BAHIA":
        nome_time2["text"] = "BAHIA"
        jogos_time2["text"] = "JOGOS: {:.0f}".format(dados['bah']['jogos'])
        gols_feitos_time2["text"] = "GOLS FEITOS: {:.0f}".format(dados['bah']['gols_feitos'])
        gols_sofridos_time2["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['bah']['gols_sofridos'])
        golf_por_jogo_time2 = (dados['bah']['gols_feitos'])/(dados['bah']['jogos'])
        gols_feitos_jogo_time2["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time2)
        gols_por_jogo_time2 = (dados['bah']['gols_sofridos'])/(dados['bah']['jogos'])
        gols_sofridos_jogo_time2["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time2)
    elif time2.get() == "bgt" or time2.get() == "BGT" or time2.get() == "Bragantino" or time2.get() == "bragantino" or time2.get() == "BRAGANTINO":
        nome_time2["text"] = "BRAGANTINO"
        jogos_time2["text"] = "JOGOS: {:.0f}".format(dados['bgt']['jogos'])
        gols_feitos_time2["text"] = "GOLS FEITOS: {:.0f}".format(dados['bgt']['gols_feitos'])
        gols_sofridos_time2["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['bgt']['gols_sofridos'])
        golf_por_jogo_time2 = (dados['bgt']['gols_feitos'])/(dados['bgt']['jogos'])
        gols_feitos_jogo_time2["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time2)
        gols_por_jogo_time2 = (dados['bgt']['gols_sofridos'])/(dados['bgt']['jogos'])
        gols_sofridos_jogo_time2["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time2)
    elif time2.get() == "cea" or time2.get() == "CEA" or time2.get() == "ceara" or time2.get() == "ceará" or time2.get() == "Ceara" or time2.get() == "Ceará" or time2.get() == "CEARA" or time2.get() == "CEARÁ":
        nome_time2["text"] = "CEARÁ"
        jogos_time2["text"] = "JOGOS: {:.0f}".format(dados['cea']['jogos'])
        gols_feitos_time2["text"] = "GOLS FEITOS: {:.0f}".format(dados['cea']['gols_feitos'])
        gols_sofridos_time2["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['cea']['gols_sofridos'])
        golf_por_jogo_time2 = (dados['cea']['gols_feitos'])/(dados['cea']['jogos'])
        gols_feitos_jogo_time2["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time2)
        gols_por_jogo_time2 = (dados['cea']['gols_sofridos'])/(dados['cea']['jogos'])
        gols_sofridos_jogo_time2["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time2)
    elif time2.get() == "cor" or time2.get() == "COR" or time2.get() == "corinthians" or time2.get() == "Corinthians" or time2.get() == "CORINTHIANS":
        nome_time1["text"] = "CORINTHIANS"
        jogos_time1["text"] = "JOGOS: {:.0f}".format(dados['cor']['jogos'])
        gols_feitos_time2["text"] = "GOLS FEITOS: {:.0f}".format(dados['cor']['gols_feitos'])
        gols_sofridos_time2["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['cor']['gols_sofridos'])
        golf_por_jogo_time2 = (dados['cor']['gols_feitos'])/(dados['cor']['jogos'])
        gols_feitos_jogo_time2["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time2)
        gols_por_jogo_time2 = (dados['cor']['gols_sofridos'])/(dados['cor']['jogos'])
        gols_sofridos_jogo_time2["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time2)
    elif time2.get() == "cui" or time2.get() == "CUI"or time2.get() == "cuiaba" or time2.get() == "cuiabá" or time2.get() == "Cuiaba" or time2.get() == "Cuiabá" or time2.get() == "CUIABA" or time2.get() == "CUIABÁ":
        nome_time2["text"] = "CUIABÁ"
        jogos_time2["text"] = "JOGOS: {:.0f}".format(dados['cui']['jogos'])
        gols_feitos_time2["text"] = "GOLS FEITOS: {:.0f}".format(dados['cui']['gols_feitos'])
        gols_sofridos_time2["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['cui']['gols_sofridos'])
        golf_por_jogo_time2 = (dados['cui']['gols_feitos'])/(dados['cui']['jogos'])
        gols_feitos_jogo_time2["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time2)
        gols_por_jogo_time2 = (dados['cui']['gols_sofridos'])/(dados['cui']['jogos'])
        gols_sofridos_jogo_time2["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time2)
    elif time2.get() == "fla" or time2.get() == "FLA" or time2.get() == "flamengo" or time2.get() == "Flamengo" or time2.get() == "FLAMENGO":
        nome_time2["text"] = "FLAMENGO"
        jogos_time2["text"] = "JOGOS: {:.0f}".format(dados['fla']['jogos'])
        gols_feitos_time2["text"] = "GOLS FEITOS: {:.0f}".format(dados['fla']['gols_feitos'])
        gols_sofridos_time2["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['fla']['gols_sofridos'])
        golf_por_jogo_time2 = (dados['fla']['gols_feitos'])/(dados['fla']['jogos'])
        gols_feitos_jogo_time2["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time2)
        gols_por_jogo_time2 = (dados['fla']['gols_sofridos'])/(dados['fla']['jogos'])
        gols_sofridos_jogo_time2["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time2)
    elif time2.get() == "flu" or time2.get() == "FLU" or time2.get() == "fluminense" or time2.get() == "Fluminense" or time2.get() == "FLUMINENSE":
        nome_time2["text"] = "FLUMINENSE"
        jogos_time2["text"] = "JOGOS: {:.0f}".format(dados['flu']['jogos'])
        gols_feitos_time2["text"] = "GOLS FEITOS: {:.0f}".format(dados['flu']['gols_feitos'])
        gols_sofridos_time2["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['flu']['gols_sofridos'])
        golf_por_jogo_time2 = (dados['flu']['gols_feitos'])/(dados['flu']['jogos'])
        gols_feitos_jogo_time2["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time2)
        gols_por_jogo_time2 = (dados['flu']['gols_sofridos'])/(dados['flu']['jogos'])
        gols_sofridos_jogo_time2["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time2)
    elif time2.get() == "for" or time2.get() == "FOR" or time2.get() == "fortaleza" or time2.get() == "Fortaleza" or time2.get() == "FORTALEZA":
        nome_time2["text"] = "FORTALEZA"
        jogos_time2["text"] = "JOGOS: {:.0f}".format(dados['for']['jogos'])
        gols_feitos_time2["text"] = "GOLS FEITOS: {:.0f}".format(dados['for']['gols_feitos'])
        gols_sofridos_time2["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['for']['gols_sofridos'])
        golf_por_jogo_time2 = (dados['for']['gols_feitos'])/(dados['for']['jogos'])
        gols_feitos_jogo_time2["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time2)
        gols_por_jogo_time2 = (dados['for']['gols_sofridos'])/(dados['for']['jogos'])
        gols_sofridos_jogo_time2["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time2)
    elif time2.get() == "gre" or time2.get() == "gre" or time2.get() == "gremio" or time2.get() == "grêmio" or time2.get() == "Gremio" or time2.get() == "GREMIO" or time2.get() == "Grêmio" or time2.get() == "GRÊMIO":
        nome_time2["text"] = "GRÊMIO"
        jogos_time2["text"] = "JOGOS: {:.0f}".format(dados['gre']['jogos'])
        gols_feitos_time2["text"] = "GOLS FEITOS: {:.0f}".format(dados['gre']['gols_feitos'])
        gols_sofridos_time2["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['gre']['gols_sofridos'])
        golf_por_jogo_time2 = (dados['gre']['gols_feitos'])/(dados['gre']['jogos'])
        gols_feitos_jogo_time2["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time2)
        gols_por_jogo_time2 = (dados['gre']['gols_sofridos'])/(dados['gre']['jogos'])
        gols_sofridos_jogo_time2["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time2)
    elif time2.get() == "int" or time2.get() == "internacional" or time2.get() == "INT" or time2.get() == "Internacional" or time2.get() == "INTERNACIONAL":
        nome_time2["text"] = "INTERNACIONAL"
        jogos_time2["text"] = "JOGOS: {:.0f}".format(dados['int']['jogos'])
        gols_feitos_time2["text"] = "GOLS FEITOS: {:.0f}".format(dados['int']['gols_feitos'])
        gols_sofridos_time2["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['int']['gols_sofridos'])
        golf_por_jogo_time2 = (dados['int']['gols_feitos'])/(dados['int']['jogos'])
        gols_feitos_jogo_time2["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time2)
        gols_por_jogo_time2 = (dados['int']['gols_sofridos'])/(dados['int']['jogos'])
        gols_sofridos_jogo_time2["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time2)
    elif time2.get() == "juv" or time2.get() == "juventude" or time2.get() == "JUV" or time2.get() == "Juventude" or time2.get() == "JUVENTUDE":
        nome_time2["text"] = "JUVENTUDE"
        jogos_time2["text"] = "JOGOS: {:.0f}".format(dados['juv']['jogos'])
        gols_feitos_time2["text"] = "GOLS FEITOS: {:.0f}".format(dados['juv']['gols_feitos'])
        gols_sofridos_time2["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['juv']['gols_sofridos'])
        golf_por_jogo_time2 = (dados['juv']['gols_feitos'])/(dados['juv']['jogos'])
        gols_feitos_jogo_time2["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time2)
        gols_por_jogo_time2 = (dados['juv']['gols_sofridos'])/(dados['juv']['jogos'])
        gols_sofridos_jogo_time2["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time2)
    elif time2.get() == "pal" or time2.get() == "palmeiras" or time2.get() == "PAL" or time2.get() == "Palmeiras" or time2.get() == "PALMEIRAS":
        nome_time2["text"] = "PALMEIRAS"
        jogos_time2["text"] = "JOGOS: {:.0f}".format(dados['pal']['jogos'])
        gols_feitos_time2["text"] = "GOLS FEITOS: {:.0f}".format(dados['pal']['gols_feitos'])
        gols_sofridos_time2["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['pal']['gols_sofridos'])
        golf_por_jogo_time2= (dados['pal']['gols_feitos'])/(dados['pal']['jogos'])
        gols_feitos_jogo_time2["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time2)
        gols_por_jogo_time2 = (dados['pal']['gols_sofridos'])/(dados['pal']['jogos'])
        gols_sofridos_jogo_time2["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time2)
    elif time2.get() == "san" or time2.get() == "santos" or time2.get() == "SAN" or time2.get() == "Santos" or time2.get() == "SANTOS":
        nome_time2["text"] = "SANTOS"
        jogos_time2["text"] = "JOGOS: {:.0f}".format(dados['san']['jogos'])
        gols_feitos_time2["text"] = "GOLS FEITOS: {:.0f}".format(dados['san']['gols_feitos'])
        gols_sofridos_time2["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['san']['gols_sofridos'])
        golf_por_jogo_time2 = (dados['san']['gols_feitos'])/(dados['san']['jogos'])
        gols_feitos_jogo_time2["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time2)
        gols_por_jogo_time2 = (dados['san']['gols_sofridos'])/(dados['san']['jogos'])
        gols_sofridos_jogo_time2["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time2)
    elif time2.get() == "sp" or time2.get() == "spfc" or time2.get() == "SP" or time2.get() == "Sao Paulo" or time2.get() == "SAO PAULO" or time2.get() == "SÃO PAULO" or time2.get() == "são paulo" or time2.get() == "São Paulo" or time2.get() == "sao paulo":
        nome_time2["text"] = "SÃO PAULO"
        jogos_time2["text"] = "JOGOS: {:.0f}".format(dados['sp']['jogos'])
        gols_feitos_time2["text"] = "GOLS FEITOS: {:.0f}".format(dados['sp']['gols_feitos'])
        gols_sofridos_time2["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['sp']['gols_sofridos'])
        golf_por_jogo_time2 = (dados['sp']['gols_feitos'])/(dados['sp']['jogos'])
        gols_feitos_jogo_time2["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time2)
        gols_por_jogo_time2 = (dados['sp']['gols_sofridos'])/(dados['sp']['jogos'])
        gols_sofridos_jogo_time2["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time2)
    elif time2.get() == "spt" or time2.get() == "sport" or time2.get() == "SPT" or time2.get() == "SPORT" or time2.get() == "Sport":
        nome_time2["text"] = "SPORT"
        jogos_time2["text"] = "JOGOS: {:.0f}".format(dados['spt']['jogos'])
        gols_feitos_time2["text"] = "GOLS FEITOS: {:.0f}".format(dados['spt']['gols_feitos'])
        gols_sofridos_time2["text"] = "GOLS SOFRIDOS: {:.0f}".format(dados['spt']['gols_sofridos'])
        golf_por_jogo_time2 = (dados['spt']['gols_feitos'])/(dados['spt']['jogos'])
        gols_feitos_jogo_time2["text"] = "GOLS PRO POR JOGO: {:.2f}".format(golf_por_jogo_time2)
        gols_por_jogo_time2 = (dados['spt']['gols_sofridos'])/(dados['spt']['jogos'])
        gols_sofridos_jogo_time2["text"] = "GOLS C POR JOGO: {:.2f}".format(gols_por_jogo_time2)




janela = Tk()

time1 = StringVar()
time2 = StringVar()


janela.configure(background="#dde")
janela.geometry("500x1000")
texto = Label(janela, text="Previsão de resultados by Pedro Palugan", background="#dde")
texto.place(x = 30, y = 20)

texto_time1 = Label(janela, text="Nome do 1° time", background="#dde")
texto_time1.place(x = 30, y = 50) 

entry_time1 = Entry(janela, textvariable = time1)
entry_time1.place(x = 20, y = 80)



botao_time1 = Button(janela, text = "TIME 1 ", background= "yellow", activebackground= "white", command = primeiro_time)
botao_time1.place(x = 20, y = 105)

botao_time2 = Button(janela, text = "TIME 2 ", background= "yellow", activebackground= "white", command = segundo_time)
botao_time2.place(x = 180, y = 105)


nome_time1 = Label(janela, text = "1° Time", background = "white")
nome_time1.place(x = 20, y = 170)
nome_time1.configure(width = 20)

jogos_time1 = Label(janela, text = "N° de jogos", background = "white")
jogos_time1.place(x = 20, y = 190)
jogos_time1.configure(width = 20)

gols_feitos_time1 = Label(janela, text = "N° de GOLS FEITOS", background = "white")
gols_feitos_time1.place(x = 20, y = 210)
gols_feitos_time1.configure(width = 20)


gols_sofridos_time1 = Label(janela, text = "N° de GOLS SOFRIDOS", background = "white")
gols_sofridos_time1.place(x = 20, y = 230)
gols_sofridos_time1.configure(width = 20)

gols_feitos_jogo_time1 = Label(janela, text = "N° de GP/JOGO", background = "white")
gols_feitos_jogo_time1.place(x = 20, y = 250)
gols_feitos_jogo_time1.configure(width = 20)

gols_sofridos_jogo_time1 = Label(janela, text = "N° de GS/JOGO", background = "white")
gols_sofridos_jogo_time1.place(x = 20, y = 270)
gols_sofridos_jogo_time1.configure(width = 20)

nome_time2 = Label(janela, text = "2° Time", background = "white")
nome_time2.place(x = 180, y = 170)
nome_time2.configure(width = 20)

jogos_time2 = Label(janela, text = "N° de jogos", background = "white")
jogos_time2.place(x = 180, y = 190)
jogos_time2.configure(width = 20)

gols_feitos_time2 = Label(janela, text = "N° de GOLS FEITOS", background = "white")
gols_feitos_time2.place(x = 180, y = 210)
gols_feitos_time2.configure(width = 20)


gols_sofridos_time2 = Label(janela, text = "N° de GOLS SOFRIDOS", background = "white")
gols_sofridos_time2.place(x = 180, y = 230)
gols_sofridos_time2.configure(width = 20)

gols_feitos_jogo_time2 = Label(janela, text = "N° de GP/JOGO", background = "white")
gols_feitos_jogo_time2.place(x = 180, y = 250)
gols_feitos_jogo_time2.configure(width = 20)

gols_sofridos_jogo_time2 = Label(janela, text = "N° de GS/JOGO", background = "white")
gols_sofridos_jogo_time2.place(x = 180, y = 270)
gols_sofridos_jogo_time2.configure(width = 20)

texto_time2 = Label(janela, text="Nome do 2° time", background="#dde")
texto_time2.place(x = 180, y = 50) 

entry_time2 = Entry(janela, textvariable = time2)
entry_time2.place(x = 180, y = 80)



janela.mainloop()
