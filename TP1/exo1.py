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
    """Classe représentant un cercle[cite: 1]."""

    def __init__(self, rayon: float, centre: Point = None) -> None:
        """Constructeur gérant l'origine par défaut ou un centre spécifié[cite: 1]."""
        self.rayon = float(rayon)
        self.centre = centre if centre is not None else Point(0.0, 0.0)

    def diametre(self) -> float:
        """(1) Calcule le diamètre du cercle[cite: 1]."""
        return 2 * self.rayon

    def perimetre(self) -> float:
        """(2) Calcule le périmètre du cercle[cite: 1]."""
        return 2 * math.pi * self.rayon

    def surface(self) -> float:
        """(3) Calcule la surface du cercle[cite: 1]."""
        return math.pi * (self.rayon**2)

    def est_en_intersection(self, autre: "Cercle") -> bool:
        """(4) Vérifie l'intersection avec un autre cercle[cite: 1]."""
        dist_centres = self.centre.distancePoint(autre.centre)
        return dist_centres <= (self.rayon + autre.rayon)

    def contient_point(self, p: Point) -> bool:
        """(5) Vérifie si un Point A fait partie du cercle (disque)[cite: 1]."""
        return self.centre.distancePoint(p) <= self.rayon


    
if __name__ == "__main__":
   point1 = Point(2,3.4)
   print(point1)
   point2 = Point(2,5)
   print(point2)
   print(point1.distancePoint(point2))
