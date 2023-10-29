#Mes imports
import tkinter as tk 
from tkinter import ttk, messagebox, Toplevel
from graphic import Main, Connexion_view
import sqlite3
import csv
from tools import Database
from tools import Toolsbox
import os, sys 
from PIL import Image, ImageTk

def redef(opt):
    donnees_user = db.instance_user()
    verif_connexions = {}
    for indication in donnees_user :
        
        if indication[3] == 1:
            verif_connexions.update({f"User-{str(indication[0])}":True})
        else:
            verif_connexions.update({f"User-{str(indication[0])}":False})
    contient_true = any(valeur for valeur in verif_connexions.values() if valeur is True)
    if opt == 1:
        if contient_true:
            Main(donnees_books=donnees_books,donnees_user=donnees_user,donnees_emprunt=donnees_emprunt)
            redef(2)
    elif opt == 2 : 
        if contient_true == False :
            Connexion_view()
            redef(1)

#Mes definitions 
db = Database()
tb = Toolsbox()
donnees_user = db.instance_user()
donnees_emprunt = db.instance_emprunt()
donnees_books = db.instance_books()
verif_connexions = {}
for indication in donnees_user :
    
    if indication[3] == 1:
        verif_connexions.update({f"User-{str(indication[0])}":True})
    else:
        verif_connexions.update({f"User-{str(indication[0])}":False})
contient_true = any(valeur for valeur in verif_connexions.values() if valeur is True)




#Architecture Graphique 
if contient_true:
    Main(donnees_books=donnees_books,donnees_user=donnees_user,donnees_emprunt=donnees_emprunt)
    redef(2)
else:
    Connexion_view()
    redef(1)