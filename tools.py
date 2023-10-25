import sqlite3
import csv
from datetime import date, datetime
import sqlite3
import csv

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
    
    def ajouter_book(self,title,autor,numS,genre,is_emprunté):
        self.cur.execute("INSERT INTO Books_new (Titre,Auteur,NumeroSerie,Genre,Emprunte) VALUES(?,?,?,?,?)", (title,autor,numS,genre,is_emprunté))

        self.conn.commit()
    
    def new_emprunt(self, numS, UtilisateurID,Year,Month,Day):
        self.DateLimite = datetime(Year, Month, Day).strftime('%Y-%m-%d')
        self.DateEmprunt = date.today()
        self.cur.execute("UPDATE Books_new SET Emprunte = TRUE WHERE NumeroSerie = ?",(numS,))
        self.cur.execute("INSERT INTO Emprunt (UtilisateurID,LivreID,DateEmprunt,DateLimite) VALUES (?,?,?,?)  ;",(UtilisateurID,numS,self.DateEmprunt,self.DateLimite))

        self.conn.commit()

    def delete_emprunt(self, numS):
        self.cur.execute("UPDATE Books_new SET Emprunte = 0 WHERE NumeroSerie = ?",(numS,))
        self.cur.execute("DELETE FROM Emprunt WHERE LivreID = ?",(numS,))
        self.conn.commit()

    def instance_user(self):
        self.cur.execute("SELECT * FROM Utilisateurs ;")

        # Récupérer toutes les lignes de résultat
        self.donnees_user = self.cur.fetchall()
        
        return self.donnees_user 

    def connexion(self, NomUtilisateur, MotDePasse):
        self.cur.execute("UPDATE Utilisateurs SET Is_connected = 1 WHERE NomUtilisateur = ? AND MotDePasse = ?", (NomUtilisateur, MotDePasse))
        self.conn.commit()

    def deconnexion(self, NomUtilisateur):
        self.cur.execute("UPDATE Utilisateurs SET Is_connected = 0 WHERE NomUtilisateur = ?",(NomUtilisateur,))
        self.conn.commit()
class Toolsbox:
    def __init__(self):
        self.pmtr = ""

    def console_test(self):
        while self.pmtr != "exit":
            self.pmtr = input("Entrez votre code : ")
            exec(self.pmtr)


