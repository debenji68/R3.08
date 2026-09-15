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
        """
        :param camarade: l'autre objet Point
        :return: distance entre les 2 points
        """
        return self.distanceCoord(camarade.__x, camarade.__y)


    def __str__(self) -> str:
        """
        Returns: affichage sous forme de chaîne de carcatère
        """
        return f"Point : ({self.__x},{self.__y})"


    def get_x(self) -> float:
        """
        Returns: récupère la valeur x
        """
        return self.__x


    def get_y(self) -> float:
        """
        Returns: récupère la valeur y
        """
        return self.__y


class Cercle:
    """Classe représentant un cercle."""

    def __init__(self, rayon: float, centre: Point=Point(0,0)):
        """
        Constructeur gérant l'origine par défaut ou un centre spécifié.
        :param rayon: l'abscisse du cercle
        :param centre: Point représentant le centre du cercle
        """
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
        """
        Vérifie l'intersection avec un autre cercle.
        :param autre: Cercle
        """
        dist_centres = self.__centre.distancePoint(autre.__centre)
        return dist_centres <= self.__rayon + autre.__rayon


    def contient_point(self, p: Point) -> bool:
        """
        Vérifie si un Point A fait partie du cercle .
        :param p: Point
        """
        return self.__centre.distancePoint(p) <= self.__rayon


class Rectangle:
    """Classe représentant un rectangle."""
    def  __init__(self, bas_gauche:Point=Point(0,0), longeur:float=1.0, hauteur:float=1.0, haut_droit:Point=None):
        """Constructeur gérant 3 modes d'instanciation :
        1. Par défaut : Point origine, longueur 1, hauteur 1.
        2. Spécification : bas-gauche (Point), longueur (float), hauteur (float).
        3. Deux points : bas-gauche (Point) et haut-droit (Point).
        :param bas_gauche: Point du rectangle
        :param longeur: longueur du rectangle
        :param hauteur: hauteur du rectangle
        :param haut_droit: Point du rectangle
        """
        if haut_droit is None:
            self.__bas_gauche = bas_gauche
            self.__longeur = longeur
            self.__hauteur = hauteur
        else:
            self.__bas_gauche = bas_gauche
            self.__longeur = haut_droit.get_x() - bas_gauche.get_x()
            self.__hauteur = haut_droit.get_y() - bas_gauche.get_y()


    def surface(self) -> float:
        """Calcule la surface"""
        return self.__longeur * self.__hauteur

    def perimetre(self) -> float:
        """Calcule le périmètre."""
        return 2 * (self.__longeur + self.__hauteur)


    @property
    def bas_gauche(self) -> Point:
        """
        Returns: renvoie la valeur du point bas gauche
        """
        return self.__bas_gauche


    @property
    def bas_droit(self) -> Point:
        """
        Returns: renvoie la valeur du point bas droit
        """
        return Point(self.__bas_gauche.get_x() + self.__longeur, self.__bas_gauche.get_y())


    @property
    def haut_gauche(self) -> Point:
        """
        Returns: renvoie la valeur du point haut gauche
        """
        return Point(self.__bas_gauche.get_x(), self.__bas_gauche.get_y() + self.__hauteur)


    @property
    def haut_droit(self) -> Point:
        """
        Returns: renvoie la valeur du point haut droit
        """
        return Point(self.__bas_gauche.get_x() + self.__longeur, self.bas_gauche.get_y() + self.__hauteur)


    def contient_point(self, p: Point) -> bool:
        """
        Vérifie si un Point est situé dans le rectangle.
        :param p: Point
        """
        if p.get_x() >= self.bas_gauche.get_x() and p.get_x() <= self.bas_droit.get_x():
            if p.get_y() >= self.bas_gauche.get_y() and p.get_y() <= self.haut_gauche.get_y():
                return True
            else:
                return False
        else:
            return False









