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

/*----------------------
 	Barre du menu
----------------------*/

.menu {
  padding:0; /* Suppression des marges internes */ 
  margin: 0;            
  background-color: #5e4a86;      /* Ajout de la couleur d'arrière-plan */
  justify-content: center; /* Alignements des liens dans le menu */ 
  opacity : 0.9;
  z-index: 3; /*superposition du menu*/
  position: fixed;
  width: 11%;
  height: 100vh;
}

.menu li {
  list-style-type: none ;       /* Suppression des puces */
}

/* Le contenu et les dimenssions de nos box*/

.menu a {
  display:block;                /* Transformation en block */
  min-width: 11%;             /* Largeur minimale des liens */   
  padding: 1.4rem 0;            /* Marges internes */
  text-align: left;         /* Centrage du texte */   
  padding-left: 10px;
  color: #fff;                  /* Couleur du texte */
  text-decoration: none;        /* Suppression du soulignement */
  border-radius: 2px;           /* Arrondis des bordures */
  transition: all 0.3s ;          /* Ajout des effets de transition */
  opacity : 0.9;
}

/* Cela va nous permettre de pouvoir donner un effet de sélection à notre menu*/

.menu a:hover,

 a:hover.actif{
  background-color: #eba3a3;
  color: #ffffff;
}

/*----------------------
 	Accueil
----------------------*/

.accueil {
  font-size: large;
  text-align: left;
  margin-left: 12%;
  margin-right: 1%;
  height: 100%;
  color: #000000;
  background-color: #ffffff;
  padding: 20px;
  font-family: 'Open Sans', sans-serif;
  position: relative;
  z-index: 2;
  top: 5px;
  box-shadow: rgba(0, 0, 0, 0.05) 0px 6px 24px 0px, rgba(0, 0, 0, 0.08) 0px 0px 0px 1px;
}

.donnée {
  font-size: large;
  text-align: left;
  margin-left: 12%;
  margin-right: 1%;
  height: 100%;
  color: #000000;
  background-color: #ffffff;
  padding: 20px;
  font-family: 'Open Sans', sans-serif;
  position: relative;
  z-index: 2;
  margin-top: 1%;
  box-shadow: rgba(0, 0, 0, 0.05) 0px 6px 24px 0px, rgba(0, 0, 0, 0.08) 0px 0px 0px 1px;
}

.information {
  
  font-size: large;
  text-align: left;
  margin-left: 12%;
  margin-right: 1%;
  height: 100%;
  color: #000000;
  background-color: #ffffff;
  padding-right: 20px;
  padding-left: 20px;
  padding-bottom: 20px;
  padding-top: 1px;
  font-family: 'Open Sans', sans-serif;
  position: relative;
  z-index: 2;
  text-align: justify;
  margin-top: 50px;
  box-shadow: rgba(9, 30, 66, 0.25) 0px 1px 1px, rgba(9, 30, 66, 0.13) 0px 0px 1px 1px;
  
}

.description {
    font-size: medium;
}

.text {
  font-size: medium;
}

a {
  text-decoration: none;
  color: #000000;
}

a:hover {
  color: blue;
}

.dose {
  font-size: large;
  text-align: left;
  margin-left: 12%;
  margin-right: 1%;
  height: 100%;
  color: #000000;
  background-color: #ffffff;
  padding: 20px;
  font-family: 'Open Sans', sans-serif;
  position: relative;
  z-index: 2;
  top: 5px;
  box-shadow: rgba(0, 0, 0, 0.05) 0px 6px 24px 0px, rgba(0, 0, 0, 0.08) 0px 0px 0px 1px;
}

/*----------------------
 	Visualisation
----------------------*/

.titre {
  font-size: large;
  text-align: left;
  margin-left: 12%;
  margin-right: 20%;
  color: #000000;
  background-color: #ffffff;
  padding: 20px;
  font-family: 'Open Sans', sans-serif;
  position: relative;
  z-index: 2;
  margin-top: 3%;
  box-shadow: rgba(0, 0, 0, 0.05) 0px 6px 24px 0px, rgba(0, 0, 0, 0.08) 0px 0px 0px 1px;
}

.table  {
  box-shadow: 0 5px 50px rgba(0,0,0,0.15);
  cursor: pointer;
  margin-left: 18%;
  margin-right: 20%;
  margin-top: 20px;
  height: 70vh;
  border: 2px solid rgb(141, 141, 192);
  border-collapse: collapse;
  display: block;
  overflow-x: auto;
  white-space: nowrap;
}

.test {
  background-color: rgb(17, 17, 63);
  color: #fff;
  text-align: center;
  overflow-x: auto;
  white-space: nowrap;
}

th, td {
  padding: 15px 20px;
  text-align: center;
  overflow-x: auto;
  white-space: nowrap;
}

