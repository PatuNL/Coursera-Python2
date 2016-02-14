hrs =raw_input("Enter Hours:")
try:
    h=float(hrs)
    if h > 40:
        overwerk = h - 40
        betaal = (overwerk * 15.75)+420
    else:
        betaal = h * 10.5
    print betaal
except:
    fout=-1
    print("Geef getal op")




