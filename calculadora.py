#     DESCONSTRUINDO A MATÉRIA
# Por: Luiza Valezim Augusto Pinto
# Data: 12/04/2021

# phi = m_a/V_c = (n*A)/V_c*N_a

# sendo:
# m_a = massa de átomos unitária
# n = número de átomos na célula unitária
# A = peso atômico
# V_C = volume da célula unitária
# N_a = Número de Avogadro (6.023*10^23 átomos/mol)

# Importando bibliotecas
import math
import scipy
from scipy import constants

avogadro = 6.023*math.pow(10,23)

estrutura = input("Qual é o tipo de estrutura cristalina? (CFC ou CCC) ")

if estrutura == "CFC":
    n = 4
elif estrutura == "CCC":
    n = 2

pergunta = input("Quer saber o que? (densidade, raio atômico, peso atômico) ")


# -------------------- DENSIDADE -----------------------
if pergunta == "densidade":
    A = float(input("Qual o peso atômico? "))
    raio = float(input("Qual o raio atômico? "))
    a = raio*(10**(-7))

    # Cúbica Face Centrada (CFC)
    if estrutura == "CFC":
        V_c = (2*a*math.sqrt(2))**3

    # Cúbica de Corpo Centrado (CCC)
    if estrutura == "CCC":
        V_c = (4*a/math.sqrt(3))**3

    phi = (n*A)/(avogadro*V_c)
    print("A densidade do {0} é de {1} g/cm^3".format(estrutura, phi))



# -------------------- RAIO ATÔMICO -----------------------
if pergunta == "raio atômico":
    A = float(input("Qual o peso atômico? "))
    phi = float(input("Qual a densidade? "))
    
    # Cúbica Face Centrada (CFC)
    if estrutura == "CFC":
        a = ((n*A)/(avogadro*phi*16*math.sqrt(2)))**(1/3)
    
    # Cúbica de Corpo Centrado (CCC)
    if estrutura == "CCC":
        a = ((n*A*3*math.sqrt(3))/(avogadro*phi*64))**(1/3)

    print("O raio atômico é de {0} m".format(a))