def main() -> None:
    """Méthode principale de test exécutée uniquement si le fichier est le script principal. Généré par IA"""

    print("=" * 40)
    print(" 1. TESTS DE LA CLASSE POINT ")
    print("=" * 40)
    p_orig = Point()
    p1 = Point(3.0, 4.0)
    print(f"Point origine par défaut : {p_orig}")
    print(f"Point p1 créé : {p1}")
    print(
        f"Distance de p_orig aux coords (3.0, 4.0) : {p_orig.distanceCoord(3.0, 4.0)}"
    )
    print(f"Distance entre p_orig et p1 (objet) : {p_orig.distancePoint(p1)}")

    print("\n" + "=" * 40)
    print(" 2. TESTS DE LA CLASSE CERCLE ")
    print("=" * 40)
    c1 = Cercle(5.0)  # Origine par défaut, rayon 5
    c2 = Cercle(3.0, Point(4.0, 0.0))  # Centre (4,0), rayon 3
    print(f"Cercle c1 (rayon 5 à l'origine) :")
    print(f"  - Diamètre : {c1.diametre()}")
    print(f"  - Périmètre : {c1.perimetre():.2f}")
    print(f"  - Surface : {c1.surface():.2f}")
    print(f"c1 est-il en intersection avec c2 ? {c1.est_en_intersection(c2)}")
    print(f"Le point p1(3,4) fait-il partie de c1 ? {c1.contient_point(p1)}")

    print("\n" + "=" * 40)
    print(" 3. TESTS DE LA CLASSE RECTANGLE ")
    print("=" * 40)
    # Mode 1 : par défaut
    r_defaut = Rectangle()
    # Mode 2 : bas-gauche, longueur, hauteur
    r_custom = Rectangle(Point(1.0, 1.0), 4.0, 2.0)
    # Mode 3 : bas-gauche et haut-droit
    r_2pts = Rectangle(Point(0.0, 0.0), Point(5.0, 5.0))

    print(f"Rectangle r_custom (Bas-Gauche: {r_custom.bas_gauche}, L=4, H=2) :")
    print(f"  - Surface : {r_custom.surface()}")
    print(f"  - Périmètre : {r_custom.perimetre()}")

    # Accès direct aux objets Point du rectangle :
    print("  - Positions des 4 coins (objets Point) :")
    print(f"    * Bas-Gauche  : {r_custom.bas_gauche}")
    print(f"    * Bas-Droit   : {r_custom.bas_droit}")
    print(f"    * Haut-Gauche : {r_custom.haut_gauche}")
    print(f"    * Haut-Droit  : {r_custom.haut_droit}")

    # Tests de présence d'un point
    pt_interieur = Point(2.0, 2.0)
    pt_exterieur = Point(10.0, 10.0)
    print(
        f"  - Contient {pt_interieur} ? {r_custom.contient_point(pt_interieur)}"
    )
    print(
        f"  - Contient {pt_exterieur} ? {r_custom.contient_point(pt_exterieur)}"
    )

    print("\n" + "=" * 40)
    print(" 4. TESTS DE LA CLASSE TRIANGLE RECTANGLE ")
    print("=" * 40)
    tr1 = TriangleRectangle(3.0, 4.0)  # Angle droit à l'origine (0,0)
    tr_iso = TriangleRectangle(5.0, 5.0, Point(2.0, 2.0))

    print(f"Triangle TR1 (côtés 3 et 4 à l'origine) :")
    print(f"  - Hypoténuse : {tr1.hypotenuse()}")
    print(f"  - Périmètre  : {tr1.perimetre()}")
    print(f"  - Surface    : {tr1.surface()}")
    print(f"  - Est isocèle ? {tr1.est_isocele()}")

    print(f"Triangle TR_ISO (côtés 5 et 5) :")
    print(f"  - Est isocèle ? {tr_iso.est_isocele()}")


if __name__ == "__main__":
    main()
