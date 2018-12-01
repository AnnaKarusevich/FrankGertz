import numpy as np
import matplotlib.pyplot as plt
from  matplotlib.ticker import FuncFormatter
fig = plt.figure()
ax = fig.add_subplot(111)
x=np.array([0,1.5,3,4.5,6,7.5,9,10.5,12,13.5,15,16.5,18,19.5,20,20.5,21,21.5,22,22.5,23,23.5,24,24.5,25,25.5,26,26.5,27,27.5,28,28.5,29,29.5,30,30.5,31,31.5,32,32.5,33,33.5,34,34.5,35,35.5,36,36.5,37,37.5,38,38.5,39,39.5,40,40.5,41,41.5,42,42.5,43,43.5,44,44.5,45,45.5,46,46.5,47,47.5,48,48.8,49,49.5,50,50.5,51,51.5,52,52.5,53,53.5,54,])
y=np.array([0,0,1,2.8,6,11.5,18.5,26,34,42,49,54.5,60.5,64,65,66,67,67.1,67.1,67.1,66.1,65.5,64.8,62.1,61,59,58.1,55.3,54,53.1,52,51.2,51,50.3,50,50,49.9,50,50.5,51.5,53,55,57,59.1,61.5,63.8,65,66.7,69,71,72,73.1,74.8,76,77.2,78,78.5,79,79.5,80,80,80,80,80,79.8,79.5,79,78.8,78.2,78,78,77.5,77.5,77.5,77.5,77.5,77.5,78,78.2,78.5,79,79.5,80])
#plt.title('Анодно-сеточная характеристика')
plt.ylabel('$i_а$,мА')
plt.xlabel('$φ_y$,В')
plt.grid ()
ax.plot(x,y,'ko',markersize=2)
plt.axvline(21.75,ymin=0, ymax=0.783,color='k', linestyle='--')

plt.xticks([i for i in range(0,60,10)])
plt.text(21.6, -4,'$\phi_1$')

plt.axvline(31,ymin=0, ymax=0.59,color='k', linestyle='--')
plt.text(31.2, -4,'$\phi_{min}$')

plt.axvline(43,ymin=0, ymax=0.93,color='k', linestyle='--')
plt.text(43.2, -4,'$\phi_2$')

plt.errorbar(x, y, xerr=0.75, yerr=1, c='black', \
lw=2, marker='.', mfc='black', ms=5)

plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))
plt.xlim([0,60])
plt.ylim([0,85])
# %plt.savefig('11.png',dpi=300)
plt.show()
