# Author: Alexander Sutter
# Date: June 6, 2022
# Latest Revision: June 6, 2022

'''
You might need to install the matplotlib and numpy packages

Here is how to install packages on your computer:
https://packaging.python.org/en/latest/tutorials/installing-packages/#use-pip-for-installing

here is the install of numpy: https://numpy.org/install/
here is the install of matplotlib: https://matplotlib.org/stable/users/installing/index.html

for me on mac I only had to install matplotlib and did it by:
    in a terminal writing
        python3 -m pip install matplotlib
'''

import matplotlib.pyplot as plt #should work once package installed
import numpy as np #should already be installed

list = np.array([74 , 93 , 47 , 91, 79])

mylabels = ['Dr Strange Multiverse of Madness', 'Spiderman No Way Home', 'Eternals', 'Shang Chi' , 'Black Widow']
myexplode = [0.2,0,0,0,0]
mycolors = ['red','blue','teal','gold','black']

plt.pie(list, labels = mylabels, counterclock = False, startangle = 180, explode = myexplode, shadow = True, colors = mycolors)
plt.legend(title = "Movies:")
plt.show()