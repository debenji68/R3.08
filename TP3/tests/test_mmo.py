import pytest
from src.mmo import Personnage, Guerrier, Mage, Joueur

def test_perso_defaut():
    p = Personnage("Hero")
    assert p.pseudo == "Hero"
    assert p.niveau == 1
    assert p.pv == 1
    assert p.init == 1


def test_perso_niveau():
    p = Personnage("Hero", niveau=5)
    assert p.pseudo == "Hero"
    assert p.niveau == 5
    assert p.pv == 5
    assert p.init == 5


def test_perso_degats():
    p = Personnage("Hero", niveau=3)
    assert p.degats() == 3


def test_perso_egalite():
    p1 = Personnage("Hero", niveau=5)
    p2 = Personnage("Hero", niveau=5)
    p3 = Personnage("Autre", niveau=5)
    p4 = Personnage("Hero", niveau=2)

    assert p1 == p2
    assert p1 != p3
    assert p1 != p4


def test_perso_soigner():
    p = Personnage("Hero", niveau=10)
    p.soigner()
    assert p.pv == 10

def test_guerrier_statistiques():
    g = Guerrier("armin", niveau=3)
    assert g.pseudo == "armin"
    assert g.niveau == 3
    assert g.pv == 28
    assert g.init == 18
    assert g.degats() == 6