from Cliente.classic import Classic
from Cliente.gold import Gold
from Cliente.black import Black

cliente1 = Classic("Cliente","Classic",12345678,1)
cliente2 = Gold("Cliente2","Gold",12345679,2)
cliente3 = Black("Cliente3","Black",12345670,3)

cliente1.getInfo()
print()
cliente2.getInfo()
print()
cliente3.getInfo()