import datetime
from tabulate import tabulate


class Support:
    def __init__(self, id: str, Titre: str, Disponibilité: bool):
        self.__id_support = id
        self.__Titre = Titre
        self.__Disponibilité = Disponibilité

    @property
    def id_support(self):
        return self.__id_support

    @id_support.setter
    def id_support(self, value):
        if isinstance(value, str):
            self.__id_support = value
        else:
            raise ValueError("L'id du support doit être une chaîne de caractères")

    @property
    def Titre(self):
        return self.__Titre

    @Titre.setter
    def Titre(self, value):
        if isinstance(value, str):
            self.__Titre = value
        else:
            raise ValueError("Le titre du support doit être une chaîne de caractères")

    @property
    def Disponibilité(self):
        return self.__Disponibilité

    @Disponibilité.setter
    def Disponibilité(self, value):
        if isinstance(value, bool):
            self.__Disponibilité = value
        else:
            raise ValueError("La disponibilité du support doit être un booléen")

    def estDiponible(self):
        return self.__Disponibilité

    def rendreDisponible(self):
        self.__Disponibilité = True

    def rendreIndisponible(self):
        self.__Disponibilité = False


class Livre(Support):
    def __init__(self, id: str, Titre: str, Disponibilité: bool, Auteur: str, NombrePages: int):
        super().__init__(id, Titre, Disponibilité)
        self.__Auteur = Auteur
        self.__NombrePages = NombrePages

    @property
    def Auteur(self):
        return self.__Auteur

    @Auteur.setter
    def Auteur(self, value):
        if isinstance(value, str):
            self.__Auteur = value
        else:
            raise ValueError("La author must be a string")

    @property
    def NombrePages(self):
        return self.__NombrePages

    @NombrePages.setter
    def NombrePages(self, value):
        if isinstance(value, int) and value > 0:
            self.__NombrePages = value
        else:
            raise ValueError("Le nombre de pages du livre doit être un entier")


class CD_ROM(Support):
    def __init__(self, id: str, Titre: str, Disponibilité: bool, Editeur: str, Capacite: int):
        super().__init__(id, Titre, Disponibilité)
        self.__Editeur = Editeur
        self.__Capacite = Capacite

    @property
    def Capacite(self):
        return self.__Capacite

    @Capacite.setter
    def Capacite(self, value):
        if isinstance(value, int) and value > 0:
            self.__Capacite = value
        else:
            raise ValueError("La capacité du CD-ROM doit être un entier")

    @property
    def Editeur(self):
        return self.__Editeur

    @Editeur.setter
    def Editeur(self, value):
        if isinstance(value, str):
            self.__Editeur = value
        else:
            raise ValueError("L'éditeur du CD-ROM doit être une chaîne de caractères")


class Magazine(Support):
    def __init__(self, id: str, Titre: str, Disponibilité: bool, Editeur: str, NumeroPublication: int,
                 DatePublication: datetime.date):
        super().__init__(id, Titre, Disponibilité)
        self.__Editeur = Editeur
        self.__NumeroPublication = NumeroPublication
        self.__DatePublication = DatePublication

    @property
    def Editeur(self):
        return self.__Editeur

    @Editeur.setter
    def Editeur(self, value):
        if isinstance(value, str):
            self.__Editeur = value
        else:
            raise ValueError("L'éditeur du magazine doit être une chaîne de caractères")

    @property
    def NumeroPublication(self):
        return self.__NumeroPublication

    @NumeroPublication.setter
    def NumeroPublication(self, value):
        if isinstance(value, int) and value > 0:
            self.__NumeroPublication = value
        else:
            raise ValueError("Le numéro de publication du magazine doit être un entier")

    @property
    def DatePublication(self):
        return self.__DatePublication

    @DatePublication.setter
    def DatePublication(self, date: datetime.date):
        if isinstance(date, datetime.date):
            self.__DatePublication = date
        else:
            raise ValueError("La date de publication du magazine doit être une date")


class Adherent:
    def __init__(self, id: str, Nom: str, Prenom: str,Numero_Support_Autorise : int):
        self.__id = id
        self.__Nom = Nom
        self.__Prenom = Prenom
        self.__Numero_Support_Autorise = Numero_Support_Autorise
    @property
    def id(self):
        return self.__id

    @property
    def Nom(self):
        return self.__Nom

    @property
    def Prenom(self):
        return self.__Prenom

    @property
    def Numero_Support_Autorise(self):
        return self.__Numero_Support_Autorise

    def Afficher(self):
        print(f"Nom : {self.__Nom}")
        print(f"Prenom :{self.__Prenom}")
        print(f"Numero_Support_Autorise :{self.__Numero_Support_Autorise}")


