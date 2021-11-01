from tkinter import *
janela = Tk()
janela.title("Previsão de resultados by PEDRO PALUGAN")
janela.geometry ("750x1000")




txt1 = Label(janela, text= "PREVISÂO DE QUALQUER JOGO DE FUTEBOL")
janela.configure(background="#4682B4")
txt1 = Label(janela, text="PREVISÂO DE RESULTADOS", background= "#ADD8E6",)
txt1.grid(column=0, row=0, pady= 5, padx= 13)

txt900 = Label(janela, text="Gols nos últimos 15 jogos", background= "#ADD8E6")
txt900.grid(column=0, row= 1, pady= 5)

txt2 = Label(janela, text= "Nome do 1° Time", background="#ADD8E6" )
txt2.grid(column=0, row=2, pady= 5)
time1 = Entry(janela)
time1.grid(column=0, row= 3, pady= 5)

jogo1time1 = Label(janela, text= "1° Jogo", background="#ADD8E6" )
jogo1time1.grid(column=0, row=4, pady= 5)
jogo11 = Entry(janela)
jogo11.grid(column=0, row= 5, pady= 5)




cont = 1
placar_golf_time12 = 0
placar_gols_time12 = 0
placar_golf_time22 = 0
placar_gols_time22 = 0
golf_total_time12 = 0
gols_total_time12 = 0
golf_total_time22 = 0
placar_golf_time11 = 0
placar_gols_time11 = 0
placar_golf_time21 = 0
placar_gols_time21 = 0
golf_total_time11 = 0
gols_total_time11 = 0
golf_total_time21 = 0
time1 = str(input("1° Time: "))
time2 = str(input("2° Time: "))
x = int(input("Digite 1 para os últimos 15 jogos ou 2 para os últimos 10 jogos diretos: "))

