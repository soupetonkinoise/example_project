MORTE = '#FFFFFF'
VIVANTE = '#FF0000'

def creer(taille_g):
    cases = [None] * taille_g.ny
    for y in range(taille_g.ny):
        cases[y] = [0] * taille_g.nx
    return struct(cases=cases, nx=taille_g.nx, ny=taille_g.ny,
                  dim=taille_g.dim)

def init(grille):
    total = grille.nx * grille.ny
    pourcentage = random.randint(10, 50) / 100
    nb_a_placer = round(pourcentage * total)
    nb_restantes = total

    for y in range(grille.ny):
        for x in range(grille.nx):
            if random.randint(1, nb_restantes) <= nb_a_placer: 
                grille.cases[y][x] = 1
                nb_a_placer -= 1
            nb_restantes -= 1   
    return grille



     


