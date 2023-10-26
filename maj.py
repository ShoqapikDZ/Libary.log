import sqlite3

# Chemin du fichier de base de données SQLite
db_file = "Db.db"

# Établir la connexion à la base de données
conn = sqlite3.connect(db_file)

# Créer un curseur pour exécuter des requêtes SQL
cur = conn.cursor()

#Mettre ci-dessous les modifications de la base de donnée à éxecuter



conn.commit()
conn.close()