while True:
    print ("Últimos 15 jogos de cada time")
    print (time1)
    golf_1_time11 = int(input("Digite a quantidade de gols no último 1° jogo: "))
    golf_2_time11 = int(input("Digite a quantidade de gols no último 2° jogo: "))
    golf_3_time11 = int(input("Digite a quantidade de gols no último 3° jogo: "))
    golf_4_time11 = int(input("Digite a quantidade de gols no último 4° jogo: "))
    golf_5_time11 = int(input("Digite a quantidade de gols no último 5° jogo: "))
    golf_6_time11 = int(input("Digite a quantidade de gols no último 6° jogo: "))
    golf_7_time11 = int(input("Digite a quantidade de gols no último 7° jogo: "))
    golf_8_time11 = int(input("Digite a quantidade de gols no último 8° jogo: "))
    golf_9_time11 = int(input("Digite a quantidade de gols no último 9° jogo: "))
    golf_10_time11 = int(input("Digite a quantidade de gols no último 10° jogo: "))
    golf_11_time11 = int(input("Digite a quantidade de gols no último 11° jogo: "))
    golf_12_time11 = int(input("Digite a quantidade de gols no último 12° jogo: "))
    golf_13_time11 = int(input("Digite a quantidade de gols no último 13° jogo: "))
    golf_14_time11 = int(input("Digite a quantidade de gols no último 14° jogo: "))
    golf_15_time11 = int(input("Digite a quantidade de gols no último 15° jogo: "))


    golf_total_time11 = golf_1_time11 + golf_2_time11 + golf_3_time11 + golf_4_time11 + golf_5_time11 + golf_6_time11 + golf_7_time11 + golf_8_time11 + golf_total_time11
    golf_total_time11 = golf_9_time11 + golf_10_time11 + golf_11_time11 + golf_12_time11 + golf_13_time11 + golf_14_time11 + golf_15_time11 + golf_total_time11



    golf_por_jogo_time11= golf_total_time11/15
    

    print ("Últimos 15 confrontos")
    print (time2)
    golf_1_time21 = int(input("Digite a quantidade de gols no último 1° jogo: "))
    golf_2_time21 = int(input("Digite a quantidade de gols no último 2° jogo: "))
    golf_3_time21 = int(input("Digite a quantidade de gols no último 3° jogo: "))
    golf_4_time21 = int(input("Digite a quantidade de gols no último 4° jogo: "))
    golf_5_time21 = int(input("Digite a quantidade de gols no último 5° jogo: "))
    golf_6_time21 = int(input("Digite a quantidade de gols no último 6° jogo: "))
    golf_7_time21 = int(input("Digite a quantidade de gols no último 7° jogo: "))
    golf_8_time21 = int(input("Digite a quantidade de gols no último 8° jogo: "))
    golf_9_time21 = int(input("Digite a quantidade de gols no último 9° jogo: "))
    golf_10_time21 = int(input("Digite a quantidade de gols no último 10° jogo: "))
    golf_11_time21 = int(input("Digite a quantidade de gols no último 11° jogo: "))
    golf_12_time21 = int(input("Digite a quantidade de gols no último 12° jogo: "))
    golf_13_time21 = int(input("Digite a quantidade de gols no último 13° jogo: "))
    golf_14_time21 = int(input("Digite a quantidade de gols no último 14° jogo: "))
    golf_15_time21 = int(input("Digite a quantidade de gols no último 15° jogo: "))


    golf_total_time21 = golf_1_time21 + golf_2_time21+ golf_3_time21 + golf_4_time21 + golf_5_time21 + golf_6_time21 + golf_7_time21 + golf_8_time21+ golf_total_time21
    golf_total_time21 = golf_9_time21 + golf_10_time21 + golf_11_time21 + golf_12_time21 + golf_13_time21 + golf_14_time21 + golf_15_time21 + golf_total_time21



    golf_por_jogo_time21 = golf_total_time21/15
    

    dif_gol_por_jogo11 = golf_por_jogo_time11 - golf_por_jogo_time21
    dif_gol_por_jogo21 = golf_por_jogo_time21 - golf_por_jogo_time11

    if golf_por_jogo_time11 > golf_por_jogo_time21:
        if round(golf_por_jogo_time11) >= 3:
            if round(dif_gol_por_jogo11) == 1:
                placar_golf_time11 = 3
                placar_gols_time21 = 2
            elif round(dif_gol_por_jogo11) == 2:
                placar_golf_time11 = 3
                placar_gols_time21 = 1
            elif round(dif_gol_por_jogo11) == 3:
                placar_golf_time11 = 3
                placar_gols_time21 = 0
            elif round(dif_gol_por_jogo11) == 0:
                placar_golf_time11 = 3
                placar_gols_time21 = 3
            elif round(dif_gol_por_jogo11) > 3:
                placar_golf_time11 = 4
                placar_gols_time21 = 0
        elif round(golf_por_jogo_time11) == 2:
            if round(dif_gol_por_jogo11) == 1:
                placar_golf_time11 = 2
                placar_gols_time21 = 1
            elif round(dif_gol_por_jogo11) == 2:
                placar_golf_time11 = 2
                placar_gols_time21 = 10
            elif round(dif_gol_por_jogo11) == 0:
                placar_golf_time11 = 2
                placar_gols_time21 = 2
        elif round(golf_por_jogo_time11) <= 1:
            if round(dif_gol_por_jogo11) == 1:
                placar_golf_time11 = 1
                placar_gols_time21 = 0
            elif round(dif_gol_por_jogo11) == 0:
                placar_golf_time11 = 1
                placar_gols_time21 = 1
    elif golf_por_jogo_time11 < golf_por_jogo_time21:
        if round(golf_por_jogo_time21) >= 3:
            if round(dif_gol_por_jogo21) == 1:
                placar_golf_time21 = 3
                placar_gols_time11 = 2
            elif round(dif_gol_por_jogo21) == 2:
                placar_golf_time21 = 3
                placar_gols_time11 = 1
            elif round(dif_gol_por_jogo21) == 3:
                placar_golf_time21 = 3
                placar_gols_time11 = 0
            elif round(dif_gol_por_jogo21) == 0:
                placar_golf_time21 = 3
                placar_gols_time11 = 3
            elif round(dif_gol_por_jogo21) > 3:
                placar_golf_time21 = 4
                placar_gols_time11 = 0
        elif round(golf_por_jogo_time21) == 2:
            if round(dif_gol_por_jogo21) == 1:
                placar_golf_time21 = 2
                placar_gols_time11 = 1
            elif round(dif_gol_por_jogo21) == 2:
                placar_golf_time21 = 2
                placar_gols_time11 = 0
            elif round(dif_gol_por_jogo21) == 0:
                placar_golf_time21 = 2
                placar_gols_time11 = 2
            elif round(dif_gol_por_jogo21) > 2:
                placar_golf_time21 = 3
                placar_gols_time11 = 0
        elif round(golf_por_jogo_time21) == 1:
            if round(dif_gol_por_jogo21) == 1:
                placar_golf_time21 = 1
                placar_gols_time11 = 0
            elif round(dif_gol_por_jogo21) > 1:
                placar_golf_time21 = 2
                placar_gols_time11 = 0
            elif round(dif_gol_por_jogo21) == 0:
                placar_golf_time21 = 1
                placar_gols_time11 = 1
    elif round(golf_por_jogo_time11) == round(golf_por_jogo_time21): 
        if round(golf_por_jogo_time11) == 4:
            placar_golf_time11 = 4
            placar_golf_time21 = 4
        if round(golf_por_jogo_time11) == 3:
            placar_golf_time11 = 3
            placar_golf_time21 = 3
        if round(golf_por_jogo_time11) == 2:
            placar_golf_time11 = 2
            placar_golf_time21 = 2
        if round(golf_por_jogo_time11) == 1:
            placar_golf_time11 = 1
            placar_golf_time21 = 1
        if round(golf_por_jogo_time11) == 0:
            placar_golf_time11 = 0
            placar_golf_time21 = 0


