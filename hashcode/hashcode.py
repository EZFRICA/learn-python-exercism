# a_an_example.in.txt
# b_basic.in.txt
# c_coarse.in.txt
# d_difficult.in.txt
# e_elaborate.in.txt

import os
name_file = 'e_elaborate.in.txt'
filename = os.path.join("input_data", name_file)
listaime = []
listnonaime = []
 
with open(filename, 'r') as file:
    line1 =  int("\n".join(file.readline().split()))
    if  1 <= line1 <= 10**5:
        liste_des_ingredients = file.readlines()
        taille_liste_des_ingredients = len(liste_des_ingredients)
        for i in range(0, taille_liste_des_ingredients):
            current_line = liste_des_ingredients[i].split()
            if(i % 2 == 0):
                if 1 <= int(current_line[0]) <= 5:
                    del current_line[0]
                    listaime.extend(current_line)
            else:
                if 0 <= int(current_line[0]) <= 5:
                    del current_line[0]
                    listnonaime.extend(current_line)


# print("tab aime = " + str(len(listaime)) + "   " + str(len(list(dict.fromkeys(listaime)))))
# print("tab n'aime pas = " + str(len(listnonaime)) + "   " + str(len(list(dict.fromkeys(listnonaime)))))

final_tab = []
file = open('e_elaborate.out.txt', 'w')
listaime_sans_double = list(dict.fromkeys(listaime))

if len(listnonaime) == 0:
    result = str(len(listaime_sans_double)) + " " + " ".join(listaime_sans_double)
    file.write(result)
elif name_file == "c_coarse.in.txt":
    for aime in listaime_sans_double:
        # print(" " + str(aime) + "   " + str(listaime.count(aime)) + "   naimepas   " + str(listnonaime.count(aime)))
        if listaime.count(aime) > listnonaime.count(aime):
            final_tab.append(aime)
    # final_tab = list(dict.fromkeys(final_tab))
    
    for aime in listaime_sans_double:
        somme = 0
        if listaime.count(aime) == listnonaime.count(aime):
            for i in range(taille_liste_des_ingredients):
                if (i % 2 == 0) and (aime in liste_des_ingredients[i]):
                    ing_non_aimer = liste_des_ingredients[i+1].split()
                    del ing_non_aimer[0]
                    for k in ing_non_aimer:
                        if k not in final_tab:
                            somme +=1
        if somme == listaime.count(aime):
            final_tab.append(aime)

    result = str(len(final_tab)) + " " + " ".join(final_tab)
    file.write(result)

else:
    for aime in listaime_sans_double:
        # print(" " + str(aime) + "   " + str(listaime.count(aime)) + "   naimepas   " + str(listnonaime.count(aime)))
        if listaime.count(aime) >= listnonaime.count(aime):
            final_tab.append(aime)
    # final_tab = list(dict.fromkeys(final_tab))

    result = str(len(final_tab)) + " " + " ".join(final_tab)
    file.write(result)
file.close()
