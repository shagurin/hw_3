sum = float(input("Сумма вклада: "))
sum_after = float(input("Желаемая сумма: "))

import sys
if sum>sum_after:
    print("Так нельзя")
    sys.exit()

rate = float(input("Процентная ставка: "))
term=0

while sum<sum_after:
    sum = sum + int(sum*(rate/100))
    term=term+1
print("Срок: ", term)