class Adherent_Payent(Adherent):
    def __init__(self,nom,prenom,Numero_Support_Autorise,NumeroSupport , JoursMax ,CIN):
        super.__init__(nom,prenom,Numero_Support_Autorise)
        self.__NumeroSupport = 3
        self.__JoursMax = 3
        self.__CIN = CIN

    @property
    def NumeroSupport(self):
       return  self.__NumeroSupport

    @NumeroSupport.setter
    def NumeroSupport(self,value):
        if isinstance(value,int) and 0 < value <= 3:
            self.__NumeroSupport = value
        else:
            raise ValueError("Numero du support et invalide")

    @property
    def JoursMax(self):
        return   self.__JoursMax

    @JoursMax.setter
    def JoursMax(self,value):
        if isinstance(value,int) and  0 < value <= 3 :
            self.__JoursMax = value
        else:
            raise ValueError("Jours max et invalide")

    @property
    def CIN(self):
        return  self.__CIN

    @CIN.setter
    def CIN(self,value):
        if isinstance(value , str):
            self.__CIN = value

    def Nb_Emprunt_Encours(self):
        if self.JoursMax > 0:
            return self.JoursMax
        else:
            return 0

class Adherent_Gratuit(Adherent):
    def __init__(self,nom,prenom,Numero_Support_Autorise,JoursMax,code):
        super.__init__(nom,prenom,Numero_Support_Autorise)
        self.__NumeroSupport = 1
        self.__JoursMax = 1
        self.__code = code

    @property
    def NumeroSupport(self):
       return  self.__NumeroSupport

    @NumeroSupport.setter
    def NumeroSupport(self,value):
        if isinstance(value,int) and value==1:
            self.__NumeroSupport = value
        else:
            raise ValueError("Numero du support et invalide")

    @property
    def JoursMax(self):
        return   self.__JoursMax

    @JoursMax.setter
    def JoursMax(self,value):
        if isinstance(value,int) and value==1:
            self.__JoursMax = value
        else:
            raise ValueError("Jours max et invalide")

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self,value):
        if isinstance(value,str) and value > 0:
            self.__code = value
        else:
            raise ValueError("code invalide")

class Emprunt():

    Liste_Empruntes = []
    __auto = 0
    def __init__(self , support ,adherent, dateEmprunt , dateRetour):
        Emprunt.__auto += 1
        self.__numeroEmprunt = Emprunt.__auto
        self.__support = support
        if support.est_Disponible():
           support.Rendre_Non_Disponible()
           self.__adherent = adherent
           self.__dateEmprunt = dateEmprunt
           self.__dateRetour = dateRetour
           self.Date_Retour_max = None

        else :
            raise ValueError("Le support est non disponible ")

    @property
    def numeroEmprunt(self):
       return  self.__numeroEmprunt

    @property
    def support(self):
        return self.__support

    @support.setter
    def support(self, nouvelleSupport):
        if isinstance(nouvelleSupport, Support):
            self.__support = nouvelleSupport
        else:
            raise ValueError("le support est un objet de Support !!")

    @property
    def adherent(self):
       return  self.__adherent

    @adherent.setter
    def adherent(self,nouvelleAdherent):
      if isinstance(nouvelleAdherent , Adherent):
        self.__adherent = nouvelleAdherent
      else :
          raise ValueError("l'adherent est un objet de Adherent !!")


    @property
    def dateEmprunt(self):
        return self.__dateEmprunt

    @dateEmprunt.setter
    def dateEmprunt(self, nouveau_Date_Emprunt : datetime.date ):
        if isinstance(nouveau_Date_Emprunt, datetime.date):
            self.__dateEmprunt = nouveau_Date_Emprunt
        else:
            raise ValueError(" la date Emprunt est invalid !!!")

    @property
    def dateRetour(self):
        return self.__dateRetour

    @dateRetour.setter
    def dateRetour(self, nouveau_Date_Retour = datetime.date):
        if isinstance(nouveau_Date_Retour, datetime.date):
            self.__dateRetour = nouveau_Date_Retour
        else:
            raise ValueError(" la date de publication est invalid !!!")

    @property
    def Date_Retour_max(self):
        return self.__DateRetourMaximale

    @Date_Retour_max.setter
    def Date_Retour_max(self, value):
        if isinstance(value, datetime.date):
            self.__DateRetourMaximale = value
        else:
            raise ValueError("la date de retoure max invalid !!")

    def Marquer_Support_Comme_Emprunte(self):
          if self.__support is None:
            return True
          return self.dateRetour > datetime.date.today()

    def Marquer_Support_Comme_Rendu(self):
        if self.__support is None:
            return False
        return self.dateRetour <= datetime.date.today()

    def Afficher_details(self):
            print(f"Numéro Emprunt: {self.__numeroEmprunt}"
                  f"Adhérent: {self.__adherent.nom} {self.__adherent.prenom}"
                  f"Support: {self.__support.titre}"
                  f"Date Emprunt: {self.__dateEmprunt.strftime('%d/%m/%Y')}"
                  f"Date Retour: {self.__dateRetour.strftime('%d/%m/%Y')}")

    def Retourner(self,date_Retour : datetime.date):
             self.__dateRetour = date_Retour
             if date_Retour < datetime.date.today() :
                self.support.Rendre_Disponible()
             else :
                 self.support.Rendre_Non_Disponible()

