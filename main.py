#Mes imports
import tkinter as tk 
from graphic import Main, Connexion_view
import sqlite3
import csv
from tools import Database
from tools import Toolsbox
import os, sys 
from PIL import Image, ImageTk

def redef(donnees_user):
    verif_connexions = {}
    for indication in donnees_user :
        
        if indication[3] == 1:
            verif_connexions.update({f"User-{str(indication[0])}":True})
        else:
            verif_connexions.update({f"User-{str(indication[0])}":False})
    contient_true = any(valeur for valeur in verif_connexions.values() if valeur is True)
    if contient_true:
        Main()

#Mes definitions 
db = Database()
tb = Toolsbox()
donnees_user = db.instance_user()
verif_connexions = {}
for indication in donnees_user :
    
    if indication[3] == 1:
        verif_connexions.update({f"User-{str(indication[0])}":True})
    else:
        verif_connexions.update({f"User-{str(indication[0])}":False})
contient_true = any(valeur for valeur in verif_connexions.values() if valeur is True)




#Architecture Graphique 

if contient_true:
    Main()
else:
    Connexion_view()
    redef(db.instance_user())






