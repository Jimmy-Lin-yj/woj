cases_no = int(input())
for i in range(cases_no):
    text = input().split()
    text[0] = text[0][0].upper() + text[0][1:]
    for i in range(1,len(text)):
        text[i] = text[i][0] + text[i][1:].lower()
    print(*text)