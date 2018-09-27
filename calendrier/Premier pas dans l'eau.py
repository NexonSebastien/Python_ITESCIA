from tkinter import *
from tkinter import tix, messagebox


# (4) Fonction de recherche de la valeur du mois
def rechercheMois(mois):
    # (4) tableau associatif pour retrouver la valeur qui corespond au mois
    tblMois = {"Janvier":0,
               "Fevrier":3,
               "Mars":3,
               "Avril":6,
               "Mai":1,
               "Juin":4,
               "Juillet":6,
               "Aout":2,
               "Septembre":5,
               "Octobre":0,
               "Novembre":3,
               "Decembre":5}
    return tblMois[mois]

# (5) Fonction de recherche si l'année est bissextile ou non
def anneeBissextile(annee):
    check = False
    if annee % 4 == 0:
        if annee % 100 == 0:
            if annee % 400 == 0:
                check = True
        else:
            check = True
    return check

# (6) Fonction de recherche de la valeur du siecle
def rechercheSiecle(annee):
    annee = annee // 100
    # (6) tableau associatif pour retrouver la valeur qui corespond au siecle
    tblSiecle ={16:6,
                17:4,
                18:2,
                19:0,
                20:6,
                21:4}
    return tblSiecle[annee]

# (8) Fonction de recherche du jour de la semaine recherché
def rechercheJour(resultat):
    # (8) tableau associatif pour retrouver la valeur qui corespond au jour de la semaine recherché
    tblJour = {0:"Dimanche",
               1:"Lundi",
               2:"Mardi",
               3:"Mercredi",
               4:"Jeudi",
               5:"Vendredi",
               6:"Samedi",}
    return tblJour[resultat]

def recherche():
	# Recupération de la saisie des variable
    jour = int(jourSaisie.get())
    mois = cbVar.get()
    annee = int(anneeSaisie.get())

    # Remise à vide du champ resultat
    lblResultat.config(text="")

    # Verification de la saisie d'un jour valide selon le mois(Janvier = 31 jours, Avril = 30 jours)
    if mois in ['Avril','Juin','Septembre','Novembre'] and jour > 30:
        messagebox.showinfo("ERREUR SAISIE !!!", "Le mois "+mois+" comporte que 30 jours")
        return ""
    elif mois == "Fevrier" and jour > 29 and anneeBissextile(annee) == True:
        messagebox.showinfo("ERREUR SAISIE !!!", "Le mois de Fevrier comporte que 29 jours les années bisextile")
        return ""
    elif mois == "Fevrier" and jour > 28 and anneeBissextile(annee) == False:
        messagebox.showinfo("ERREUR SAISIE !!!", "Le mois de Fevrier comporte que 28 jours")
        return ""

    # (1) Garder les deux derniers chiffres de l'année
    resultat = (annee % 100)
	
    # (2) Ajout de 1/4 en ignorant le reste
    resultat += (resultat//4)
	
    # (3) Ajout de la journée
    resultat += jour
	
    # (4) Ajout de la valeur du mois
    resultat += rechercheMois(mois)
	
    # (5) Retrait de 1 pour les année bissextile de janvier ou fevrier
    if anneeBissextile(annee) == True and (mois == "Janvier" or mois == "Fevrier"):
        resultat += -1
		
    # (6) Ajout de la valeur du siècle
    resultat += rechercheSiecle(annee)
	
    # (7) On divise par 7 et on garde le reste
    resultat = resultat % 7
	
    # (8) Recherche du jour de la semaine recherché
    leJour = rechercheJour(resultat)
    lblResultat.config(text=leJour)

# FENETRE
#Accueil
fenetreAccueil = Tk()
fenetreAccueil.title("Premier pas dans l'eau")

# JOUR
lblJour = Label(fenetreAccueil, text="Jour :").pack()
# Permet de faire une saisie de nombre entre 1 et 31 sans que l'utilisateur ecrire dans le champ
jourSaisie = Spinbox(fenetreAccueil, from_=1, to=31, state="readonly")
jourSaisie.pack()

# MOIS
lblMois = Label(fenetreAccueil, text="Mois :").pack()
# Utilisation de Tix pour faire une liste deroulante
fenetreAccueil.tk.eval('package require Tix')
cbVar = tix.StringVar()
combo = tix.ComboBox(fenetreAccueil,dropdown=1, variable=cbVar)
combo.entry.config(state='readonly')  #Lecture seul dans la zone de text
combo.insert(0, 'Janvier')
combo.insert(1, 'Fevrier')
combo.insert(2, 'Mars')
combo.insert(3, 'Avril')
combo.insert(4, 'Mai')
combo.insert(5, 'Juin')
combo.insert(6, 'Juillet')
combo.insert(7, 'Aout')
combo.insert(8, 'Septembre')
combo.insert(9, 'Octobre')
combo.insert(10, 'Novembre')
combo.insert(11, 'Decembre')
combo.pack()

# ANNEE
lblAnnee = Label(fenetreAccueil, text="Annee :").pack()
# Permet de faire une saisie de nombre entre 1600 et 2099 sans que l'utilisateur ecrire dans le champ (repeatinterval modifie la vitesse de defilement)
anneeSaisie = Spinbox(fenetreAccueil, from_= 1600,to=2099, state="readonly", repeatinterval=15)
anneeSaisie.pack()

# RESULTAT
lblResultat = Label(fenetreAccueil, text="")
lblResultat.pack()

bouttonValider = Button(fenetreAccueil, text="Valider",command=recherche).pack()

fenetreAccueil.mainloop()

# Sébastien NEXON