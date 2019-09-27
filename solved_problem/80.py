stdio = []
while True:
    try:
        stdio.append(input())
    except:
        break
stdio.pop(0)
for i in stdio:
    i = int(i)
    s = "snoopy wins the game!" if i % 14 == 0 else "flymouse wins the game!"
    print(s)