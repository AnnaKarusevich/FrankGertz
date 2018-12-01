import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter 
fig = plt.figure() 
ax = fig.add_subplot(111) 

x=np.array([0,19,19.5,20,20.5,21,21.5,22,22.5,23,23.5,24,24.5,25,25.5,26,26.5]) 
y=np.array([0,0.005,0.01,0.015,0.03,0.038,0.058,0.082,0.11,0.147,0.195,0.26,0.33,0.413,0.548,0.72,0.948]) 
plt.errorbar(x, y, xerr=0.5, yerr=0.01, c='blue', lw=0.5, mfc='white', ms=3) 


x=np.array([0,19.5,20,20.5,21,21.5,22,22.5,23,23.5,24,24.5,25,25.5,26,26.5,27]) 
y=np.array([0,0.01,0.016,0.025,0.038,0.055,0.079,0.115,0.152,0.185,0.26,0.33,0.38,0.51,0.66,0.86,0.98]) 
plt.errorbar(x, y, xerr=0.5, yerr=0.01, c='black', lw=0.5, mfc='white', ms=3) 


x=np.array([0,19.8,20,20.5,21,21.5,22,22.5,23,23.5,24,24.5,25,25.5,26,26.5,27]) 
y=np.array([0,0.008,0.015,0.022,0.033,0.059,0.071,0.092,0.13,0.17,0.227,0.301,0.375,0.455,0.62,0.74,0.985]) 
plt.errorbar(x, y, xerr=0.5, yerr=0.01, c='red', lw=0.5, mfc='white', ms=3) 

plt.legend(('$\phi_з=40В$','$\phi_з=45В$','$\phi_з=50В$'),loc=(0.1,0.4))

ax.plot(x,y,'ko',markersize=2) 
#plt.title('Анодно-сеточная характеристика')
plt.ylabel('$i_а$,мА') 
plt.xlabel('$φ_y$,В') 
plt.grid () 
plt.xlim([15,28.1]) 
plt.ylim([0,1.1]) 
plt.savefig('22.png',dpi=300)
plt.show()