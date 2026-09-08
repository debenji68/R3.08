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

