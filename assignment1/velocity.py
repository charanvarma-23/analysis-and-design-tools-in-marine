## Dispersion equation : w^2 = gktanh(kd)

import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import LineString
import math

d =15                                          #waterdepth be d in meters
t =8                                           #Wave period in seconds
g= float(9.81)                                  #gravity in m/s^2
omegasquare = (2*3.14156/t)**2                  # w^2 = (2*pie/t)^2
k= np.arange(0.003,3,0.0001)                    #as we are doing iterative process I am ranging k values from 0.025 to 0.125
kd = k*d                                        #multiply depth with k as it is easy for understanding

lhs =[]  
rhs =[]
for k in kd:                                    #from equation w^2 = gktanhkd
    lhs.append((omegasquare*d)/(g*k))
    rhs.append(math.tanh(k)) 

    
x = kd
f = lhs
g = rhs

plt.plot(x, f)
plt.plot(x, g)
plt.xlabel('kd')
plt.ylabel('orange:tanhkd, green:w^2d/gk')
first_line = LineString(np.column_stack((x, f)))
second_line = LineString(np.column_stack((x, g)))
intersection = first_line.intersection(second_line)

if intersection.geom_type == 'MultiPoint':       #plotting the intersection and identifying kd on x axis
    plt.plot(*LineString(intersection).xy, 'o')
elif intersection.geom_type == 'Point':
    plt.plot(*intersection.xy, 'o')


x, y = intersection.xy
k= x[0]/d
print('k is' ,k,'m^-1')                                  #wave number k

#                                               ||| Dispersion relations |||
#---------------------------------------------------------------------------------------------------------------------


c = 9.81*k*(math.tanh(k*d))                       #speed of wave propagation C can be expressed from, 𝐶^2 =𝑔𝑘tanh(𝑘𝑑)
c =math.sqrt(c)
print('speed of wave propagation C ', c,'m/s')
#----------------------------------------------------------------------------------------------------------------------------


l= 2*np.pi/k                                      #Similar algebraic manipulation will yield a relationship for the wave length
print('so wavelenth(l) is ',l,'m')
#-----------------------------------------------------------------------------------------------------------------------------


plt.show()
