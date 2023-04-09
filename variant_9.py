counter = int(input())
answer = False
for _ in range(counter): 
    number = int(input())
    assert number <=30000 
    if number >= 10 and number <=99 and number <= 1000: 
        answer = True
        break

if answer :
    print("NO")
else:
    print("YES")