def afficher_menu():
    print("\n___________________________________________________")
    print("    LA GESTION DES EMPRUNTS   ")
    print("___________________________________________________\n")
    print("              Menu Principal             ")
    print("****************************************************")

    print("  1. 🔍 Afficher les détails d'un emprunt réalisés")
    print("  2. 📝 Afficher les emprunts en cours")
    print("  3. ⚠️ Afficher les emprunts en retard")
    print("  4. 👤 Afficher les emprunts d'un adhérent")
    print("  5. 📚 Afficher les emprunts d'un support")
    print("  6. 📊 Afficher les statistiques")
    print("  7. 📋 Afficher tous les emprunts")
    print("  8.📚 Afficher tous les supports")
    print("  9. ➕ Créer un emprunt")
    print("  10. ↩️ Retourner un emprunt")
    print("  0. 🚪 Quitter")
    print("**************************************************** ")

def Afficher_Supports(Liste_Supports):
    table_data = []
    for support in Liste_Supports:
        if isinstance(support , Livre):
           #if support.est_Disponible():
               #return("Disponible .")
           #else :
               #return ("Non Disponible .")
          statu = "Disponible" if support.est_Disponible() else "Non Disponible"
          table_data.append([
              support.id_support ,
              "Livre",
              support.titre,
              statu,
              support.auteur,
              f"{support.Nb_Page} pages",
              "_",
              "_",
              "_",
              "_"
           ])

        elif isinstance(support, CD_ROM):
                statu = "Disponible" if support.est_Disponible() else "Non Disponible"
                table_data.append([
                    support.id_support,
                    "CD_ROM",
                    support.titre,
                    statu,
                    "_",
                    "_",
                    "_",
                    f"{support.capacite} Mo",
                    "_",
                    support.editeur
                ])

        elif isinstance(support, Magazine):
            statu = "Disponible" if support.est_Disponible()else "Non Disponible"
            table_data.append([
                support.id_support,
                "Magazine",
                support.titre,
                statu,
                "_",
                "_",
                f"N°{support.NumeroPublic}",
                "_",
                str(support. datePublication)

            ])

    headers = ["ID", "Type", "Titre", "Statu", "Auteur", "Pages","Numéro pub", "Capacité","Date pub"]
    print("\n Liste des supports:")
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

def Afficher_Adherents(Liste_Adherents):
    table_data = [[
        adherent.id,
        adherent.nom,
        adherent.prenom,
    ]for adherent in Liste_Adherents]

    headers = ["ID","Nom","Prénom"]
    print("\n Liste des supports:")
    print(tabulate(table_data,headers =headers ,tablefmt = "fancy_grid" ))

def Afficher_Emprunts(Liste_Emprunts):
    table_data = [[
        emprunt.id ,
        emprunt.Support.titre,
        f"{emprunt.Adherent.nom} {emprunt.Adherent.prenom}",
        emprunt.dateEmprunt,
        emprunt.dateRetour if emprunt.dateRetour else "Non retourné"
    ] for emprunt in Liste_Emprunts]

    headers = ["ID", "Support", "Adhérent", "Date Emprunt", "Date Retour"]
    print("\n Liste des emprunts:")
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))



