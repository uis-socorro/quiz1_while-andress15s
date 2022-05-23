print("---------------------------------------")
print("---------meses para el negocio---------")
print("---------------------------------------")

#input 

c1 = int(input("digite el capital: "))
c2 = int(input("digite el capital: "))
c3 = int(input("digite el valor del negocio: "))
CU = 0
CP = c1
CJ = c2
CU = CP + CJ
M = 0

while CU <= c3 : 
    CP = (0.03*CP) + CP
    CJ = (0.04*CJ) + CJ
    CU = CU = CP + CJ
    M = M + 1

print("faltan " + str(M) + " para reunir el monto")