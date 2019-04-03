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


from matplotlib import pyplot as plt
import numpy as np

input=input('Enter Degree: ')

sin={'0':np.sin(0),'30':np.sin(30),'45':np.sin(45),'60':np.sin(60),'90':np.sin(90)}
cos={'0':np.cos(0),'30':np.cos(30),'45':np.cos(45),'60':np.cos(60),'90':np.cos(90)}
tan={'0':np.tan(0),'30':np.tan(30),'45':np.tan(45),'60':np.tan(60),'90':np.tan(90)}

print(eval(input))

'''
with Graph represent
'''
x=np.arange(0,90,15)

y1=np.sin(x)
y2=np.cos(x)
y3=np.tan(x)

plt.plot(x,y1,'r',label='sin(x)')
plt.plot(x,y2,'g',label='cos(x)')
plt.plot(x,y3,'b',label='tan(x)')

plt.xlabel('x values (rads)')
plt.ylabel('sin(x) and cos(x) and tan(x)')

plt.title('sin(x) cos(x) tan(x)')


plt.legend()

plt.show()
