import sqlite3
import csv
from datetime import date, datetime
import sqlite3
import csv

import sqlite3
import csv
from datetime import date, datetime

class Database:
    def __init__(self, db_file="Db.db"):
        # Chemin du fichier de base de données SQLite
        self.db_file = db_file

        # Établir la connexion à la base de données
        self.conn = sqlite3.connect(self.db_file)

        # Créer un curseur pour exécuter des requêtes SQL
        self.cur = self.conn.cursor()

    def ajouter_utilisateur(self, nom_utilisateur, mot_de_passe):
        # Insérer un nouvel utilisateur dans la table
        self.cur.execute("INSERT INTO Utilisateurs (NomUtilisateur, MotDePasse) VALUES (?, ?)", (nom_utilisateur, mot_de_passe))
        # Valider les modifications et fermer la connexion
        self.conn.commit()

    def ajouter_book(self, title, autor, numS, genre):
        self.cur.execute("INSERT INTO Books_new (Titre, Auteur, NumeroSerie, Genre, Emprunte) VALUES (?, ?, ?, ?, ?)", (title, autor, numS, genre, 0))
        self.conn.commit()

    def new_emprunt(self, numS, UtilisateurID, Year, Month, Day):
        DateLimite = datetime(Year, Month, Day).strftime('%Y-%m-%d')
        DateEmprunt = date.today().strftime('%Y-%m-%d')
        self.cur.execute("UPDATE Books_new SET Emprunte = 1 WHERE NumeroSerie = ?", (numS,))
        self.cur.execute("INSERT INTO Emprunt (UtilisateurID, LivreID, DateEmprunt, DateLimite) VALUES (?, ?, ?, ?)", (UtilisateurID, numS, DateEmprunt, DateLimite))
        self.conn.commit()

    def delete_emprunt(self, numS):
        self.cur.execute("UPDATE Books_new SET Emprunte = 0 WHERE NumeroSerie = ?", (numS,))
        self.cur.execute("DELETE FROM Emprunt WHERE LivreID = ?", (numS,))
        self.conn.commit()

    def instance_user(self):
        self.cur.execute("SELECT * FROM Utilisateurs")
        # Récupérer toutes les lignes de résultat
        donnees_user = self.cur.fetchall()
        return donnees_user

    def instance_books(self):
        self.cur.execute("SELECT * FROM Books_new")
        # Récupérer toutes les lignes de résultat
        donnees_user = self.cur.fetchall()
        return donnees_user

    def instance_emprunt(self):
        self.cur.execute("SELECT * FROM Emprunt")
        # Récupérer toutes les lignes de résultat
        donnees_user = self.cur.fetchall()
        return donnees_user

    def connexion(self, NomUtilisateur, MotDePasse):
        self.cur.execute("SELECT * FROM Utilisateurs WHERE NomUtilisateur = ? AND MotDePasse = ?", (NomUtilisateur, MotDePasse))
        utilisateur = self.cur.fetchone()

        if utilisateur:
            # Les informations d'utilisateur sont correctes, marquez l'utilisateur comme connecté
            self.cur.execute("UPDATE Utilisateurs SET Is_connected = 1 WHERE NomUtilisateur = ?", (NomUtilisateur,))
            self.conn.commit()
            return True
        else:
            # Les informations d'utilisateur ne sont pas correctes
            return False


    def deconnexion(self,window):
        self.cur.execute("UPDATE Utilisateurs SET Is_connected = 0 ;")
        self.conn.commit()

        window.destroy()

class Toolsbox:
    def __init__(self):
        self.pmtr = ""

    def console_test(self):
        while self.pmtr != "exit":
            self.pmtr = input("Entrez votre code : ")
            exec(self.pmtr)


