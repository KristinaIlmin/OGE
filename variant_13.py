counter = int(input())
answer = False
for _ in range(counter):
    number = int(input())
    if number % 3 == 0 and number <= 1000:
        answer = True
        break

if answer :
    print("YES")
else:
    print("NO")