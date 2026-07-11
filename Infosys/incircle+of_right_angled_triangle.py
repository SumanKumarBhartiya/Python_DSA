PI = 3.14159265

def area_inscribed(P, B, H):
    return ((P + B - H)*(P + B - H)*(PI / 4))


P = 3
B = 4
H = 5
print(area_inscribed(P, B, H))