def Afficher_Details(Liste_Supports,Liste_Adherents,Liste_Emprunts):
    print("-----------Supports-----------\n")
    Afficher_Supports(Liste_Supports)
    print("-----------Adherents-----------\n")
    Afficher_Adherents(Liste_Adherents)
    print("-----------Emprunts-----------\n")
    Afficher_Emprunts(Liste_Emprunts)

def Ajouter_Support():
    print("\n=== Ou est le type voulez-vous ajouter ? ===")
    print("1. 📖 Livre")
    print("2. 💿 CD-ROM")
    print("3. 📰 Magazine")
    choix = input("\nVotre choix : ")

    id = input("ID du support : ")
    titre = input("Titre : ")

    if choix == "1" :
        auteur = input("Auteur : ")
        nb_pages = int(input("Nombre de pages : "))
        return Livre(id, titre, True, auteur, nb_pages)
    elif choix == "2" :
        editeur = input("Éditeur : ")
        capacite = int(input("Capacité (Mo) : "))
        return CD_ROM(id, titre, True, capacite, editeur)
    elif choix == "3" :
        numero = int(input("Numéro de publication : "))
        date_str = input("Date de publication (YYYY-MM-DD) : ")
        date= datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        return Magazine(id, titre, True,numero, date)
    else:
        print("❌ Le Choix est invalide!")
        return None

def Ajouter_Adherent():
    print("\n=== Nouvel adhérent ===")
    id = input("ID de l'adhérent : ")
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    return Adherent(id, nom, prenom)


def Afficher_Statistiques(Liste_Emprunts):
    total_emprunts = len(Liste_Emprunts)
    emprunts_en_cours = len([emprunt for emprunt in Liste_Emprunts if not emprunt.estRendu()])
    emprunts_retournes = len([emprunt for emprunt in Liste_Emprunts if emprunt.estRendu()])

    print("\n----------------------------------------------")
    print("         STATISTIQUES DES EMPRUNTS        ")
    print("------------------------------------------------")
    print(f"  Le Total des emprunts: {total_emprunts}")
    print(f"  Les Emprunts en cours: {emprunts_en_cours}")
    print(f"  Les Emprunts retournés: {emprunts_retournes}")
    print("-------------------------------------------------")

def afficher_details_emprunt(Liste_Emprunts):
    if not Liste_Emprunts :
        print("\n----------------------------------------------")
        print("        Aucun Emprunt Enregistré!        ")
        print("----------------------------------------------")
        return

    print("\n----------------------------------------------")
    print("            DÉTAILS DES EMPRUNTS       ")
    print("-----------------------------------------------")
    for i, emprunt in enumerate(Liste_Emprunts):
        status = "Retourné" if emprunt.Marquer_Support_Comme_Rendu() else "En cours"
        print(f"  #{i + 1:<3} {emprunt.support.titre}")

    try:
        choix = int(input("\nChoisir le numéro de l'emprunt (0 pour retour): "))
        if choix == 0:
            return
        if 1 <= choix <= len(Liste_Emprunts):
            emprunt = Liste_Emprunts[choix - 1]
            print("\n===========================================")
            print("                   DÉTAILS DE L'EMPRUNT      ")
            print("-------------------------------------------")
            print(f"  Support: {emprunt.support.titre}")
            print(f"  Adhérent: {emprunt.Adherent.nom} {emprunt.Adherent.prenom}")
            print(f"  Date d'emprunt: {emprunt.dateEmprunt}")
            if emprunt.estRendu():
                print(f"  Date de retour: {emprunt.dateRetour}")
            print(f"  Statut: {status}")
            print("===========================================")
        else:
            print("Le Numéro d'emprunt invalide!!")
    except ValueError:
        print("Le choix est invalide !!")


