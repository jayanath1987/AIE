'''
This program is free software: you can redistribute it and/or modify it under the
terms of the GNU Affero General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along
with this program. If not, see <http://www.gnu.org/licenses/>

Date : April 2019
Author: Mr. Jayanath Liyanage   jayanathl@icta.lk/jayanath1987@gmail.com
URL: https://github.com/jayanath1987/AIE
'''


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