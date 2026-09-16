class Personnage:
    """
    classe personnage représentant un avatar du joueur
    """
    def __init__(self, pseudo :str, niveau=1):
        """
        Args:
            pseudo: (str) nom du personnage
            niveau: (int) niveau du personnage
        """
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__pv = niveau
        self.__init = niveau


    @property
    def init(self):
        return self.__init


    @property
    def pv(self):
        return self.__pv


    @property
    def niveau(self):
        return self.__niveau


    def attaque(self,opposant:Personnage)->None:
        """
        fonction permettant de lancer une attaque contre un adversaire
        Args:
            opposant: (Personnage) personnage qui va être l'opposant de l'attaque

        Returns: None

        """
        degats_de_self = self.degats()
        degats_de_autre = autre.degats()

        if opposant.__init < self.__init:
            opposant.__pv -= degats_de_self
            if opposant.__pv > 0:
                self.__pv -= degats_de_autre
        elif opposant.__init == self.__init:
            opposant.__pv -= degats_de_self
            self.__pv -= degats_de_autre
        else:
             self.__pv -= degats_de_autre
            if self.__pv > 0:
                opposant.__pv -= degats_de_self


    def combat(self,opposant:Personnage)->str:
        """
        fonction permettant de faire un combat entre 2 personnages
        Args:
            opposant: (Personnage) Personnage qui va s'opposer a un autre personnage

        Returns: (str) renvoie les 2 adversaire du combat

        """
        while self.__pv > 0 and opposant.__pv > 0:
            self.attaque(opposant)
            print(f"{self.__pseudo} ({self.__pv} PV) vs {opposant.__pseudo} ({opposant.__pv} PV)")


    def soigner(self)->None:
        """
        fonction permettant de soigner les personnages
        Returns: None

        """
        self.__pv = self.__niveau

    def degats(self):
        return self.__niveau


class Guerrier(Personnage):
    def __init__(self, pseudo, niveau=1):
        super().__init__(pseudo, niveau)
        self.__pv = self.niveau * 8 + 4
        self.__init = self.niveau * 4 + 6

    def degats(self):
        return self.niveau * 2


class Mage(Personnage):
    def __init__(self, pseudo, niveau=1):
        super().__init__(pseudo, niveau)
        self.pv = niveau * 5 + 10
        self.init = niveau * 6 + 4
        self.__mana = niveau * 5


    def degats(self):
        if self.__mana >= 4:
            self.__mana -= 4
            return self.niveau * 3
        return self.niveau


class Joueur:
    def __init__(self, nom, max_personnages):
        self.__nom = nom
        self.__max_personnages = max_personnages
        self.__personnages = []


    def ajouter_personnage(self, personnage):
        if len(self.__personnages) < self.__max_personnages:
            self.__personnages.append(personnage)
