score =raw_input("Enter Score:")
try:
    h=float(score)
    if h > 1:
        print("Geef getal onder 1")
    elif h<= 0:
        print("Geef getal boven de 0")
    elif h>= 0.9:
        print("A")
    elif h>= 0.8:
        print("B")
    elif h>= 0.7:
        print("C")
    elif h>= 0.6:
        print("D")
    elif h< 0.6:
        print("F")
except:
    fout=-1
    print("Geef getal op")




