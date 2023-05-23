x = int(input())
if x % 4 != 0:
    print("Обычный")
elif x % 100 == 0:
    if x % 400 == 0:
        print("Високостный")
    else:
        print("Обычный")
else:
    print("Високостный")