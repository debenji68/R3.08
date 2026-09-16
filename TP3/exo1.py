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

    def attaque(self,opposant:Personnage)->None:
        """
        Args:
            opposant: (Personnage) personnage qui va être l'opposant de l'attaque

        Returns: None

        """
        if opposant.__init < self.__init:
            opposant.__pv -= self.__niveau
            if opposant.__pv > 0:
                self.__pv -= opposant.__niveau
        elif opposant.__init == self.__init:
            opposant.__pv -= self.__niveau
            self.__pv -= opposant.__niveau
        else:
             self.__pv -= opposant.__niveau
            if self.__pv > 0:
                opposant.__pv -= self.__niveau


    def combat(self,opposant:Personnage)->None:
        while self.__pv > 0 and opposant.__pv > 0:
            self.attaque(autre)
            print(f"{self.__pseudo} ({self.__pv} PV) vs {autre.__pseudo} ({autre.__pv} PV)")