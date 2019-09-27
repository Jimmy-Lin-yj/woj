import math
a = list()
value = 1e-9
rate = {"inches":0.0254,"feet":0.3048,"centimeters":0.01,"cubits":0.4572,"meters":1.00}
while True:
    try:
        a.append(input())
    except:
        break
c = list()
for st in a:
    if st == "" :
        continue
    temp = st.split()
    t = float(temp[0])*rate[temp[1]]
    c.append(t)
    if  len(c) == 3:
        if abs(c[0] - c[1]) < value :
            print("Spin")
        elif abs(c[0] - 6 * c[1]) < value:
            print("Excellent")
        else:
            print("Neither")
        c = list()
        print("")