.moyenne {
  background-color: rgb(17, 17, 63);
  color: #fff;
  text-align: left;
  overflow-x: auto;
  white-space: nowrap;
  width: 100%;
  text-align: center;
}

.jour {
  background-color: rgb(17, 17, 63);
  color: #fff;
  text-align: center;
  overflow-x: auto;
  white-space: nowrap;
}

.date {
  background-color: rgb(48, 25, 133);
  color:#ffffff
}

.moy  {
  box-shadow: 0 5px 50px rgba(0,0,0,0.15);
  cursor: pointer;
  margin-left: 18%;
  margin-right: 40%;
  margin-top: 20px;
  height: 70vh;
  border: 2px solid rgb(141, 141, 192);
  border-collapse: collapse;
  display: block;
  overflow-x: auto;
  white-space: nowrap;
}

/*----------------------
 	Responsive
----------------------*/

@media screen and (max-width: 550px) {
  body {
    align-items: flex-start;
  }
  .table{
    margin-left: 35%;
    margin-right: 20%;
    margin-top: 5%;
    font-size: 10px;
  }
  th, td {
    padding: 10px 7px;
}

.accueil{
  font-size: 10px;
}

.menu a {
  font-size: 10px;
}

.titre {
  font-size: 10px;
}

}""")


#on fait notre variable page pour la "structure" de notre site.
page = """<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html lang="fr">
<meta charset="UTF-8">

<head>
    <link rel="stylesheet"type="text/css"href="css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@300&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&display=swap" rel="stylesheet">        
    <title>DOUICHER Massi SAE15</title>
        
</head>

<!-- Page HTML -->

<htlm>
    <body>
      <head>
        <!-- Menu HTML -->
        <ul class="menu">
              <li class=h>
                <a href="../index.html">Accueil</a>
              </li>
              <li>
                <a href="pfizer.html">Pfizer/BioNTech</a>
              </li>
              <li>
                <a href="moderna.html">Moderna</a>
              </li>
              <li>
                <a href="astra.html">AstraZeneka</a>
              </li>
              <li>
                <a href="jan.html">Janssen</a>
              </li>
              <li>
                <a href="moyenne.html">Moyenne</a>
              </li>
        </ul>
      </head>



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

csvreader=csv.DictReader(file)

def boucle():
	vaccin='2'
	for row in csvreader:
		if row['vaccin']==vaccin:
			html.write("<tr><td class=date>"+row['jour']+"</td>  <td>"+row['n_dose1']+"</td>  <td>"+row['n_dose2']+"</td>  <td>"+row['n_dose3']+"</td>  <td>"+row['n_dose4']+"</td>  <td>"+row['n_rappel']+"</td>  <td>"+row['n_cum_dose1']+"</td>  <td>"+row['n_cum_dose2']+"</td>  <td>"+row['n_cum_dose3']+"</td>  <td>"+row['n_cum_dose4']+"</td>  <td>"+row['n_cum_rappel']+"</td></tr>")
boucle()
html.write("</tbody></table></body></html>")
html.close()

#ASTRA
file=open("vacsi-v-fra-2022-01-06-19h05.csv", "r")
html=open("astra.html",'w',encoding="utf-8")
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

csvreader=csv.DictReader(file)

def boucle():
	vaccin='3'
	for row in csvreader:
		if row['vaccin']==vaccin:
			html.write("<tr><td class=date>"+row['jour']+"</td>  <td>"+row['n_dose1']+"</td>  <td>"+row['n_dose2']+"</td>  <td>"+row['n_dose3']+"</td>  <td>"+row['n_dose4']+"</td>  <td>"+row['n_rappel']+"</td>  <td>"+row['n_cum_dose1']+"</td>  <td>"+row['n_cum_dose2']+"</td>  <td>"+row['n_cum_dose3']+"</td>  <td>"+row['n_cum_dose4']+"</td>  <td>"+row['n_cum_rappel']+"</td></tr>")
boucle()
html.write("</tbody></table></body></html>")
html.close()

#JAN
file=open("vacsi-v-fra-2022-01-06-19h05.csv", "r")
html=open("jan.html",'w',encoding="utf-8")
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

csvreader=csv.DictReader(file)
def boucle():
	vaccin='4'
	for row in csvreader:
		if row['vaccin']==vaccin:
			html.write("<tr><td class=date>"+row['jour']+"</td>  <td>"+row['n_dose1']+"</td>  <td>"+row['n_dose2']+"</td>  <td>"+row['n_dose3']+"</td>  <td>"+row['n_dose4']+"</td>  <td>"+row['n_rappel']+"</td>  <td>"+row['n_cum_dose1']+"</td>  <td>"+row['n_cum_dose2']+"</td>  <td>"+row['n_cum_dose3']+"</td>  <td>"+row['n_cum_dose4']+"</td>  <td>"+row['n_cum_rappel']+"</td></tr>")
boucle()
html.write("</tbody></table></body></html>")
html.close()
