import string
s = input()
a = string.ascii_uppercase[::-1]
upper = s
for i in a:
    if not i in upper:
        upper += i
lower = upper.lower()
while True:
    try:
        s = input()
        tmp = ""
        for i in s:
            if i.islower():
                tmp += string.ascii_lowercase[lower.index(i)]
            elif i.isupper():
                tmp += string.ascii_uppercase[upper.index(i)]
            else:
                tmp += i
        print(tmp)
    except:
        break