def retourner_emprunt(Liste_Emprunts):
    if not Liste_Emprunts:
        print("\n---------------------------------------------")
        print("        Aucun emprunt enregistré!        ")
        print("---------------------------------------------")
        return

    print("\n---------------------------------------------")
    print("                   Gestion des retours        ")
    print("---------------------------------------------")
    print("  1. 🔄 Retourner un emprunt")
    print("  2. 📅 Modifier une date de retour")
    print("  3. 📋 Voir tous les emprunts")
    print("  0. 🚪 Quitter")
    print("---------------------------------------------")

    choix = input("\nVotre choix : ")

    if choix == "1":
        print("\n-------------------------------------------")
        print("               Tous les emprunts        ")
        print("-------------------------------------------")
        for emprunt in Liste_Emprunts:
            statu = "Retour prévu: " + str(emprunt.dateRetour) if emprunt.dateRetour else " En cours"
            dispo = "✅ Disponible" if emprunt.Support.estDiponible() else "❌ Indisponible"
            print(f" {emprunt.id} {emprunt.Support.Titre:<45}")
            print(f" Adhérent: {emprunt.Adherent.nom} {emprunt.Adherent.prenom}")
            print(f" Statut: {statu}")
            print("-------------------------------------------")
        print("--------------------------------------------")

        try:
            emprunt_id = input("\nEntrez l'ID de l'emprunt  : ")
            emprunt = next((e for e in Liste_Emprunts if e.id == emprunt_id), None)

            if emprunt:
                print("\nDate de retour :")
                print("1. Aujourd'hui")
                print("2. Autre date")
                choix_date = input("Votre choix (1-2) : ")

                if choix_date == "1":
                    date_retour = datetime.date.today()
                elif choix_date == "2":
                    while True:
                        try:
                            date_str = input("Entrez la date de retour (YYYY-MM-DD) : ")
                            date_retour = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                            if date_retour < emprunt.dateEmprunt:
                                print("❌ La date de retour ne peut pas être antérieure à la date d'emprunt!")
                                continue
                            break
                        except ValueError:
                            print("❌ Format de date invalide! Utilisez le format YYYY-MM-DD")
                else:
                    print("❌ Choix invalide!")
                    return

                emprunt.retourner(date_retour)
                statu = "Disponible" if emprunt.Support.est_Diponible() else "Non Disponible"
                print(f"✅ Date de retour mise à jour avec succès! Le support est maintenant {statu}.")
            else:
                print("❌ ID d'emprunt invalide!")
        except ValueError:
            print("❌ Entrée invalide!")

    elif choix == "2":
        print("\n--------------------------------------------------")
        print("             Tous les emprunts        ")
        print("----------------------------------------------------")
        for i, emprunt in enumerate(Liste_Emprunts):
            status = " Retour prévu: " + str(emprunt.dateRetour) if emprunt.dateRetour else "En cours"
            dispo = " Disponible" if emprunt.Support.est_Diponible() else " Non Disponible"
            print(f" #{i + 1:<3} {emprunt.Support.Titre}")
            print(f" Adhérent: {emprunt.Adherent.Nom} {emprunt.Adherent.Prenom}")
            print(f" Statut: {status}")
            if i < len(Liste_Emprunts):
                print("----------------------------------------------")
        print("-----------------------------------------------------")

        try:
            emprunt_index = int(input("\nChoisir le numéro de l'emprunt à modifier : "))
            if 0 <= emprunt_index < len(Liste_Emprunts):
                emprunt = Liste_Emprunts[emprunt_index]

                while True:
                    try:
                        date_str = input("Nouvelle date de retour (YYYY-MM-DD) : ")
                        nouvelle_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                        if nouvelle_date < emprunt.dateEmprunt:
                            print(" La date de retour ne peut pas être antérieure à la date d'emprunt!")
                            continue
                        emprunt.retourner(nouvelle_date)
                        statu = "disponible" if emprunt.Support.est_Diponible() else " Non disponible"
                        print(f" Date de retour modifiée avec succès! Le support est maintenant {statu}.")
                        break
                    except ValueError:
                        print(" Format de date invalide! Utilisez le format YYYY-MM-DD")
            else:
                print("Numéro d'emprunt invalide! ")
        except ValueError:
            print("                 Entrée invalide!                         ")

    elif choix == "3":
        # Voir tous les emprunts
        print("\n-------------------------------------------------")
        print("             Tous les emprunts        ")
        print("---------------------------------------------------")
        for i, emprunt in enumerate(Liste_Emprunts):
            statu = "Retour prévu: " + str(emprunt.dateRetour) if emprunt.dateRetour else " En cours"
            dispo = "Disponible" if emprunt.Support.est_Diponible() else " Non Disponible"
            print(f" #{i + 1:<3} {emprunt.Support.titre}")
            print(f" Adhérent: {emprunt.Adherent.nom} {emprunt.Adherent.prenom}")
            print(f" Statut: {statu}")
            if i < len(Liste_Emprunts):
                print("-------------------------------------------")
        print("----------------------------------------------------------")

    else:
        print("                 Entrée invalide!                         ")


