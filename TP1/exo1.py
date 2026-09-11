import math
class Point:
    """
    Représente un point dans un repère cartésien 2D.
    Attributes:
        x (float): L'abscisse du point.
        y (float): L'ordonnée du point.
    """
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        """
        :param x: abscisse du point (0.0 par défaut)
        :param y: ordonnée du point (0.0 par défaut)
        """
        self.__x = float(x)
        self.__y = float(y)


    def distanceCoord(self,a:float,b:float)->float:
        """
        :param a: abscisse de l'autre point
        :param b: ordonnée de l'autre point
        :return: distance entre les 2 points
        """
        return math.sqrt((self.__x - a) ** 2 + (self.__y - b) ** 2)


    def distancePoint(self, camarade: "Point") -> float:
        """:
        param camarade: l'autre objet Point
        :return: distance entre les 2 points
        """
        return self.distanceCoord(camarade.__x, camarade.__y)


    def __str__(self) -> str:
        return f"Point : ({self.__x},{self.__y})"


class Cercle:
    """Classe représentant un cercle."""

    def __init__(self, rayon: float, centre: Point=Point(0,0)):
        """Constructeur gérant l'origine par défaut ou un centre spécifié."""
        self.__rayon = float(rayon)
        self.__centre = centre


    def diametre(self) -> float:
        """Calcule le diamètre du cercle."""
        return 2 * self.__rayon

    def perimetre(self) -> float:
        """ Calcule le périmètre du cercle."""
        return 2 * math.pi * self.__rayon

    def surface(self) -> float:
        """Calcule la surface du cercle."""
        return math.pi * (self.__rayon**2)


    def est_en_intersection(self, autre: "Cercle") -> bool:
        """Vérifie l'intersection avec un autre cercle."""
        dist_centres = self.__centre.distancePoint(autre.__centre)
        return dist_centres <= self.__rayon + autre.__rayon


    def contient_point(self, p: Point) -> bool:
        """Vérifie si un Point A fait partie du cercle ."""
        return self.__centre.distancePoint(p) <= self.__rayon


class Rectangle:
    """Classe représentant un rectangle."""
    def  __init__(self, bas_gauche:Point=Point(0,0), longeur:float=1.0, hauteur:float=1.0, haut_droit:Point=None):
        """Constructeur gérant 3 modes d'instanciation :
        1. Par défaut : Point origine, longueur 1, hauteur 1.
        2. Spécification : bas-gauche (Point), longueur (float), hauteur (float).
        3. Deux points : bas-gauche (Point) et haut-droit (Point).
        """
        if haut_droit is None:
            self.__bas_gauche = bas_gauche
            self.__longeur = longeur
            self.__hauteur = hauteur
        else:
            self.__bas_gauche = bas_gauche
            self.__longeur =  - bas_gauche.__x
            self.__hauteur =


    def get_bas_gauche(self) -> Point:
        return self.bas_gauche

    def get_haut_droit(self) -> Point:
        return self.haut_droit



if __name__ == "__main__":
   point1 = Point(2,3.4)
   print(point1)
   point2 = Point(2,5)
   print(point2)
   print(point1.distancePoint(point2))
