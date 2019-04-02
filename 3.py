input=input()

try:
    unit = int(input)
    billT = 0
    bill = 0

    if unit < 30:
        bill = (unit)*5
        billT = bill
    if unit < 60 and 30 <= unit:
        bill = (30*5)+(unit-30)*20
        billT = bill
    if unit < 120 and 60 <= unit:
        bill = (30*5)+(30*20)+(unit-60)*150
        billT = bill
    if unit < 200 and 120 <= unit:
        bill = (30*5)+(30*20)+(60*150)+(unit-120)*150
        billT = bill
    if unit > 200:
        bill = (30*5)+(30*20)+(60*150)+(80*150)+(unit-200)*1000
        billT = bill


    print(' If the amount of units consumed is ',unit,' Charge = ',billT)
except ValueError:
   print("ERROR! Please enter a numerical value")