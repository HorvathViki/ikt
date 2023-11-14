csapat1 = input("Mi az egyik csapat neve? ")
pontsz1 = input("Hány pontot szereztek? ")
pontsz1 = int(pontsz1)
csapat2 = input("Mi a másik  csapat neve? ")
pontsz2 = input("Hány pontot szereztek? ")
pontsz2 = int(pontsz2)
merkozes = print(f"Az egyik csapat neve:{csapat1}, 
szerzet pontjaik:{pont1}")
merkozes1 = print(f"A másik cspat neve: {csapat2},
szerzet pontjaik {pont2}")
osszecsapas = print (f"Az összes eredménye : 
{csapat1} - {csapat2} {pont1} : {pont2}")
if pontsz1 > pontsz2 :
    print(f"A {csapat1} nyertek ")
elif pontsz1 < pontsz2 :
    print(f"A {csapat2} nyertek")
else :
    print(f"Ezt nem tudom értelmezni")
