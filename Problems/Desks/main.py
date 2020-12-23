desks_classroom_1 = abs(int(input()))  # put your python code here
desks_classroom_2 = abs(int(input()))
desks_classroom_3 = abs(int(input()))

if desks_classroom_1 % 2 == 0:
    desks_classroom_1 = (desks_classroom_1 // 2)
else:
    desks_classroom_1 = (desks_classroom_1 // 2) + 1

if desks_classroom_2 % 2 == 0:
    desks_classroom_2 = (desks_classroom_2 // 2)
else:
    desks_classroom_2 = (desks_classroom_2 // 2) + 1

if desks_classroom_3 % 2 == 0:
    desks_classroom_3 = (desks_classroom_3 // 2)
else:
    desks_classroom_3 = (desks_classroom_3 // 2) + 1

print(desks_classroom_1 + desks_classroom_2 + desks_classroom_3)
