#!/usr/bin/python3
import csv
import shutil #déplacer les fichiers
import os #gére la création de l'arborescence


#Répare le fichier csv en remplacant les points virgules par des virgules 
remplace = open("vacsi-v-fra-2022-01-06-19h05.csv", "r")
remplace = ''.join([i for i in remplace])
remplace = remplace.replace(";",",")

a = open("vacsi-v-fra-2022-01-06-19h05.csv","w")
a.writelines(remplace)
a.close
 
#création de nos fichiers css
file=open("vacsi-v-fra-2022-01-06-19h05.csv", "r")
css=open("style.css",'w',encoding="utf-8")

#Supprime l'intégralité des fichiers (met à jour le site avec les nouvelles informations du csv
try:
	shutil.rmtree('interface') 
except:
	print("Visualisation des données")
else:
	print("Mise à jour avec les nouvelles données")
	
#Création de l'arborescence et déplacement des dossiers
os.mkdir('interface')

os.mkdir('css')
shutil.move('css','interface')

css.write(
"""/*----------------------
 	General
----------------------*/

html, body {
  font-family: 'Quicksand', sans-serif;
  padding:0;
  margin:0;
  height: 100%;
}

html {
  background-size: cover; /* version standardisée */
  height: 100%;
  top: 0;
	left: 0; 
}

#MODERNA
file=open("vacsi-v-fra-2022-01-06-19h05.csv", "r")
html=open("moderna.html",'w',encoding="utf-8")
html.write(page)
html.write("""<table class=table>
		<thead>
        <td class=jour>Jour</td>
        <td class=test>Première dose</td>
        <td class=test>Deuxième dose</td>
        <td class=test>Troisième dose</td>
        <td class=test>Quatrième dose</td>
        <td class=test>Rappel</td>
        <td class=test>Cumulation une</td>
        <td class=test>Cumulation deux</td>
        <td class=test>Cumulation trois</td>
        <td class=test>Cumulation quatre</td>
        <td class=test>Cumulation rappel</td
	</thead>""")

#PFIZER
file=open("vacsi-v-fra-2022-01-06-19h05.csv", "r")
html=open("pfizer.html",'w',encoding="utf-8")
html.write(page)
html.write("""<table class=table>
		<thead>
        <td class=jour>Jour</td>
        <td class=test>Première dose</td>
        <td class=test>Deuxième dose</td>
        <td class=test>Troisième dose</td>
        <td class=test>Quatrième dose</td>
        <td class=test>Rappel</td>
        <td class=test>Cumulation une</td>
        <td class=test>Cumulation deux</td>
        <td class=test>Cumulation trois</td>
        <td class=test>Cumulation quatre</td>
        <td class=test>Cumulation rappel</td
	</thead>""")