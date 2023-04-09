array = []  
while True:
    number = int(input())
    if number == 0:
       break
    assert number <=30000
    array.append(number)

array.sort()
answer = None 
for element in array:
    if element % 2 == 0 and element % 10 != 2:
         answer = element 
         break 
assert answer != None 
print("ответ =", answer)