import tkinter as tk
from tkinter import messagebox, Toplevel
from tools import Database
from PIL import Image, ImageTk, ImageDraw

db = Database()

def round_rectangle(width, height, radius, fill_color, border_color):
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    dc = ImageDraw.Draw(image)
    dc.rounded_rectangle((0, 0, width, height), radius, fill=fill_color, outline=border_color)
    return ImageTk.PhotoImage(image)

def verifier_connexion(entry_nom_utilisateur,entry_mot_de_passe,window):
    nom_utilisateur = entry_nom_utilisateur.get()
    mot_de_passe = entry_mot_de_passe.get()
    
    if not nom_utilisateur or not mot_de_passe:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
    else:
        if db.connexion(nom_utilisateur, mot_de_passe):
            messagebox.showinfo("Succès", "Connexion réussie!")
            window.destroy()
        else :
            messagebox.showerror("Erreur","Nom d'Utilisateur ou Mot de passe incorrect.")

def Main():
    def Ajout_user():
        def add_user(mot_de_passe,nom_utilisateur, fenetre):
            nameUser = nom_utilisateur.get()
            mdp = mot_de_passe.get()
            db.ajouter_utilisateur(nameUser,mdp)
            fenetre.destroy()

        vert_spotify = "#1DB954"
        noir = "#000000"
        blanc = "#FFFFFF"
        fenetre = Toplevel()
        fenetre.title("Ajouter un utilisateur")
        fenetre.geometry("400x300")
        fenetre.resizable(False,False)
        fenetre.configure(bg=noir)
        

        # Cadre de connexion
        frame = tk.Frame(fenetre, bg=vert_spotify)
        frame.grid(row=0, column=0, padx=50, pady=50, sticky='nsew')

        # Label Nom d'utilisateur
        label_nom_utilisateur = tk.Label(frame, text="Nom d'utilisateur", bg=vert_spotify, fg=blanc)
        label_nom_utilisateur.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        entry_nom_utilisateur = tk.Entry(frame, bg=blanc, fg=noir)
        entry_nom_utilisateur.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        # Label Mot de passe
        label_mot_de_passe = tk.Label(frame, text="Mot de passe", bg=vert_spotify, fg=blanc)
        label_mot_de_passe.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        entry_mot_de_passe = tk.Entry(frame, bg=blanc, fg=noir, show="*")
        entry_mot_de_passe.grid(row=1, column=1, padx=10, pady=10, sticky='e')

        # Bouton de connexion
        bouton_connexion = tk.Button(frame, text="Création utilisateur", bg=vert_spotify, fg=blanc, width=20, height=2, command=lambda: add_user(entry_mot_de_passe,entry_nom_utilisateur, fenetre))
        bouton_connexion.grid(row=2, columnspan=2, padx=10, pady=20)

    # Ajustement automatique en fonction de la taille de la fenêtre
        for i in range(3):  # 3 lignes
            frame.grid_rowconfigure(i, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        fenetre.mainloop()

    window = tk.Tk()
    window.title("Page d'Accueil")
    window.iconbitmap("assets\livres-empiles.ico")
    window.geometry("1400x1080")

    bouton_deconnexion = tk.Button(window, text="Se déconnecter", command=lambda: db.deconnexion(window), bg="red", fg="black")
    bouton_deconnexion.pack()

    bouton_ajout_user = tk.Button(window, text="Ajouter un utilisateur", command=lambda: Ajout_user(), bg="grey", fg="black")
    bouton_ajout_user.pack()

    window.mainloop()



def Connexion_view():
    window = tk.Tk()
    window.iconbitmap("assets\livres-empiles.ico")
    window.title("Connexion")
    window.geometry("400x300")
    window.resizable(False, False)

    # Couleurs inspirées de Spotify
    vert_spotify = "#1DB954"
    noir = "#000000"
    blanc = "#FFFFFF"

    # Mise en page principale
    window.configure(bg=noir)

    # Cadre de connexion
    frame = tk.Frame(window, bg=vert_spotify)
    frame.grid(row=0, column=0, padx=50, pady=50, sticky='nsew')  # Ajuste au nord, au sud, à l'est et à l'ouest

    # Label Nom d'utilisateur
    label_nom_utilisateur = tk.Label(frame, text="Nom d'utilisateur", bg=vert_spotify, fg=blanc)
    label_nom_utilisateur.grid(row=0, column=0, padx=10, pady=10, sticky='w')

    entry_nom_utilisateur = tk.Entry(frame, bg=blanc, fg=noir)
    entry_nom_utilisateur.grid(row=0, column=1, padx=10, pady=10, sticky='e')

    # Label Mot de passe
    label_mot_de_passe = tk.Label(frame, text="Mot de passe", bg=vert_spotify, fg=blanc)
    label_mot_de_passe.grid(row=1, column=0, padx=10, pady=10, sticky='w')

    entry_mot_de_passe = tk.Entry(frame, bg=blanc, fg=noir, show="*")
    entry_mot_de_passe.grid(row=1, column=1, padx=10, pady=10, sticky='e')

    # Bouton de connexion
    bouton_connexion = tk.Button(frame, text="Connexion", bg=vert_spotify, fg=blanc, width=20, height=2, command=lambda: verifier_connexion(entry_nom_utilisateur, entry_mot_de_passe, window))
    bouton_connexion.grid(row=2, columnspan=2, padx=10, pady=20)

    # Ajustement automatique en fonction de la taille de la fenêtre
    for i in range(3):  # 3 lignes
        frame.grid_rowconfigure(i, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)

    window.mainloop()