#segundo bloco para condições de confrontos diretos 
    print ("Últimos 10 confrontos diretos")
    print (time1)
    golf_1_time12 = int(input("Digite a quantidade de gols no último 1° jogo: "))
    golf_2_time12 = int(input("Digite a quantidade de gols no último 2° jogo: "))
    golf_3_time12 = int(input("Digite a quantidade de gols no último 3° jogo: "))
    golf_4_time12 = int(input("Digite a quantidade de gols no último 4° jogo: "))
    golf_5_time12 = int(input("Digite a quantidade de gols no último 5° jogo: "))
    golf_6_time12 = int(input("Digite a quantidade de gols no último 6° jogo: "))
    golf_7_time12 = int(input("Digite a quantidade de gols no último 7° jogo: "))
    golf_8_time12 = int(input("Digite a quantidade de gols no último 8° jogo: "))
    golf_9_time12 = int(input("Digite a quantidade de gols no último 9° jogo: "))
    golf_10_time12 = int(input("Digite a quantidade de gols no último 10° jogo: "))


    golf_total_time12 = golf_1_time12 + golf_2_time12 + golf_3_time12 + golf_4_time12 + golf_5_time12 + golf_6_time12 + golf_7_time12 + golf_8_time12 + golf_total_time12
    golf_total_time12 = golf_9_time12 + golf_10_time12 + golf_total_time12



    golf_por_jogo_time12 = golf_total_time12/10



    print ("Últimos 10 confrontos diretos")
    print(time2)
    golf_1_time22 = int(input("Digite a quantidade de gols no último 1° jogo: "))
    golf_2_time22 = int(input("Digite a quantidade de gols no último 2° jogo: "))
    golf_3_time22 = int(input("Digite a quantidade de gols no último 3° jogo: "))
    golf_4_time22 = int(input("Digite a quantidade de gols no último 4° jogo: "))
    golf_5_time22 = int(input("Digite a quantidade de gols no último 5° jogo: "))
    golf_6_time22 = int(input("Digite a quantidade de gols no último 6° jogo: "))
    golf_7_time22 = int(input("Digite a quantidade de gols no último 7° jogo: "))
    golf_8_time22 = int(input("Digite a quantidade de gols no último 8° jogo: "))
    golf_9_time22 = int(input("Digite a quantidade de gols no último 9° jogo: "))
    golf_10_time22 = int(input("Digite a quantidade de gols no último 10° jogo: "))



    golf_total_time22 = golf_1_time22 + golf_2_time22 + golf_3_time22 + golf_4_time22 + golf_5_time22 + golf_6_time22 + golf_7_time22 + golf_8_time22 + golf_total_time22
    golf_total_time22 = golf_9_time22 + golf_10_time22 + golf_total_time22



    golf_por_jogo_time22 = golf_total_time22/10

    

    dif_gol_por_jogo12 = golf_por_jogo_time12 - golf_por_jogo_time22
    dif_gol_por_jogo22 = golf_por_jogo_time22 - golf_por_jogo_time12

    if golf_por_jogo_time12 > golf_por_jogo_time22:
        if round(golf_por_jogo_time12) >= 3:
            if round(dif_gol_por_jogo12) == 1:
                placar_golf_time12 = 3
                placar_gols_time22 = 2
            elif round(dif_gol_por_jogo12) == 2:
                placar_golf_time12 = 3
                placar_gols_time22 = 1
            elif round(dif_gol_por_jogo12) == 3:
                placar_golf_time12 = 3
                placar_gols_time22 = 0
            elif round(dif_gol_por_jogo12) == 0:
                placar_golf_time12 = 3
                placar_gols_time22 = 3
            elif round(dif_gol_por_jogo12) > 3:
                placar_golf_time12 = 4
                placar_gols_time22 = 0
        elif round(golf_por_jogo_time12) == 2:
            if round(dif_gol_por_jogo12) == 1:
                placar_golf_time12 = 2
                placar_gols_time22 = 1
            elif round(dif_gol_por_jogo12) == 2:
                placar_golf_time12 = 2
                placar_gols_time22 = 10
            elif round(dif_gol_por_jogo12) == 0:
                placar_golf_time12 = 2
                placar_gols_time22 = 2
        elif round(golf_por_jogo_time12) <= 1:
            if round(dif_gol_por_jogo12) == 1:
                placar_golf_time12 = 1
                placar_gols_time22 = 0
            elif round(dif_gol_por_jogo12) == 0:
                placar_golf_time12 = 1
                placar_gols_time22 = 1
    elif golf_por_jogo_time12 < golf_por_jogo_time22:
        if round(golf_por_jogo_time22) >= 3:
            if round(dif_gol_por_jogo22) == 1:
                placar_golf_time22 = 3
                placar_gols_time12 = 2
            elif round(dif_gol_por_jogo22) == 2:
                placar_golf_time22 = 3
                placar_gols_time12 = 1
            elif round(dif_gol_por_jogo22) == 3:
                placar_golf_time22 = 3
                placar_gols_time12 = 0
            elif round(dif_gol_por_jogo22) == 0:
                placar_golf_time22 = 3
                placar_gols_time12 = 3
            elif round(dif_gol_por_jogo22) > 3:
                placar_golf_time22 = 4
                placar_gols_time12 = 0
        elif round(golf_por_jogo_time22) == 2:
            if round(dif_gol_por_jogo22) == 1:
                placar_golf_time22 = 2
                placar_gols_time12 = 1
            elif round(dif_gol_por_jogo22) == 2:
                placar_golf_time22 = 2
                placar_gols_time12 = 0
            elif round(dif_gol_por_jogo22) == 0:
                placar_golf_time22 = 2
                placar_gols_time12 = 2
            elif round(dif_gol_por_jogo22) > 2:
                placar_golf_time22 = 3
                placar_gols_time12 = 0
        elif round(golf_por_jogo_time22) == 1:
            if round(dif_gol_por_jogo22) == 1:
                placar_golf_time22 = 1
                placar_gols_time12 = 0
            elif round(dif_gol_por_jogo22) > 1:
                placar_golf_time22 = 2
                placar_gols_time12 = 0
            elif round(dif_gol_por_jogo22) == 0:
                placar_golf_time22 = 1
                placar_gols_time12 = 1
    elif round(golf_por_jogo_time12) == round(golf_por_jogo_time22): 
        if round(golf_por_jogo_time12) == 4:
            placar_golf_time12 = 4
            placar_golf_time22 = 4
        if round(golf_por_jogo_time12) == 3:
            placar_golf_time12 = 3
            placar_golf_time22 = 3
        if round(golf_por_jogo_time22) == 2:
            placar_golf_time12 = 2
            placar_golf_time22 = 2
        if round(golf_por_jogo_time12) == 1:
            placar_golf_time12 = 1
            placar_golf_time22 = 1
        if round(golf_por_jogo_time12) == 0:
            placar_golf_time12 = 0
            placar_golf_time22 = 0




    print ("Resultado por conta dos últimos 15 jogos: ")
    print ("--------------------------------------------------------------")
    if golf_por_jogo_time11 > golf_por_jogo_time21:
        print (time1, placar_golf_time11, " x ", placar_gols_time21, time2)
    elif golf_por_jogo_time11 < golf_por_jogo_time21:
        print (time1, placar_gols_time11, " x ", placar_golf_time21, time2)
    elif round(golf_por_jogo_time11) == round(golf_por_jogo_time21): 
        print (time1, placar_golf_time11, " x ", placar_golf_time21, time2)
    print ("-------------------------------------------------------------------")



    print ("Resultado por conta dos últimos 10 jogos diretos: ")
    print ("-------------------------------------------------------------------")
    if golf_por_jogo_time12 > golf_por_jogo_time22:
        print (time1, placar_golf_time12, " x ", placar_gols_time22, time2)
    elif golf_por_jogo_time12 < golf_por_jogo_time22:
        print (time1, placar_gols_time11, " x ", placar_golf_time22, time2)
    elif round(golf_por_jogo_time12) == round(golf_por_jogo_time22): 
        print (time1, placar_golf_time12, " x ", placar_golf_time22, time2)
    print ("-------------------------------------------------------------------------------")
    cont = cont + 1


    media_golf_por_jogo_time1 = (golf_por_jogo_time11 + golf_por_jogo_time12)/2
    media_golf_por_jogo_time2 = (golf_por_jogo_time21 + golf_por_jogo_time22)/2
    
    dif_media_time12 = media_golf_por_jogo_time1 - media_golf_por_jogo_time2
    dif_media_time21 = media_golf_por_jogo_time2 - media_golf_por_jogo_time1
    if media_golf_por_jogo_time1 >  media_golf_por_jogo_time2:
        if dif_media_time12 < 0.5:
            print ("--------------------------------------------------------")
            print (time1, round(media_golf_por_jogo_time1), " x ", round(media_golf_por_jogo_time2), time2)
        elif dif_media_time12 >= 0.5:
            print ("--------------------------------------------------------")
            media_golf_por_jogo_time1 = media_golf_por_jogo_time1 + 1
            print (time1, round(media_golf_por_jogo_time1), " x ", round(media_golf_por_jogo_time2), time2)
    elif media_golf_por_jogo_time2 > media_golf_por_jogo_time1:
        if dif_media_time21 >= 0.5:
            print ("---------------------------------------------------")
            media_golf_por_jogo_time2 = media_golf_por_jogo_time2 + 1
            print (time1, round(media_golf_por_jogo_time1), " x ", round(media_golf_por_jogo_time2), time2)
        elif dif_media_time21 < 0.5:
            print ("---------------------------------------------------")
            print (time1, round(media_golf_por_jogo_time1), " x ", round(media_golf_por_jogo_time2), time2)
    elif media_golf_por_jogo_time2 == media_golf_por_jogo_time1:
        print ("---------------------------------------------------")
        print (time1, round(media_golf_por_jogo_time1), " x ", round(media_golf_por_jogo_time2), time2)

        


    if cont == 10:
        break