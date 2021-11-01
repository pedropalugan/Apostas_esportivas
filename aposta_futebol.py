golf_ult15_time1 = 0
gols_ult15_time1 = 0
chance_empate = 0
chance_ganhar_time1 = 50
chance_ganhar_time2 = 50
per_vit_ult15_time1 = 0
per_der_ult15_time1 = 0
per_emp_ult15_time1 = 0
per_golf_ult15_time1 = 0
per_gols_ult15_time1 = 0
per_golfs_ult15_time1 = 0
per_golsf_ult15_time1 = 0
per_vit_cont_time1 = 0
per_der_cont_time1 = 0
per_emp_cont_time1 = 0
per_golf_cont_time1 = 0
per_gols_cont_time1 = 0
per_golfs_cont_time1 = 0
per_golsf_cont_time1 = 0
per_jogchave_time1 = 0
per_tit_time1 = 0
per_jog_casa_time1 = 0
per_emp_ult15_time2 = 0 
per_der_ult15_time2 = 0 
per_vit_ult15_time2 = 0
per_golsf_ult15_time2 = 0
per_golfs_ult15_time2 = 0 
per_gols_ult15_time2 = 0
per_golf_ult15_time2 = 0
per_golsf_cont_time2 = 0
per_golfs_cont_time2 = 0  
per_gols_cont_time2 = 0 
per_golf_cont_time2 = 0
per_tit_time2 = 0
per_jog_casa_time2 = 0
per_jogchave_time2 = 0
x = ""
while x == "":
    time1 = str(input("Qual o nome do 1° Time: "))
    time2 = str(input("Qual o nome do 2° Time: "))
    print ("BLOCO 1")
    print ("-----")
    vit_ult15_time1 = int(input("Quantas vitórias nas últimas 15: "))
    if vit_ult15_time1 >= 13 and vit_ult15_time1 <= 15:
        per_vit_ult15_time1 = 5
    elif vit_ult15_time1 >= 10 and vit_ult15_time1 <= 12:
        per_vit_ult15_time1 = 4
    elif vit_ult15_time1 >= 7 and vit_ult15_time1 <= 9:
        per_vit_ult15_time1 = 3
    elif vit_ult15_time1 >= 4 and vit_ult15_time1 <= 6:
        per_vit_ult15_time1 = 1.75
    elif vit_ult15_time1 == 2 or vit_ult15_time1 == 3:
        per_vit_ult15_time1 = -1
    elif vit_ult15_time1 == 0:
        per_vit_ult15_time1 = -1.75

    der_ult15_time1 = int(input("Quantas derrotas nas últimas 15: "))
    if der_ult15_time1 >= 13 and der_ult15_time1 <= 15:
        per_der_ult15_time1 = -5
    elif der_ult15_time1 >= 10 and der_ult15_time1 <= 12:
        per_der_ult15_time1 = -4
    elif der_ult15_time1 >= 7 and der_ult15_time1 <= 9:
        per_der_ult15_time1 = -3
    elif der_ult15_time1 >= 4 and der_ult15_time1 <= 6:
        per_der_ult15_time1 = -1.75
    elif der_ult15_time1 == 2 or der_ult15_time1 == 3:
        per_der_ult15_time1 = 1
    elif der_ult15_time1 == 0:
        per_der_ult15_time1 = 1.75


    emp_ult15_time1 = int(input("Quantas empates nas últimas 15: "))
    if emp_ult15_time1 >= 13 and emp_ult15_time1 <= 15:
        if vit_ult15_time1 > der_ult15_time1:
            per_emp_ult15_time1 = 1
        elif vit_ult15_time1 < der_ult15_time1:
            per_emp_ult15_time1 = -1
        else:
            per_emp_ult15_time1 = 0
    elif emp_ult15_time1 >= 10 and emp_ult15_time1 <= 12:
        if vit_ult15_time1 > der_ult15_time1:
            per_emp_ult15_time1 = 1.5
        elif vit_ult15_time1 < der_ult15_time1:
            per_emp_ult15_time1 = -1.5
        else:
            per_emp_ult15_time1 = 0
    elif emp_ult15_time1 >= 7 and emp_ult15_time1 <= 9:
        if vit_ult15_time1 > der_ult15_time1:
            per_emp_ult15_time1 = 2.25
        elif vit_ult15_time1 < der_ult15_time1:
            per_emp_ult15_time1 = -2.25
        else:
            per_emp_ult15_time1 = 0
    elif emp_ult15_time1 >= 4 and emp_ult15_time1 <= 6:
        if vit_ult15_time1 > der_ult15_time1:
            per_emp_ult15_time1 = 3
        elif vit_ult15_time1 < der_ult15_time1:
            per_emp_ult15_time1 = -3
        else:
            per_emp_ult15_time1 = 0
    elif emp_ult15_time1 == 2 or emp_ult15_time1 == 3:
        if vit_ult15_time1 > der_ult15_time1:
            per_emp_ult15_time1 = 4
        elif vit_ult15_time1 < der_ult15_time1:
            per_emp_ult15_time1 = -4
        else:
            per_emp_ult15_time1 = 0
    elif emp_ult15_time1 == 0:
        if vit_ult15_time1 > der_ult15_time1:
            per_emp_ult15_time1 = 5
        elif vit_ult15_time1 < der_ult15_time1:
            per_emp_ult15_time1 = -5
        else:
            per_emp_ult15_time1 = 0

    chance_ganhar_time1 = per_emp_ult15_time1 + per_der_ult15_time1 + per_vit_ult15_time1 + chance_ganhar_time1
    

    print ("Bloco 2 -> Time 1")
    golf_1_time1 = int(input("Quantos gols o time fez nos últimos 1° jogos: "))
    golf_2_time1 = int(input("Quantos gols o time fez nos últimos 2° jogos: "))
    golf_3_time1 = int(input("Quantos gols o time fez nos últimos 3° jogos: "))
    golf_4_time1 = int(input("Quantos gols o time fez nos últimos 4° jogos: "))
    golf_5_time1 = int(input("Quantos gols o time fez nos últimos 5° jogos: "))
    golf_6_time1 = int(input("Quantos gols o time fez nos últimos 6° jogos: "))
    golf_7_time1 = int(input("Quantos gols o time fez nos últimos 7° jogos: "))
    golf_8_time1 = int(input("Quantos gols o time fez nos últimos 8° jogos: "))
    golf_9_time1 = int(input("Quantos gols o time fez nos últimos 9° jogos: "))
    golf_10_time1 = int(input("Quantos gols o time fez nos últimos 10° jogos: "))
    golf_11_time1 = int(input("Quantos gols o time fez nos últimos 11° jogos: "))
    golf_12_time1 = int(input("Quantos gols o time fez nos últimos 12° jogos: "))
    golf_13_time1 = int(input("Quantos gols o time fez nos últimos 13° jogos: "))
    golf_14_time1 = int(input("Quantos gols o time fez nos últimos 14° jogos: "))
    golf_15_time1 = int(input("Quantos gols o time fez nos últimos 15° jogos: "))
    golf_ult15_time1 = golf_1_time1 + golf_2_time1 + golf_3_time1 + golf_4_time1 + golf_5_time1 + golf_6_time1 + golf_7_time1 + golf_8_time1 + golf_9_time1
    golf_ult15_time1 = golf_ult15_time1 + golf_10_time1 + golf_11_time1 + golf_12_time1 + golf_13_time1 + golf_14_time1 + golf_15_time1

    gols_1_time1 = int(input("Quantos gols o time sofreu nos últimos 1° jogos: "))
    gols_2_time1 = int(input("Quantos gols o time sofreu nos últimos 2° jogos: "))
    gols_3_time1 = int(input("Quantos gols o time sofreu nos últimos 3° jogos: "))
    gols_4_time1 = int(input("Quantos gols o time sofreu nos últimos 4° jogos: "))
    gols_5_time1 = int(input("Quantos gols o time sofreu nos últimos 5° jogos: "))
    gols_6_time1 = int(input("Quantos gols o time sofreu nos últimos 6° jogos: "))
    gols_7_time1 = int(input("Quantos gols o time sofreu nos últimos 7° jogos: "))
    gols_8_time1 = int(input("Quantos gols o time sofreu nos últimos 8° jogos: "))
    gols_9_time1 = int(input("Quantos gols o time sofreu nos últimos 9° jogos: "))
    gols_10_time1 = int(input("Quantos gols o time sofreu nos últimos 10° jogos: "))
    gols_11_time1 = int(input("Quantos gols o time sofreu nos últimos 11° jogos: "))
    gols_12_time1 = int(input("Quantos gols o time sofreu nos últimos 12° jogos: "))
    gols_13_time1 = int(input("Quantos gols o time sofreu nos últimos 13° jogos: "))
    gols_14_time1 = int(input("Quantos gols o time sofreu nos últimos 14° jogos: "))
    gols_15_time1 = int(input("Quantos gols o time sofreu nos últimos 15° jogos: "))
    gols_ult15_time1 = gols_1_time1 + gols_2_time1 + gols_3_time1 + gols_4_time1 + gols_5_time1 + gols_6_time1 + gols_7_time1 + gols_8_time1 + gols_9_time1
    gols_ult15_time1 = gols_ult15_time1 + gols_10_time1 + gols_11_time1 + gols_12_time1 + gols_13_time1 + gols_14_time1 + gols_15_time1

    if golf_ult15_time1 >= 25:
        per_golf_ult15_time1 = 5
        if golf_ult15_time1 > gols_ult15_time1:
            per_golfs_ult15_time1 = 5
        elif golf_ult15_time1 < gols_ult15_time1:
            per_golfs_ult15_time1 = -5
        else:
            per_golfs_ult15_time1 = 0
    elif golf_ult15_time1 >= 20 and golf_ult15_time1 < 25:
        per_golf_ult15_time1 = 4
        if golf_ult15_time1 > gols_ult15_time1:
            per_golfs_ult15_time1 = 4
        elif golf_ult15_time1 < gols_ult15_time1:
            per_golfs_ult15_time1 = -4
        else:
            per_golfs_ult15_time1 = 0
    elif golf_ult15_time1 >= 15 and golf_ult15_time1 < 20:
        per_golf_ult15_time1 = 3
        if golf_ult15_time1 > gols_ult15_time1:
            per_golfs_ult15_time1 = 3
        elif golf_ult15_time1 < gols_ult15_time1:
            per_golfs_ult15_time1 = -3
        else:
            per_golfs_ult15_time1 = 0
    elif golf_ult15_time1 >= 10 and golf_ult15_time1 < 15:
        per_golf_ult15_time1 = 1.5
        if golf_ult15_time1 > gols_ult15_time1:
            per_golfs_ult15_time1 = 1.5
        elif golf_ult15_time1 < gols_ult15_time1:
            per_golfs_ult15_time1 = -1.5
        else:
            per_golfs_ult15_time1 = 0
    elif golf_ult15_time1 >= 0 and golf_ult15_time1 < 10:
        per_golf_ult15_time1 = -0.75
        if golf_ult15_time1 > gols_ult15_time1:
            per_golfs_ult15_time1 = 1
        elif golf_ult15_time1 < gols_ult15_time1:
            per_golfs_ult15_time1 = -1
        else:
            per_golfs_ult15_time1 = 0


    if gols_ult15_time1 >= 25:
        per_gols_ult15_time1 = -5
        if gols_ult15_time1 > golf_ult15_time1:
            per_golsf_ult15_time1 = -5
        elif golf_ult15_time1 > gols_ult15_time1:
            per_golsf_ult15_time1 = 5
        else:
            per_golsf_ult15_time1 = 0
    elif gols_ult15_time1 >= 20 and gols_ult15_time1 < 25:
        per_gols_ult15_time1 = -4
        if gols_ult15_time1 > golf_ult15_time1:
            per_golsf_ult15_time1 = -4
        elif golf_ult15_time1 > gols_ult15_time1:
            per_golsf_ult15_time1 = 4
        else:
            per_golsf_ult15_time1 = 0
    elif gols_ult15_time1 >= 15 and gols_ult15_time1 < 20:
        per_gols_ult15_time1 = -3
        if gols_ult15_time1 > golf_ult15_time1:
            per_golsf_ult15_time1 = -3
        elif golf_ult15_time1 > gols_ult15_time1:
            per_golsf_ult15_time1 = 3
        else:
            per_golsf_ult15_time1 = 0
    elif gols_ult15_time1 >= 10 and gols_ult15_time1 < 15:
        per_gols_ult15_time1 = -1.5
        if gols_ult15_time1 > golf_ult15_time1:
            per_golsf_ult15_time1 = -1.5
        elif golf_ult15_time1 > gols_ult15_time1:
            per_golsf_ult15_time1 = 1.5
        else:
            per_golsf_ult15_time1 = 0
    elif gols_ult15_time1 >= 0 and gols_ult15_time1 < 10:
        per_gols_ult15_time1 = 0.75
        if gols_ult15_time1 > golf_ult15_time1:
            per_golsf_ult15_time1 = -1
        elif golf_ult15_time1 > gols_ult15_time1:
            per_golsf_ult15_time1 = 1
        else:
            per_golsf_ult15_time1 = 0


    chance_ganhar_time1 = per_golsf_ult15_time1 + per_golf_ult15_time1 + per_golfs_ult15_time1 + per_gols_ult15_time1 + chance_ganhar_time1

    print ("Bloco 2 -> Time 1")
    vit_cont_time1 = int(input("Quantas vitórias o time 1 teve contra o time 2 nos últimos 5 confrontos: "))
    if vit_cont_time1 == 4 or vit_cont_time1 == 5:
        per_vit_cont_time1 = 6
    elif vit_cont_time1 == 3:
        per_vit_ult15_time1 = 4
    elif vit_cont_time1 == 2:
        per_vit_ult15_time1 = 2.25
    elif vit_cont_time1 == 1:  
        per_vit_ult15_time1 = 1
    elif vit_cont_time1 == 0:
        per_vit_ult15_time1 = -1.5

    der_cont_time1 = int(input("Quantas derrotas o time 1 teve contra o time 2 nos últimos 5 confrontos: "))
    if der_cont_time1 == 4 or der_cont_time1 == 5:
        per_der_cont_time1 = -6
    elif der_cont_time1 == 3 :
        per_der_cont_time1 = -4
    elif der_cont_time1 == 2:
        per_der_cont_time1 = -2.25
    elif der_cont_time1 == 1:
        per_der_cont_time1 = -1
    elif der_cont_time1 == 0:
        per_der_cont_time1 = 1.5

    emp_cont_time1 = int(input("Quantas empates o time 1 teve contra o time 2 nos últimos 5 confrontos: "))
    if emp_cont_time1 == 4 or emp_ult15_time1 == 5:
        if vit_cont_time1 > der_cont_time1:
            per_emp_cont_time1 = 1
        elif vit_cont_time1 < der_cont_time1:
            per_emp_cont_time1 = -1
        else: 
            per_emp_cont_time1 = 0
    elif emp_cont_time1 == 3:
        if vit_cont_time1 > der_cont_time1:
            per_emp_cont_time1 = 2
        elif vit_cont_time1 < der_cont_time1:
            per_emp_cont_time1 = -2
        else: 
            per_emp_cont_time1 = 0
    elif emp_cont_time1 == 2:
        if vit_cont_time1 > der_cont_time1:
            per_emp_cont_time1 = 3
        elif vit_cont_time1 < der_cont_time1:
            per_emp_cont_time1 = -3
        else: 
            per_emp_cont_time1 = 0
    elif emp_cont_time1 == 1:
        if vit_cont_time1 > der_cont_time1:
            per_emp_cont_time1 = 5
        elif vit_cont_time1 < der_cont_time1:
            per_emp_cont_time1 = -5
        else: 
            per_emp_cont_time1 = 0
    elif emp_cont_time1 == 0:
        if vit_cont_time1 > der_cont_time1:
            per_emp_cont_time1 = 6
        elif vit_cont_time1 < der_cont_time1:
            per_emp_cont_time1 = -6
        else: 
            per_emp_cont_time1 = 0

    chance_ganhar_time1 = vit_cont_time1 + der_cont_time1 + emp_cont_time1 + chance_ganhar_time1

    golf_cont1_time1 = int(input("Quantos gols o time 1 fez nos últimos 1° confrontos diretos: "))
    golf_cont2_time1 = int(input("Quantos gols o time 1 fez nos últimos 2° confrontos diretos: "))
    golf_cont3_time1 = int(input("Quantos gols o time 1 fez nos últimos 3° confrontos diretos: "))
    golf_cont4_time1 = int(input("Quantos gols o time 1 fez nos últimos 4° confrontos diretos: "))
    golf_cont5_time1 = int(input("Quantos gols o time 1 fez nos últimos 5° confrontos diretos: "))
    golf_cont_time1 = golf_cont1_time1 + golf_cont2_time1 + golf_cont3_time1 + golf_cont4_time1 + golf_cont5_time1 

    gols_cont1_time1 = int(input("Quantos gols o time 1 sofreu nos últimos 1° confrontos diretos: "))
    gols_cont2_time1 = int(input("Quantos gols o time 1 sofreu nos últimos 2° confrontos diretos: "))
    gols_cont3_time1 = int(input("Quantos gols o time 1 sofreu nos últimos 3° confrontos diretos: "))
    gols_cont4_time1 = int(input("Quantos gols o time 1 sofreu nos últimos 4° confrontos diretos: "))
    gols_cont5_time1 = int(input("Quantos gols o time 1 sofreu nos últimos 5° confrontos diretos: "))
    gols_cont_time1 = gols_cont1_time1 + gols_cont2_time1 + gols_cont3_time1 + gols_cont4_time1 + gols_cont5_time1 

    if golf_cont_time1 >= 8:
        per_golf_cont_time1 = 4
        if golf_cont_time1 > gols_cont_time1:
            per_golfs_cont_time1 = 4
        elif gols_cont_time1 > golf_cont_time1:
            per_golfs_cont_time1 = -4
        else: 
            per_golfs_cont_time1 = 0
    elif golf_cont_time1 >= 5 and golf_cont_time1 < 8:
        per_golf_cont_time1 = 2.75
        if golf_cont_time1 > gols_cont_time1:
            per_golfs_cont_time1 = 2.75
        elif gols_cont_time1 > golf_cont_time1:
            per_golfs_cont_time1 = -2.75
        else: 
            per_golfs_cont_time1 = 0
    elif golf_cont_time1 >= 3 and golf_cont_time1 < 5:
        per_golf_cont_time1 = 2
        if golf_cont_time1 > gols_cont_time1:
            per_golfs_cont_time1 = 2
        elif gols_cont_time1 > golf_cont_time1:
            per_golfs_cont_time1 = -2
        else: 
            per_golfs_cont_time1 = 0
    elif golf_cont_time1 == 2:
        per_golf_cont_time1 = 1
        if golf_cont_time1 > gols_cont_time1:
            per_golfs_cont_time1 = 1
        elif gols_cont_time1 > golf_cont_time1:
            per_golfs_cont_time1 = -1
        else: 
            per_golfs_cont_time1 = 0
    elif golf_cont_time1 < 2:
        per_golf_cont_time1 = -1  
        if golf_cont_time1 > gols_cont_time1:
            per_golfs_cont_time1 = 1
        elif gols_cont_time1 > golf_cont_time1:
            per_golfs_cont_time1 = -1
        else: 
            per_golfs_cont_time1 = 0


    if gols_cont_time1 >= 8:
        per_gols_cont_time1 = -4
        if gols_cont_time1 > golf_cont_time1:
            per_golsf_cont_time1 = -4
        elif golf_cont_time1 > gols_cont_time1:
            per_golsf_cont_time1 = 4
        else: 
            per_golsf_cont_time1 = 0
    elif gols_cont_time1 >= 5 and gols_cont_time1 < 8:
        per_gols_cont_time1 = -2.75
        if gols_cont_time1 > golf_cont_time1:
            per_golsf_cont_time1 = -2.75
        elif golf_cont_time1 > gols_cont_time1:
            per_golsf_cont_time1 = 2.75
        else: 
            per_golsf_cont_time1 = 0
    elif gols_cont_time1 >= 3 and gols_cont_time1 < 5:
        per_gols_cont_time1 = -2
        if gols_cont_time1 > golf_cont_time1:
            per_golsf_cont_time1 = -2
        elif golf_cont_time1 > gols_cont_time1:
            per_golsf_cont_time1 = 2
        else: 
            per_golsf_cont_time1 = 0
    elif gols_cont_time1 == 2:
        per_gols_cont_time1 = -1
        if gols_cont_time1 > golf_cont_time1:
            per_golsf_cont_time1 = -1
        elif golf_cont_time1 > gols_cont_time1:
            per_golsf_cont_time1 = 1
        else: 
            per_golsf_cont_time1 = 0
    elif gols_cont_time1 < 2:
        per_gols_cont_time1 = 1
        if gols_cont_time1 > golf_cont_time1:
            per_golsf_cont_time1 = -1
        elif golf_cont_time1 > gols_cont_time1:
            per_golsf_cont_time1 = 1
        else: 
            per_golsf_cont_time1 = 0



    chance_ganhar_time1 = per_golsf_cont_time1 + per_golfs_cont_time1 + per_gols_cont_time1 + per_golf_cont_time1 + chance_ganhar_time1


    print ("Bloco 3 -> Time 1")
    jog_casa_time1 = str(input("Joga em casa [s/n]: "))
    if jog_casa_time1 == "s" or jog_casa_time1 == "S":
        per_jog_casa_time1 = 5
    elif jog_casa_time1 == "n" or jog_casa_time1 == "N":
        per_jog_casa_time1 = -5


    titulares_time1 = int(input("Quantos titulares o time 1 vai jogar: "))
    if titulares_time1 >= 8:
        per_tit_time1 = 2.5
    elif titulares_time1 >= 5 and titulares_time1 < 8:
        per_tit_time1 = 1.25
    elif titulares_time1 < 5:
        per_tit_time1 = 0.75


    jog_chave_time1 = int(input("Quantos jogadores chaves o time 1 vai jogar: "))
    if jog_chave_time1 >= 6:
        per_jogchave_time1 = 2.5
    elif jog_chave_time1 < 6 and jog_chave_time1 >= 4:
        per_jogchave_time1 = 1.25
    elif jog_chave_time1 < 4:
        per_jogchave_time1 = 0.75

    chance_ganhar_time1 = per_jogchave_time1 + per_tit_time1 + per_jog_casa_time1 + chance_ganhar_time1 


