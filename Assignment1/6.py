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
while True:
    userInput = input()


    def add(x=0, y=0):
        z = x + y
        print(z)

    def sub(x=0, y=0):
        z = x - y
        print(z)

    def mul(x=0, y=0):
        z = x * y
        print(z)

    def div(x=0, y=0):
        z = x / y
        print(z)

    if userInput == "quit":
        exit()
    else:

        data = userInput
        print(data[0],data[1],data[2])
        if data[1] is '+':
            add(float(data[0]),float(data[2]))
        elif data[1] is '-':
            sub(float(data[0]),float(data[2]))
        elif data[1] is '*':
            mul(float(data[0]),float(data[2]))
        elif data[1] is '/':
            div(float(data[0]),float(data[2]))