def afficher_tableau(headers, data):
    widths = [len(str(header)) for header in headers]
    for row in data:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))

    # Créer la ligne de séparation
    separator = "+" + "+".join("-" * (w + 2) for w in widths) + "+"

    # Afficher l'en-tête
    print(separator)
    header_str = "|"
    for header, width in zip(headers, widths):
        header_str += f" {str(header):<{width}} |"
    print(header_str)
    print(separator)

    # Afficher les données
    for row in data:
        row_str = "|"
        for cell, width in zip(row, widths):
            row_str += f" {str(cell):<{width}} |"
        print(row_str)

    print(separator)


def afficher_emprunts_en_cours(Liste_Emprunts):
    print("\n------------------------------------------")
    print("          EMPRUNTS EN COURS              ")
    print("----------------------------------------------")

    emprunts_en_cours = [em for em in Liste_Emprunts if not em.Marquer_Support_Comme_Rendu()]
    if emprunts_en_cours:
        headers = ["ID", "Support", "Adhérent", "Date emprunt", "Date retour max"]
        data = [
            [
                em.id,
                em.Support.Titre,
                f"{em.Adherent.nom} {em.Adherent.prenom}",
                em.DateEmprunt,
                em.DateRetourMaximale
            ]
            for em in emprunts_en_cours
        ]
        afficher_tableau(headers, data)
    else:
        print("Aucun emprunt en cours")


def afficher_emprunts_retard(Liste_Emprunts):
    print("\n-------------------------------------------------")
    print("          L'emprunt est en retard               ")
    print("----------------------------------------------------")

    aujourd_hui = datetime.date.today()

    Liste_Emprunts_retard = [
        em for em in Liste_Emprunts
        if not em.estRendu() and aujourd_hui > em.DateRetourMaximale
    ]

    if Liste_Emprunts_retard:
        headers = ["ID", "Support", "Adhérent", "Date emprunt", "Date retour max", "Jours retard"]
        data = [
            [
                em.id,
                em.Support.titre,
                f"{em.Adherent.nom} {em.Adherent.prenom}",
                em.dateEmprunt,
                em.dateRetour_max,
                (aujourd_hui - em.dateRetour_max).days
            ]
            for em in Liste_Emprunts_retard
        ]
        afficher_tableau(headers, data)
    else:
        print("Aucun emprunt en retard")


def afficher_tous_emprunts(Liste_Emprunts):
    print("\n----------------------------------------------")
    print("        LISTE  DES EMPRUNTS       ")
    print("--------------------------------------------")

    if Liste_Emprunts:
        headers = ["ID", "Support", "Adhérent", "Date emprunt", "Date retour max", "Statut"]
        data = [
            [
                em.id,
                em.Support.titre,
                f"{em.Adherent.nom} {em.Adherent.nrenom}",
                em.dateEmprunt,
                em.dateRetour_max,
                "En retard" if (not em.dateRetour and datetime.date.today() > em.dateRetour_max)
                else "En cours" if not em.dateRetour
                else "Retourné le " + str(em.dateRetour)
            ]
            for em in Liste_Emprunts
        ]
        afficher_tableau(headers, data)
    else:
        print("Aucun emprunt enregistré")


def afficher_emprunts_adherent(Liste_Emprunts, id_adherent):
    print("\n-----------------------------------------------------")
    print(f"     EMPRUNTS DE L'ADHÉRENT {id_adherent}    ")
    print("---------------------------------------------------------")

    emprunts_adherent = [em for em in Liste_Emprunts if em.Adherent.id == id_adherent]
    if emprunts_adherent:
        headers = ["Support", "Date emprunt", "Date retour max", "Statut"]
        data = [
            [
                em.Support.Titre,
                em.DateEmprunt,
                em.DateRetourMaximale,
                "Retourné" if em.DateRetour else "En cours"
            ]
            for em in emprunts_adherent
        ]
        afficher_tableau(headers, data)
    else:
        print("Aucun emprunt trouvé pour cet adhérent")


