import sqlite3
import csv

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

    def csv_actualisation_user(self):
        # Exécutez une requête pour récupérer toutes les données de la table
        self.cur.execute("SELECT * FROM Utilisateurs")

        # Récupérez toutes les lignes de résultat
        donnees = self.cur.fetchall()

        # Chemin du fichier CSV de sortie
        csv_file = "Template/utilisateurs.csv"

        # Écrivez les données dans le fichier CSV
        with open(csv_file, "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)

            # Écrivez l'en-tête du fichier CSV
            en_tete = [description[0] for description in self.cur.description]
            csv_writer.writerow(en_tete)

            # Écrivez les données
            csv_writer.writerows(donnees)

        print(f"Les données ont été exportées dans {csv_file}.")

    def creer_table(self, nom_table, colonnes):
        # Créer la table avec les colonnes spécifiées
        self.cur.execute(f"CREATE TABLE IF NOT EXISTS {nom_table} ({', '.join(colonnes)})")

        # Valider les modifications et fermer la connexion
        self.conn.commit()

    def ajouter_utilisateur(self, nom_utilisateur, mot_de_passe):
        # Insérer un nouvel utilisateur dans la table
        self.cur.execute("INSERT INTO Utilisateurs (NomUtilisateur, MotDePasse) VALUES (?, ?)", (nom_utilisateur, mot_de_passe))

        # Valider les modifications et fermer la connexion
        self.conn.commit()

class Toolsbox:


# Utilisez la variable code_python pour obtenir le code Python sous forme de chaîne de caractères. Vous pouvez ensuite l'exécuter comme du code Python en utilisant exec(), ou l'enregistrer dans un fichier si nécessaire. Assurez-vous de personnaliser le chemin de la base de données et d'autres détails selon vos besoins spécifiques.

    def console_test():
        pmtr = ''
        while pmtr != "exit":
            pmtr = input("Entrez votre code : ")
            exec(pmtr)

