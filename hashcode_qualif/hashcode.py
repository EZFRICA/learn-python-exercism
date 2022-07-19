# a_an_example.in.txt


import os
name_file = 'a_an_example.in.txt'
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