import os

for x in os.listdir() :
    if (".txt" in x) :
        f = open(x)
        z = f.readlines()
        for y in range(1, len(z)) :
            if ((z[y-1])[5:-1]!="" and (z[y])[5:-1]!="") :
                if (abs(int((z[y])[5:])-int((z[y-1])[5:]))>25) :
                    print(x)
