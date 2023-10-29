import tkinter as tk
from tkinter import messagebox, Toplevel, ttk
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

def Main(donnees_books,donnees_emprunt,donnees_user):

#Toplevels

    def Add_book():
        def ajouter_livre(Titre,Auteur,NumeroSerie,Genre,fenetre):
            db.ajouter_book(Titre.get(),Auteur.get(),NumeroSerie.get(),Genre.get())
            fenetre.destroy()

        vert_spotify = "#1DB954"
        noir = "#000000"
        blanc = "#FFFFFF"
        fenetre = Toplevel()
        fenetre.title("Ajouter un nouveau livre")
        fenetre.geometry("400x300")
        fenetre.resizable(False,False)
        fenetre.configure(bg=noir)
        fenetre.iconbitmap("assets\livres-empiles.ico")

        # Cadre de connexion
        frame = tk.Frame(fenetre, bg=vert_spotify)
        frame.grid(row=0, column=0, padx=50, pady=50, sticky='nsew')

        label_title = tk.Label(frame, text="Titre", bg=vert_spotify, fg=blanc)
        label_title.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        Titre = tk.Entry(frame, bg=blanc, fg=noir)
        Titre.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        # Label Mot de passe
        label_auteur = tk.Label(frame, text="Auteur", bg=vert_spotify, fg=blanc)
        label_auteur.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        Auteur= tk.Entry(frame, bg=blanc, fg=noir)
        Auteur.grid(row=1, column=1, padx=10, pady=10, sticky='e')

        label_numS = tk.Label(frame, text="Numéro de Série", bg=vert_spotify, fg=blanc)
        label_numS.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        NumeroSerie= tk.Entry(frame, bg=blanc, fg=noir)
        NumeroSerie.grid(row=2, column=1, padx=10, pady=10, sticky='e')

        label_genre = tk.Label(frame, text="Genre", bg=vert_spotify, fg=blanc)
        label_genre.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        Genre= tk.Entry(frame, bg=blanc, fg=noir)
        Genre.grid(row=3, column=1, padx=10, pady=10, sticky='e')

        # Bouton de connexion
        bouton_connexion = tk.Button(frame, text="Ajout du nouveau livre", bg=vert_spotify, fg=blanc, width=20, height=2, command=lambda: ajouter_livre(Titre,Auteur,NumeroSerie,Genre, fenetre))
        bouton_connexion.grid(row=4, columnspan=2, padx=10, pady=20)

        # Ajustement automatique en fonction de la taille de la fenêtre
        for i in range(3):  # 3 lignes
            frame.grid_rowconfigure(i, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        fenetre.mainloop()

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
        fenetre.iconbitmap("assets\livres-empiles.ico")
        

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

    def Add_emprunt():
        pass
#Page

    window = tk.Tk()
    window.title("Page d'Accueil")
    window.iconbitmap("assets\livres-empiles.ico")
    window.geometry("1400x1080")

    bouton_deconnexion = tk.Button(window, text="Se déconnecter", command=lambda: db.deconnexion(window), bg="red", fg="black")
    bouton_deconnexion.pack()

    bouton_ajout_user = tk.Button(window, text="Ajouter un utilisateur", command=lambda: Ajout_user(), bg="grey", fg="black")
    bouton_ajout_user.pack()

    bouton_ajout_book = tk.Button(window, text="Ajouter un livre", command=lambda: Add_book(), bg="grey", fg="black")
    bouton_ajout_book.pack()

    bouton_new_emprunt = tk.Button(window, text="Nouvel emprunt",bg="grey",fg="black",command=lambda: Add_emprunt())
    bouton_new_emprunt.pack()
    #Table books
    table_frame = ttk.Frame(window)
    table_frame.pack()

    tree = ttk.Treeview(table_frame, columns=("Titre", "Auteur", "Numéro de Série", "Genre", "Disponibilité"))
    tree.heading("#1", text="Titre")
    tree.heading("#2", text="Auteur")
    tree.heading("#3", text="Numéro de Série")
    tree.heading("#4", text="Genre")
    tree.heading("#5", text="Disponibilité")
    
    tree.column("#1", stretch=tk.YES, anchor="w")
    tree.column("#2", stretch=tk.YES, anchor="w")
    tree.column("#3", stretch=tk.YES, anchor="w")
    tree.column("#4", stretch=tk.YES, anchor="w")
    tree.column("#5", stretch=tk.YES, anchor="w")
    
    tree.pack(fill="both", expand=True)

    for instance in donnees_books:
        if instance[4] == 0:
            disponibilite = "Oui"
        else:
            disponibilite = "Non"

        tree.insert("", "end", values=(instance[0], instance[1], instance[2], instance[3], disponibilite))

    #Table Emprunts
    tree1 = ttk.Treeview(table_frame, columns=("Emprunteur","Titre", "Auteur", "Date d'emprunt", "Date limite"))
    tree1.heading("#1", text="Emprunteur")
    tree1.heading("#2", text="Titre")
    tree1.heading("#3", text="Auteur")
    tree1.heading("#4", text="Date d'emprunt")
    tree1.heading("#5", text="Date limite")
    
    tree1.column("#1", stretch=tk.YES, anchor="w")
    tree1.column("#2", stretch=tk.YES, anchor="w")
    tree1.column("#3", stretch=tk.YES, anchor="w")
    tree1.column("#4", stretch=tk.YES, anchor="w")
    
    tree1.pack(fill="both", expand=True)

    for instance in donnees_emprunt:
        user_value = None
        titre = None
        autor = None

        for user in donnees_user:
            if instance[1] == user[0]:
                user_value = user[1]

        for book in donnees_books:
            if instance[2] == book[2]:
                titre = book[0]
                autor = book[1]

        tree1.insert("", "end", values=(user_value, titre, autor, instance[3], instance[4]))




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

