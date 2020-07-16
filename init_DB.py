import sqlite3
import hashlib

conn = sqlite3.connect('boutique.db')
cur = conn.cursor()

#Delete des tables
req = "DROP TABLE client" 
cur.execute(req)
conn.commit()

req = "DROP TABLE produit" 
cur.execute(req)
conn.commit()

#Création des tables
req = "CREATE TABLE client (id INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT NOT NULL, nom TEXT NOT NULL, prenom TEXT NOT NULL, password TEXT NOT NULL, role TEXT NOT NULL)" 
cur.execute(req)
conn.commit()

req = "CREATE TABLE produit (id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT NOT NULL, description TEXT NOT NULL, prix DOUBLE)" 
cur.execute(req)
conn.commit()

#Insertion des données
password = "azerty123"
cur.execute ("INSERT INTO client ('login', 'nom', 'prenom', 'password', 'role') VALUES (?, ?, ?, ?, ?)", ("RojonL", "Rojon", "Loic", str(password), "user"))
conn.commit ()

password = "qsdfgh456"
cur.execute ("INSERT INTO client ('login', 'nom', 'prenom', 'password', 'role') VALUES (?, ?, ?, ?, ?)", ("LopezGomezJ", "Lopez Gomez", "Jonathan", str(password), "user"))
conn.commit ()

password = "Admin"
cur.execute ("INSERT INTO client ('login', 'nom', 'prenom', 'password', 'role') VALUES (?, ?, ?, ?, ?)", ("Admin", "istrateur", "Admin", str(password), "admin"))
conn.commit ()

cur.execute ("INSERT INTO produit ('nom', 'description', 'prix') VALUES (?, ?, ?)", ("Farfalle", "500g de farfalle", 0.82))
conn.commit()

cur.execute ("INSERT INTO produit ('nom', 'description', 'prix') VALUES (?, ?, ?)", ("Farfalle", "1kg de farfalle", 1.53))
conn.commit()

cur.execute ("INSERT INTO produit ('nom', 'description', 'prix') VALUES (?, ?, ?)", ("Fusilli", "500g de fusilli", 0.99))
conn.commit()

cur.execute ("INSERT INTO produit ('nom', 'description', 'prix') VALUES (?, ?, ?)", ("Fusilli", "1kg de fusilli", 1.87))
conn.commit()

cur.execute ("INSERT INTO produit ('nom', 'description', 'prix') VALUES (?, ?, ?)", ("Pastabox", "Fusilli à la bolognaise 300g", 1.71))
conn.commit()

cur.execute ("INSERT INTO produit ('nom', 'description', 'prix') VALUES (?, ?, ?)", ("Pastabox", "Fusilli à la carbonara 300g", 1.80))
conn.commit()

cur.execute ("INSERT INTO produit ('nom', 'description', 'prix') VALUES (?, ?, ?)", ("Pastabox", "Fusilli aux fromages italiens 300g", 1.72))
conn.commit()

cur.execute ("INSERT INTO produit ('nom', 'description', 'prix') VALUES (?, ?, ?)", ("Pastabox", "Fusilli au saumon 300g", 2.69))
conn.commit()

cur.execute ("INSERT INTO produit ('nom', 'description', 'prix') VALUES (?, ?, ?)", ("Penne Rigate", "500g de penne rigate", 0.84))
conn.commit()

# Fermer la connexion 
conn.close