# Author: Alexander Sutter
# Date: June 6, 2022
# Latest Revision: June 6, 2022

import matplotlib.pyplot as plt #should work once package installed
import numpy as np #should already be installed

rottenTomatoes = [74 , 93 , 47 , 91, 79]
list = np.array(rottenTomatoes)

mylabels = ['Dr Strange Multiverse of Madness', 'Spiderman No Way Home', 'Eternals', 'Shang Chi' , 'Black Widow']
myexplode = [0.2,0,0,0,0]
mycolors = ['red','blue','teal','gold','black']

plt.pie(list, labels = mylabels, counterclock = False, startangle = 180, explode = myexplode, shadow = True, colors = mycolors)
plt.legend(title = "Movies:")
plt.show()