#condições para o time 2
    print ("------------")
    print ("Bloco 1 -> Time 2")
    vit_ult15_time2 = int(input("Quantas vitórias o time 2 teve nas últimas 15 partidas: "))
    if vit_ult15_time2 >= 13 and vit_ult15_time2 <= 15:
        per_vit_ult15_time2 = 5
    elif vit_ult15_time2 >= 10 and vit_ult15_time2 <= 12:
        per_vit_ult15_time2 = 4
    elif vit_ult15_time2 >= 7 and vit_ult15_time2 <= 9:
        per_vit_ult15_time2 = 3
    elif vit_ult15_time2 >= 4 and vit_ult15_time2 <= 6:
        per_vit_ult15_time2 = 1.75
    elif vit_ult15_time2 == 3 or vit_ult15_time2 == 2:
        per_vit_ult15_time2 = -1
    elif vit_ult15_time2 == 0:
        per_vit_ult15_time2 = -1.75


    der_ult15_time2 = int(input("Quantas derrotas o time 2 teve nas últimas 15 partidas: "))
    if der_ult15_time2 >= 13 and der_ult15_time2 <= 15:
        per_der_ult15_time2 = -5
    elif der_ult15_time2 >= 10 and der_ult15_time2 <= 12:
        per_der_ult15_time2 = -4
    elif der_ult15_time2 >= 7 and der_ult15_time2 <= 9:
        per_der_ult15_time2 = -3
    elif der_ult15_time2 >= 4 and der_ult15_time2 <= 6:
        per_der_ult15_time2 = -1.75
    elif der_ult15_time2 == 2 and der_ult15_time2 == 3:
        per_der_ult15_time2 = 1
    elif der_ult15_time2 == 0: 
        per_der_ult15_time2 = 1.75


    emp_ult15_time2 = int(input("Quantos empates o time 2 teve nas últimas 15 partidas: "))
    if emp_ult15_time2 >= 13 and emp_ult15_time2 <= 15:
        if vit_ult15_time2 > der_ult15_time2:
            per_emp_ult15_time2 = 1
        elif vit_ult15_time2 < der_ult15_time2:
            per_emp_ult15_time2 = -1
        else:
            per_emp_ult15_time2 = 0
    elif emp_ult15_time2 >= 10 and emp_ult15_time2 <= 12:
        if vit_ult15_time2 > der_ult15_time2:
            per_emp_ult15_time2 = 1.5
        elif vit_ult15_time2 < der_ult15_time2:
            per_emp_ult15_time2 = -1.5
        else:
            per_emp_ult15_time2 = 0
    elif emp_ult15_time2 >= 7 and emp_ult15_time2 <= 9:
        if vit_ult15_time2 > der_ult15_time2:
            per_emp_ult15_time2 = 2.25
        elif vit_ult15_time2 < der_ult15_time2:
            per_emp_ult15_time2 = -2.25
        else:
            per_emp_ult15_time2 = 0
    elif emp_ult15_time2 >= 4 and emp_ult15_time2 <= 6:
        if vit_ult15_time2 > der_ult15_time2:
            per_emp_ult15_time2 = 3
        elif vit_ult15_time2 < der_ult15_time2:
            per_emp_ult15_time2 = -3
        else:
            per_emp_ult15_time2 = 0
    elif emp_ult15_time2 == 3 and emp_ult15_time2 == 2:
        if vit_ult15_time2 > der_ult15_time2:
            per_emp_ult15_time2 = 4
        elif vit_ult15_time2 < der_ult15_time2:
            per_emp_ult15_time2 = -4
        else:
            per_emp_ult15_time2 = 0
    elif emp_ult15_time2 == 0:
        if vit_ult15_time2 > der_ult15_time2:
            per_emp_ult15_time2 = 5
        elif vit_ult15_time2 < der_ult15_time2:
            per_emp_ult15_time2 = -5
        else:
            per_emp_ult15_time2 = 0




    chance_ganhar_time2 = per_emp_ult15_time2 + per_der_ult15_time2 + per_vit_ult15_time2 + chance_ganhar_time2


    print ("Bloco 2 -> Time 2")

 
    golf_1_time2 = int(input("Quantos gols o time fez nos últimos 1° jogos: "))
    golf_2_time2 = int(input("Quantos gols o time fez nos últimos 2° jogos: "))
    golf_3_time2 = int(input("Quantos gols o time fez nos últimos 3° jogos: "))
    golf_4_time2 = int(input("Quantos gols o time fez nos últimos 4° jogos: "))
    golf_5_time2 = int(input("Quantos gols o time fez nos últimos 5° jogos: "))
    golf_6_time2 = int(input("Quantos gols o time fez nos últimos 6° jogos: "))
    golf_7_time2 = int(input("Quantos gols o time fez nos últimos 7° jogos: "))
    golf_8_time2 = int(input("Quantos gols o time fez nos últimos 8° jogos: "))
    golf_9_time2 = int(input("Quantos gols o time fez nos últimos 9° jogos: "))
    golf_10_time2 = int(input("Quantos gols o time fez nos últimos 10° jogos: "))
    golf_11_time2 = int(input("Quantos gols o time fez nos últimos 11° jogos: "))
    golf_12_time2 = int(input("Quantos gols o time fez nos últimos 12° jogos: "))
    golf_13_time2 = int(input("Quantos gols o time fez nos últimos 13° jogos: "))
    golf_14_time2 = int(input("Quantos gols o time fez nos últimos 14° jogos: "))
    golf_15_time2 = int(input("Quantos gols o time fez nos últimos 15° jogos: "))
    golf_ult15_time2 = golf_1_time2 + golf_2_time2 + golf_3_time2 + golf_4_time2 + golf_5_time2 + golf_6_time2 + golf_7_time2 + golf_8_time2 + golf_9_time2
    golf_ult15_time2 = golf_ult15_time2 + golf_10_time2 + golf_11_time2 + golf_12_time2 + golf_13_time2 + golf_14_time2 + golf_15_time2

    gols_1_time2 = int(input("Quantos gols o time sofreu nos últimos 1° jogos: "))
    gols_2_time2 = int(input("Quantos gols o time sofreu nos últimos 2° jogos: "))
    gols_3_time2 = int(input("Quantos gols o time sofreu nos últimos 3° jogos: "))
    gols_4_time2 = int(input("Quantos gols o time sofreu nos últimos 4° jogos: "))
    gols_5_time2 = int(input("Quantos gols o time sofreu nos últimos 5° jogos: "))
    gols_6_time2 = int(input("Quantos gols o time sofreu nos últimos 6° jogos: "))
    gols_7_time2 = int(input("Quantos gols o time sofreu nos últimos 7° jogos: "))
    gols_8_time2 = int(input("Quantos gols o time sofreu nos últimos 8° jogos: "))
    gols_9_time2 = int(input("Quantos gols o time sofreu nos últimos 9° jogos: "))
    gols_10_time2 = int(input("Quantos gols o time sofreu nos últimos 10° jogos: "))
    gols_11_time2 = int(input("Quantos gols o time sofreu nos últimos 11° jogos: "))
    gols_12_time2 = int(input("Quantos gols o time sofreu nos últimos 12° jogos: "))
    gols_13_time2 = int(input("Quantos gols o time sofreu nos últimos 13° jogos: "))
    gols_14_time2 = int(input("Quantos gols o time sofreu nos últimos 14° jogos: "))
    gols_15_time2 = int(input("Quantos gols o time sofreu nos últimos 15° jogos: "))
    gols_ult15_time2 = gols_1_time2 + gols_2_time2 + gols_3_time2 + gols_4_time2 + gols_5_time2 + gols_6_time2 + gols_7_time2 + gols_8_time2 + gols_9_time2
    gols_ult15_time2 = gols_ult15_time2 + gols_10_time2 + gols_11_time2 + gols_12_time2 + gols_13_time2 + gols_14_time2 + gols_15_time2


    if golf_ult15_time2 >= 25:
        per_golf_ult15_time2 = 5
        if golf_ult15_time2 > gols_ult15_time2:
            per_golfs_ult15_time2 = 5
        elif gols_ult15_time2 < gols_ult15_time2:
            per_golfs_ult15_time2 = -5
        else:
            per_golfs_ult15_time2 = 0
    elif golf_ult15_time2 >= 20 and golf_ult15_time2 < 25:
        per_golf_ult15_time2 = 4
        if golf_ult15_time2 > gols_ult15_time2:
            per_golfs_ult15_time2 = 4
        elif gols_ult15_time2 < gols_ult15_time2:
            per_golfs_ult15_time2 = -4
            per_golfs_ult15_time2 = 0
    elif golf_ult15_time2 >= 15 and golf_ult15_time2 < 20:
        per_golf_ult15_time2 = 3
        if golf_ult15_time2 > gols_ult15_time2:
            per_golfs_ult15_time2 = 3
        elif gols_ult15_time2 < gols_ult15_time2:
            per_golfs_ult15_time2 = -3
        else:
            per_golfs_ult15_time2 = 0
    elif golf_ult15_time2 >= 10 and golf_ult15_time2 < 15:
        per_golf_ult15_time2 = 1.5
        if golf_ult15_time2 > gols_ult15_time2:
            per_golfs_ult15_time2 = 1.5
        elif gols_ult15_time2 < gols_ult15_time2:
            per_golfs_ult15_time2 = -1.5
        else:
            per_golfs_ult15_time2 = 0
    elif golf_ult15_time2 >= 0 and golf_ult15_time2 < 10:
        per_golf_ult15_time2 = -0.75
        if golf_ult15_time2 > gols_ult15_time2:
            per_golfs_ult15_time2 = 1
        elif gols_ult15_time2 < gols_ult15_time2:
            per_golfs_ult15_time2 = -1
        else:
            per_golfs_ult15_time2 = 0
    



    if gols_ult15_time2 >= 25:
        per_gols_ult15_time2 = -5
        if gols_ult15_time2 > golf_ult15_time2:
            per_golsf_ult15_time2 = -5
        elif gols_ult15_time2 < golf_ult15_time2:
            per_golsf_ult15_time2 = 5
        else: 
            per_golsf_ult15_time2 = 0
    elif gols_ult15_time2 >= 20 and gols_ult15_time2 < 25:
        per_gols_ult15_time2 = -4
        if gols_ult15_time2 > golf_ult15_time2:
            per_golsf_ult15_time2 = -4
        elif gols_ult15_time2 < golf_ult15_time2:
            per_golsf_ult15_time2 = 4
        else: 
            per_golsf_ult15_time2 = 0
    elif gols_ult15_time2 >= 15 and gols_ult15_time2 < 20:
        per_gols_ult15_time2 = -3
        if gols_ult15_time2 > golf_ult15_time2:
            per_golsf_ult15_time2 = -3
        elif gols_ult15_time2 < golf_ult15_time2:
            per_golsf_ult15_time2 = 3
        else: 
            per_golsf_ult15_time2 = 0
    elif gols_ult15_time2 >= 10 and gols_ult15_time2 < 15:
        per_gols_ult15_time2 = -1.5
        if gols_ult15_time2 > golf_ult15_time2:
            per_golsf_ult15_time2 = -1.5
        elif gols_ult15_time2 < golf_ult15_time2:
            per_golsf_ult15_time2 = 1.5
        else: 
            per_golsf_ult15_time2 = 0
    elif gols_ult15_time2 >= 0 and gols_ult15_time2 < 10:
        per_gols_ult15_time2 = 0.75
        if gols_ult15_time2 > golf_ult15_time2:
            per_golsf_ult15_time2 = -1
        elif gols_ult15_time2 < golf_ult15_time2:
            per_golsf_ult15_time2 = 1
        else: 
            per_golsf_ult15_time2 = 0



    chance_ganhar_time2 = per_golsf_ult15_time2 + per_golfs_ult15_time2 + per_gols_ult15_time2 + per_golf_ult15_time2 + chance_ganhar_time2


    print ("Bloco 2 -> Time 1")
    vit_cont_time2 = int(input("Quantas vitórias o time 2 teve nos últimos 5 confrontos diretos: "))
    if vit_cont_time2== 4 or vit_cont_time2 == 5:
        per_vit_cont_time2 = 6
    elif vit_cont_time2 == 3:
        per_vit_cont_time2 = 4
    elif vit_cont_time2 == 2:
        per_vit_cont_time2 = 2.25
    elif vit_cont_time2 == 1:
        per_vit_cont_time2 = 1
    elif vit_cont_time2 == 0:
        per_vit_cont_time2 = -1.5



    der_cont_time2 = int(input("Quantas derrotas o time 2 teve nos últimos 5 confrontos diretos: "))
    if der_cont_time2 == 4 or der_cont_time1 == 5:
        per_der_cont_time2 = -6
    elif der_cont_time2 == 3 :
        per_der_cont_time2 = -4
    elif der_cont_time2 == 2:
        per_der_cont_time2 = -2.25
    elif der_cont_time2 == 1:
        per_der_cont_time2 = -1
    elif der_cont_time2 == 0:
        per_der_cont_time2 = 1.5


    emp_cont_time2 = int(input("Quantos empates o time 2 teve nos últimos 5 confrontos diretos: "))
    if emp_cont_time2 == 4 or emp_cont_time2 == 5:
        if vit_cont_time2 > der_cont_time2:
            per_emp_cont_time2 = 1
        elif der_cont_time2 > vit_cont_time2:
            per_emp_cont_time2 = -1
        else:
            per_emp_cont_time2 = 0
    elif emp_cont_time2 == 3:
        if vit_cont_time2 > der_cont_time2:
            per_emp_cont_time2 = 2
        elif der_cont_time2 > vit_cont_time2:
            per_emp_cont_time2 = -2
        else:
            per_emp_cont_time2 = 0
    elif emp_cont_time2 == 2:
        if vit_cont_time2 > der_cont_time2:
            per_emp_cont_time2 = 3
        elif der_cont_time2 > vit_cont_time2:
            per_emp_cont_time2 = -3
        else:
            per_emp_cont_time2 = 0
    elif emp_cont_time2 == 1:
        if vit_cont_time2 > der_cont_time2:
            per_emp_cont_time2 = 5
        elif der_cont_time2 > vit_cont_time2:
            per_emp_cont_time2 = -5
        else:
            per_emp_cont_time2 = 0
    elif emp_cont_time2 == 0:
        if vit_cont_time2 > der_cont_time2:
            per_emp_cont_time2 = 6
        elif der_cont_time2 > vit_cont_time2:
            per_emp_cont_time2 = -6
        else:
            per_emp_cont_time2 = 0

    chance_ganhar_time2 = vit_cont_time2 + der_cont_time2 + emp_cont_time2 + chance_ganhar_time2


    golf_cont1_time2 = int(input("Quantos gols o time 2 fez nos últimos 1° confrontos diretos: "))
    golf_cont2_time2 = int(input("Quantos gols o time 2 fez nos últimos 2° confrontos diretos: "))
    golf_cont3_time2 = int(input("Quantos gols o time 2 fez nos últimos 3° confrontos diretos: "))
    golf_cont4_time2 = int(input("Quantos gols o time 2 fez nos últimos 4° confrontos diretos: "))
    golf_cont5_time2 = int(input("Quantos gols o time 2 fez nos últimos 5° confrontos diretos: "))
    golf_cont_time2 = golf_cont1_time2 + golf_cont2_time2 + golf_cont3_time2 + golf_cont4_time2 + golf_cont5_time2 

    gols_cont1_time2 = int(input("Quantos gols o time 2 sofreu nos últimos 1° confrontos diretos: "))
    gols_cont2_time2 = int(input("Quantos gols o time 2 sofreu nos últimos 2° confrontos diretos: "))
    gols_cont3_time2 = int(input("Quantos gols o time 2 sofreu nos últimos 3° confrontos diretos: "))
    gols_cont4_time2 = int(input("Quantos gols o time 2 sofreu nos últimos 4° confrontos diretos: "))
    gols_cont5_time2 = int(input("Quantos gols o time 2 sofreu nos últimos 5° confrontos diretos: "))
    gols_cont_time2 = gols_cont1_time2 + gols_cont2_time2 + gols_cont3_time2 + gols_cont4_time2 + gols_cont5_time2 

    if golf_cont_time2 >= 8:
        per_golf_cont_time2 = 4
        if golf_cont_time2 > gols_cont_time2:
            per_golfs_cont_time2 = 4
        elif golf_cont_time2 < gols_cont_time2:
            per_golfs_cont_time2 = -4
        else:
            per_golfs_cont_time2 = 0
    elif golf_cont_time2 >= 5 and golf_cont_time2 < 8:
        per_golf_cont_time2 = 2.75
        if golf_cont_time2 > gols_cont_time2:
            per_golfs_cont_time2 = 2.75
        elif golf_cont_time2 < gols_cont_time2:
            per_golfs_cont_time2 = -2.75
        else:
            per_golfs_cont_time2 = 0
    elif golf_cont_time2 >= 3 and golf_cont_time2 < 5:
        per_golf_cont_time2 = 2
        if golf_cont_time2 > gols_cont_time2:
            per_golfs_cont_time2 = 2
        elif golf_cont_time2 < gols_cont_time2:
            per_golfs_cont_time2 = -2
        else:
            per_golfs_cont_time2 = 0
    elif golf_cont_time2 == 2:
        per_golf_cont_time2 = 1
        if golf_cont_time2 > gols_cont_time2:
            per_golfs_cont_time2 = 1
        elif golf_cont_time2 < gols_cont_time2:
            per_golfs_cont_time2 = -1
        else:
            per_golfs_cont_time2 = 0
    elif golf_cont_time2 < 2:
        per_golf_cont_time2 = -1
        if golf_cont_time2 > gols_cont_time2:
            per_golfs_cont_time2 = 1
        elif golf_cont_time2 < gols_cont_time2:
            per_golfs_cont_time2 = -1
        else:
            per_golfs_cont_time2 = 0
    


    if gols_cont_time2 >= 8:
        per_gols_cont_time2 = -4
        if gols_cont_time2 > golf_cont_time2:
            per_golsf_cont_time2 = -4
        elif golf_cont_time2 > gols_cont_time2:
            per_golsf_cont_time2 = 4
        else:
            per_golsf_cont_time2 = 0
    elif gols_cont_time2 >= 5 and gols_cont_time2 < 8:
        per_gols_cont_time1 = -2.75
        if gols_cont_time2 > golf_cont_time2:
            per_golsf_cont_time2 = -2.75
        elif golf_cont_time2 > gols_cont_time2:
            per_golsf_cont_time2 = 2.75
        else:
            per_golsf_cont_time2 = 0
    elif gols_cont_time2 >= 3 and gols_cont_time2 < 5:
        per_gols_cont_time1 = -2
        if gols_cont_time2 > golf_cont_time2:
            per_golsf_cont_time2 = -2
        elif golf_cont_time2 > gols_cont_time2:
            per_golsf_cont_time2 = 2
        else:
            per_golsf_cont_time2 = 0
    elif gols_cont_time2 == 2:
        per_gols_cont_time1 = -1
        if gols_cont_time2 > golf_cont_time2:
            per_golsf_cont_time2 = -1
        elif golf_cont_time2 > gols_cont_time2:
            per_golsf_cont_time2 = 1
        else:
            per_golsf_cont_time2 = 0
    elif gols_cont_time2 < 2:
        per_gols_cont_time1 = 1
        if gols_cont_time2 > golf_cont_time2:
            per_golsf_cont_time2 = -1
        elif golf_cont_time2 > gols_cont_time2:
            per_golsf_cont_time2 = 1
        else:
            per_golsf_cont_time2 = 0


    chance_ganhar_time2 = per_golsf_cont_time2 + per_golfs_cont_time2 + per_gols_cont_time2 + per_golf_cont_time2 + chance_ganhar_time2




    print ('Bloco 3 -> Time 2')
    jog_casa_time2 = str(input("Joga em casa [s/n]: "))
    if jog_casa_time2 == "s" or jog_casa_time2 == "S":
        per_jog_casa_time2 = 5
    elif jog_casa_time2 == "n" or jog_casa_time2 == "N":
        per_jog_casa_time2 = -5


    titulares_time2 = int(input("Quantos titulares o time 2 vai jogar: "))
    if titulares_time2 >= 8:
        per_tit_time2 = 2.5
    elif titulares_time2 >= 5 and titulares_time2 < 8:
        per_tit_time2 = 1.25
    elif titulares_time2 < 5:
        per_tit_time2 - 0.75



    jog_chave_time2 = int(input("Quantos jogadores chave vão jogar: "))
    if jog_chave_time2 >= 6:
        per_jogchave_time2 = 2.5
    elif jog_chave_time2 < 6 and jog_chave_time2 >= 4:
        per_jogchave_time2 = 1.25
    elif jog_chave_time2 < 4:
        per_jogchave_time2 = 0.75
    


    chance_ganhar_time2 = per_tit_time2 + per_jog_casa_time2 + per_jogchave_time2 + chance_ganhar_time2

    print (time1, " : ", vit_ult15_time1, " VITÓRIAS [15]")
    print (time1, " : ", der_ult15_time1, " DERROTAS [15]")
    print (time1, " : ", emp_ult15_time1, " EMPATES [15]")
    print (time1, " : ", golf_ult15_time1, " GOLS FEITOS [15]")
    print (time1, " : ", gols_ult15_time1, " GOLS SOFRIDOS [15]")
    print (time1, " : ", vit_cont_time1, " VITÓRIAS [5]")
    print (time1, " : ", der_cont_time1, " DERROTAS [5]")
    print (time1, " : ", emp_cont_time1, " EMPATES [5]")
    print (time1, " : ", golf_cont_time1, " GOLS FEITOS [5]")
    print (time1, " : ", gols_cont_time1, " GOLS SOFRIDOS [5]")
    print(time1, " : ", jog_casa_time1, " JOGA EM CASA [s/n]")
    print (time1, " : ", titulares_time1," TITULARES")
    print (time1, " : ", jog_chave_time1, " JOGADORES CHAVE")
    print ("-------------------------------------------------------")
    print (time2, " : ", vit_ult15_time2, " VITÓRIAS [15]")
    print (time2, " : ", der_ult15_time2, " DERROTAS [15]")
    print (time2, " : ", emp_ult15_time2, " EMPATES [15]")
    print (time2, " : ", golf_ult15_time2, " GOLS FEITOS [15]")
    print (time2, " : ", gols_ult15_time2, " GOLS SOFRIDOS [15]")
    print (time2, " : ", vit_cont_time2, " VITÓRIAS [5]")
    print (time2, " : ", der_cont_time2, " DERROTAS [5]")
    print (time2, " : ", emp_cont_time2, " EMPATES [5]")
    print (time2, " : ", golf_cont_time2, " GOLS FEITOS [5]")
    print (time2, " : ", gols_cont_time2, " GOLS SOFRIDOS [5]")
    print(time2, " : ", jog_casa_time2, " JOGA EM CASA [s/n]")
    print (time2, " : ", titulares_time2," TITULARES")
    print (time2, " : ", jog_chave_time2, " JOGADORES CHAVE")
   
    dif_chance = chance_ganhar_time1 - chance_ganhar_time2




    if golf_ult15_time1 > gols_ult15_time2:
        chance_ganhar_time1 = chance_ganhar_time1 + 5
        chance_ganhar_time2 = chance_ganhar_time2 - 5
    
    
    if golf_ult15_time2 < gols_ult15_time1:
        chance_ganhar_time1 = chance_ganhar_time1 - 5
        chance_ganhar_time2 = chance_ganhar_time2 + 5



    if golf_cont_time1 > gols_cont_time2:
        chance_ganhar_time2 = chance_ganhar_time2 - 2.5
        chance_ganhar_time1 = chance_ganhar_time1 + 2.5



    if golf_cont_time2 > gols_cont_time2:
        chance_ganhar_time2 = chance_ganhar_time2 - 2.5
        chance_ganhar_time1 = chance_ganhar_time1 + 2.5
    

    if golf_ult15_time1 > golf_ult15_time2:
        chance_ganhar_time2 = chance_ganhar_time2 - 2.5
        chance_ganhar_time1 = chance_ganhar_time1 + 2.5


    if golf_ult15_time1 < golf_ult15_time2:
        chance_ganhar_time2 = chance_ganhar_time2 + 2.5
        chance_ganhar_time1 = chance_ganhar_time1 - 2.5


    chance_empate = (chance_ganhar_time2 + chance_ganhar_time1) - 100
    chance_empate = chance_empate*(-1)
    dif_chance = chance_ganhar_time1 - chance_ganhar_time2


    if (chance_ganhar_time2 + chance_ganhar_time1) > 100:
        chance_ganhar_time2 = chance_ganhar_time2*0.55
        chance_ganhar_time1 = chance_ganhar_time1*0.55  


    chance_empate = (chance_ganhar_time2 + chance_ganhar_time1) - 100
    chance_empate = chance_empate*(-1)
    dif_chance = chance_ganhar_time1 - chance_ganhar_time2  


    print (time1, " = {:.2f}".format(chance_ganhar_time1), " %")
    print (time2, " = {:.2f}".format(chance_ganhar_time2), " %")
    print ("Empate = {:.2f}".format(chance_empate), " %")
    if dif_chance < 0:
        dif_chance = dif_chance*(-1)
        print ("Diferença = {:.2f}".format(dif_chance), " %")
    elif dif_chance >= 0:
        print ("Diferença = {:.2f}".format(dif_chance), " %")
       
        
    x = str(input("Pressione ENTER para continuar ou n para parar: "))


      
else: 
    print ("FIM DO JOGO")