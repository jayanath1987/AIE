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


input=input('Enter the marks of a student: ')

try:
    marks = int(input)
    if marks not in range(0, 101):
       print("ERROR! Please enter a numerical value between 0 to 100")
    else:
        if marks < 45:
            if marks < 30:
                grade="D-"
            elif  marks < 35:
                grade = "D"
            elif  marks < 40:
                grade = "D+"
            else :
                grade = "C-"
            print("Student is FAIL, Grade",grade)
        else:
            if marks < 50:
                grade="C"
            elif  marks < 55:
                grade = "C+"
            elif  marks < 60:
                grade = "B-"
            elif  marks < 65:
                grade = "B"
            elif  marks < 75:
                grade = "B+"
            elif  marks < 80:
                grade = "A-"
            elif  marks < 90:
                grade = "A"
            else :
                grade = "A+"
            print("Student is PASS, Grade", grade)



except ValueError:
   print("ERROR! Please enter a numerical value between 0 to 100")