def afficher_emprunts_support(Liste_Emprunts, id_support):
    print("\n------------------------------------------------")
    print(f"      EMPRUNTS DU SUPPORT {id_support}     ")
    print("-----------------------------------------------------")

    Liste_Emprunts_support = [em for em in Liste_Emprunts if em.Support.id_support == id_support]
    if Liste_Emprunts_support:
        headers = ["Adhérent", "Date emprunt", "Date retour max", "Statut"]
        data = [
            [
                f"{em.Adherent.nom} {em.Adherent.prenom}",
                em.dateEmprunt,
                em.DateRetour_max,
                "Retourné" if em.dateRetour else "En cours"
            ]
            for em in Liste_Emprunts_support
        ]
        afficher_tableau(headers, data)
    else:
        print("Aucun emprunt trouvé pour ce support")


def creer_emprunt(emprunts, supports):
    print("\n------------------------------------------")
    print("          CRÉATION D'UN EMPRUNT          ")
    print("-------------------------------------------")

    try:
        # Saisie des informations de l'adhérent
        print("\nInformations de l'adhérent:")
        id_adherent = input("ID Adhérent: ")
        nom = input("Nom: ")
        prenom = input("Prénom: ")

        adherent = Adherent(
            id=id_adherent,
            Nom=nom,
            Prenom=prenom,
        )

        # Saisie des informations du support
        print("\nInformations du support:")
        type_support = input("Type de support (1: Livre, 2: CD-ROM, 3: Magazine): ")
        id_support = input("ID Support: ")
        titre = input("Titre: ")

        if type_support == "1":
            auteur = input("Auteur: ")
            nb_pages = int(input("Nombre de pages: "))
            support = Livre(id_support, titre, True, auteur, nb_pages)
            supports.append(support)
        elif type_support == "2":
            editeur = input("Éditeur: ")
            capacite = int(input("Capacité (Mo): "))
            support = CD_ROM(id_support, titre, True, capacite, editeur)
            supports.append(support)
        elif type_support == "3":
            numero = input("Numéro de publication: ")
            date_pub = input("Date de publication (YYYY-MM): ")
            support = Magazine(id_support, titre, True, numero, date_pub)
            supports.append(support)
        else:
            raise ValueError("Type de support invalide")

        # Saisie de la date d'emprunt
        print("\n-----------------------------------------------")
        print("        DATE D'EMPRUNT")
        print("-------------------------------------------")
        print("1. Utiliser la date d'aujourd'hui")
        print("2. Autre date")
        print("-------------------------------------------")

        choix_date_emprunt = input("\nVotre choix (1 ou 2): ")

        if choix_date_emprunt == "2":
            try:
                date_str = input("Date d'emprunt (YYYY-MM-DD): ")
                date_emprunt = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                if date_emprunt > datetime.date.today():
                    raise ValueError("La date d'emprunt ne peut pas être dans le futur")
            except ValueError as e:
                print(f"Erreur: {e}")
                print("Utilisation de la date d'aujourd'hui")
                date_emprunt = datetime.date.today()
        else:
            date_emprunt = datetime.date.today()

        # Définition de la date maximale de retour
        print("\n---------------------------------------------")
        print("     DATE MAXIMALE DE RETOUR     ")
        print("-------------------------------------------")
        print("1. Entrer le nombre de jours maximum")
        print("2. Entrer directement la date maximale")
        print("3. Utiliser par défaut")
        print("-------------------------------------------")

        choix_date = input("\nVotre choix (1, 2 ou 3): ")

        # Création de l'emprunt
        id_emprunt = f"E{len(emprunts) + 1}"
        date_retour_max = None

        if choix_date == "1":
            try:
                nb_jours = int(input("Nombre de jours maximum avant retour: "))
                if nb_jours <= 0:
                    raise ValueError("Le nombre de jours doit être positif")
                date_retour_max = date_emprunt + datetime.timedelta(days=nb_jours)
            except ValueError as e:
                print(f"Erreur: {e}")
                print("Utilisation du délai par défaut (14 jours)")
                date_retour_max = date_emprunt + datetime.timedelta(days=14)

        elif choix_date == "2":
            try:
                date_str = input("Date maximale de retour (YYYY-MM-DD): ")
                date_retour_max = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                if date_retour_max <= date_emprunt:
                    raise ValueError("La date de retour doit être postérieure à la date d'emprunt")
            except ValueError as e:
                print(f"Erreur: {e}")
                print("Utilisation du délai par défaut (14 jours)")
                date_retour_max = date_emprunt + datetime.timedelta(days=14)

        else:  # choix_date == "3" ou autre
            print("Utilisation du délai par défaut (14 jours)")
            date_retour_max = date_emprunt + datetime.timedelta(days=14)

        nouvel_emprunt = Emprunt(id_emprunt, support, adherent, date_emprunt, None)
        nouvel_emprunt.DateRetourMaximale = date_retour_max
        emprunts.append(nouvel_emprunt)

        print("\n===========================================")
        print("Emprunt créé avec succès!")
        print(f"ID Emprunt: {id_emprunt}")
        print(f"Date d'emprunt: {date_emprunt}")
        print(f"Date maximale de retour: {date_retour_max}")
        print("===========================================")

    except ValueError as e:
        print(f"\n Erreur: {e}")
    except Exception as e:
        print(f"\n Erreur inattendue: {e}")


