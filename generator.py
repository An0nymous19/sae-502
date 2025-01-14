#!/usr/bin/python3
import csv


#Répare le fichier csv en remplacant les points virgules par des virgules 
remplace = open("vacsi-v-fra-2022-01-06-19h05.csv", "r")
remplace = ''.join([i for i in remplace])
remplace = remplace.replace(";",",")

a = open("vacsi-v-fra-2022-01-06-19h05.csv","w")
a.writelines(remplace)
a.close
 
