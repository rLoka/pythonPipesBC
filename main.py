import subprocess
import random

def unos():
    rezultat = random.randint(0, 10)
    operacija = input(str(rezultat) + "=")
    return (rezultat, operacija)

print("Unesite operaciju u obliku X+Y, za prekid unesite Q")

while True:
    izlaz = unos()
    if izlaz[1] == "Q" or izlaz[1] == "q":
        break
    else:
        bcProces = subprocess.Popen("bc", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = bcProces.communicate((izlaz[1] + "\n").encode("utf-8"))
        if stderr != b'':
            print("NEISPRAVAN IZRAZ")
        elif(izlaz[0] == int(stdout)):
            print("ISPRAVNO")
        else:
            print("NESIPRAVNO, tocan odgovor je " + stdout.decode("utf-8"))

