todayY=input("Enter Today Year:")
todayM=input("Enter Today Month:")
todayD=input("Enter Today Day:")
dobY=input("Enter DOB Year:")
dobM=input("Enter DOB Month:")
dobD=input("Enter DOB Day:")

try:
    todayY = int(todayY)
    todayM = int(todayM)
    todayD = int(todayD)
    dobY = int(dobY)
    dobM = int(dobM)
    dobD = int(dobD)

    tdays = todayD+(30*todayM)+(365*todayY)
    ddays = dobD+(30*dobM)+(365*dobY)

    rdays=tdays-ddays
    Year = int(rdays/365)
    RY = rdays%365
    Month = int(RY/30)
    Days = RY%30

    print("Your Age Year:",Year,"Months:",Month,"Days",Days)

except ValueError:
   print("ERROR! Please enter a numerical value between 0 to 9999")