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

input=input('Enter Amount of Units consumed in a particular month: ')

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