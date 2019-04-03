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

for num in range(0,1001):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num," is a prime")