def main():
    Liste_Emprunts = []
    Liste_Supports = []

    while True:
        afficher_menu()
        choix = input("\nVotre choix : ")

        if choix == "1":
            # Modifier cette ligne pour passer la liste des supports
            creer_emprunt(Liste_Emprunts, Liste_Supports)

        elif choix == "2":
            # Retourner un emprunt
            retourner_emprunt(Liste_Emprunts)

        elif choix == "3":
            # Afficher les détails d'un emprunt
            afficher_details_emprunt(Liste_Emprunts)

        elif choix == "4":
            # Afficher les emprunts en cours
            afficher_emprunts_en_cours(Liste_Emprunts)

        elif choix == "5":
            # Afficher les emprunts d'un adhérent
            id_adherent = input("Entrez l'ID de l'adhérent : ")
            afficher_emprunts_adherent(Liste_Emprunts, id_adherent)

        elif choix == "6":
            # Afficher les emprunts d'un support
            id_support = input("Entrez l'ID du support : ")
            afficher_emprunts_support(Liste_Emprunts, id_support)

        elif choix == "7":
            Afficher_Statistiques(Liste_Emprunts)

        elif choix == "8":
            afficher_tous_emprunts(Liste_Emprunts)

        elif choix == "9":
            Afficher_Emprunts(Liste_Emprunts)

        elif choix == "10":
            Afficher_Supports(Liste_Supports)

        elif choix == "0":
            print("\n -----------------------------------------")
            print("               Au revoir!                 ")
            print("------------------------------------------")
            break

        else:
            print("\nChoix invalide! Veuillez réessayer.")



class Bibliotheque:
    def __init__(self,nomBibliotheque,Adress,Tele,Email):
        self.__NomBibliotheque = nomBibliotheque
        self.__Adress = Adress
        self.__Tele = Tele
        self.__Email = Email
        self.Liste_Adherent = []
        self.Liste_Support = []
        self.Liste_Emprunt = []

    @property
    def NomBibliotheque(self):
        return self.__NomBibliotheque

    @NomBibliotheque.setter
    def NomBibliotheque(self,value):
        if isinstance(value,str):
            self.__NomBibliotheque = value
        else:
            raise ValueError("Nom de bibliotheque invalide")

    @property
    def Adress(self):
        return self.__Adress

    @Adress.setter
    def Adress(self,value):
        if isinstance(value,str):
            self.__Adress = value
        else :
            raise ValueError("Adress invalide")

    @property
    def Tele(self):
        return self.__Tele

    @Tele.setter
    def Tele(self,value):
        if isinstance(value,str):
            self.__Tele = value
        else:
            raise ValueError("Tele invalide")

    @property
    def Email(self):
        return self.__Email

    @Email.setter
    def Email(self,value):
        if isinstance(value,str):
            self.__Email = value
        else:
            raise ValueError("Email invalide")

    def Ajouter_Adherent(self,adherent:Adherent):
        if isinstance(adherent,Adherent):
          return  self.Liste_Adherent.append(adherent)
        else:
            return ("adherent invalide")

    def Ajouter_Support(self,support:Support):
        if isinstance(support,Support):
            return self.Liste_Support.append(support)
        else :
            return ("support invalide")

    def Ajouter_Emprunt(self,emprunt : Emprunt):
        if isinstance(emprunt,Emprunt):
            return self.Liste_Emprunt.append(emprunt)
        else:
            return ("Emprunt invalide")

    def Rechercher_Adherent(self):
        print("1_Rechercher adherent par nom ou prenom")
        print("2_Recherche  adherent Payant par CIN ")
        print("3_Rechercher  adherent Gratuit par Code")

        try :
            choix = int(input("Donner un choix (1/2/3) : ")

             if choix == "1" :
               Nom = input("donner le nom : ").lower()
               Prenom = input("donner le prenom : ").lower()




