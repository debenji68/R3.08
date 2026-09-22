from exo1 import Personnage, Guerrier, Mage, Joueur

def test_pero_defaut():
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


# ==============================================================================
# 2. TESTS DES SOUS-CLASSES GUERRIER ET MAGE
# ==============================================================================

def test_guerrier_statistiques():
    # Formules Guerrier : PV = niv*8 + 4 | Init = niv*4 + 6 | Dégâts = niv*2
    g = Guerrier("Thor", niveau=3)
    assert g.pseudo == "Thor"
    assert g.niveau == 3
    assert g.pv == 28  # 3 * 8 + 4
    assert g.init == 18  # 3 * 4 + 6
    assert g.degats() == 6  # 3 * 2


def test_mage_statistiques_et_mana():
    # Formules Mage : PV = niv*5 + 10 | Init = niv*6 + 4 | Mana = niv*5
    m = Mage("Gandalf", niveau=2)
    assert m.pseudo == "Gandalf"
    assert m.niveau == 2
    assert m.pv == 20  # 2 * 5 + 10
    assert m.init == 16  # 2 * 6 + 4


def test_mage_degats_avec_et_sans_mana():
    # Niv 2 -> Mana initial = 10, Dégâts magiques = 2 * 3 = 6
    m = Mage("Gandalf", niveau=2)

    # 1ère attaque magique (Cout : 4 Mana -> reste 6)
    assert m.degats() == 6
    # 2ème attaque magique (Cout : 4 Mana -> reste 2)
    assert m.degats() == 6
    # 3ème attaque : Plus assez de mana (2 < 4), passe en dégâts physiques = niveau = 2
    assert m.degats() == 2


# ==============================================================================
# 3. TESTS DU SYSTÈME DE COMBAT ET ATTAQUES
# ==============================================================================

def test_attaque_initiative_superieure():
    # p1 a plus d'initiative que p2
    p1 = Personnage("Rapide", niveau=5)
    p2 = Personnage("Lent", niveau=2)

    p1.attaque(p2)
    # p1 frappe p2 (p2 perd 5 PV) -> p2 passe à 2 - 5 = -3 PV (mort)
    # p2 étant mort, il ne riposte pas
    assert p2.pv == -3
    assert p1.pv == 5


def test_attaque_avec_riposte():
    # p1 attaque p2, p2 survit et riposte
    p1 = Personnage("Attaquant", niveau=2)
    p2 = Personnage("Defenseur", niveau=10)  # Beaucoup de PV/Init

    # On ajuste temporairement les initiatives pour que p1 frappe en premier
    # p1 (degats=2), p2 (degats=10, pv=10)
    p1.attaque(p2)
    # Si p2 survit, il doit infliger ses dégâts à p1
    assert p2.pv == 8  # 10 - 2
    assert p1.pv == -8  # 2 - 10


def test_attaque_egalite_initiative():
    p1 = Personnage("Joueur1", niveau=3)
    p2 = Personnage("Joueur2", niveau=3)

    p1.attaque(p2)
    # Attaques simultanées
    assert p1.pv == 0  # 3 - 3
    assert p2.pv == 0  # 3 - 3


# ==============================================================================
# 4. TESTS DE LA CLASSE JOUEUR
# ==============================================================================

def test_joueur_ajout_personnage():
    j = Joueur("Alice", max_personnages=2)
    p1 = Personnage("Hero1")
    p2 = Personnage("Hero2")
    p3 = Personnage("Hero3")

    j.ajouter_personnage(p1)
    j.ajouter_personnage(p2)

    # La limite est atteinte, p3 ne doit pas être ajouté
    j.ajouter_personnage(p3)
    assert j.acces_perso_index(0) == p1
    assert j.acces_perso_index(1) == p2


def test_joueur_recherche_personnage():
    j = Joueur("Bob", max_personnages=5)
    p1 = Guerrier("Conan", niveau=3)
    p2 = Mage("Merlin", niveau=4)

    j.ajouter_personnage(p1)
    j.ajouter_personnage(p2)

    # Recherche par index, nom et instance
    assert j.acces_perso_index(0) == p1
    assert j.acces_perso_nom("Merlin") == p2
    assert j.acces_perso_avec_personnage(Guerrier("Conan", niveau=3)) == p1


def test_joueur_suppression_personnage():
    j = Joueur("Charlie", max_personnages=5)
    p1 = Personnage("P1", niveau=1)
    p2 = Personnage("P2", niveau=2)
    p3 = Personnage("P3", niveau=3)

    j.ajouter_personnage(p1)
    j.ajouter_personnage(p2)
    j.ajouter_personnage(p3)

    # Suppression par index
    j.del_perso_index(0)  # Supprime P1
    assert j.acces_perso_nom("P1") is None

    # Suppression par nom
    j.del_perso_nom("P2")
    assert j.acces_perso_nom("P2") is None

    # Suppression par instance
    j.del_perso_avec_personnage(p3)
    assert j.acces_perso_nom("P3") is None