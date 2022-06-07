# Author: Alexander Sutter
# Date: June 6, 2022
# Latest Revision: June 6, 2022

import matplotlib.pyplot as plt #should work once package installed
import numpy as np #should already be installed

def getListFromData(key, data):
    list = []
    for set in data:
        value = set[key]
        list.append(value)
    return list

data = [
    {
        "Label": 'Dr Strange Multiverse of Madness',
        "Rotten Tomatoes": 74,
        "color": 'red',
        "explode": 0
    },
    {
        "Label": 'Spiderman No Way Home',
        "Rotten Tomatoes": 93,
        "color": 'blue',
        "explode": 0
    },
    {
        "Label": 'Eternals',
        "Rotten Tomatoes": 47,
        "color": 'teal',
        "explode": 0
    },
    {
        "Label": 'Shang Chi',
        "Rotten Tomatoes": 91,
        "color": 'gold',
        "explode": 0
    },
    {
        "Label": 'Black Widow',
        "Rotten Tomatoes": 79,
        "color": 'black',
        "explode": 0
    }
]#end data

# rottenTomatoes = [74 , 93 , 47 , 91, 79]
rottenTomatoes = getListFromData("Rotten Tomatoes", data)
values = np.array(rottenTomatoes)

# mylabels = ['Dr Strange Multiverse of Madness', 'Spiderman No Way Home', 'Eternals', 'Shang Chi' , 'Black Widow']
myLabels = getListFromData("Label", data)
# myexplode = [0.2,0,0,0,0]
myExplode = getListFromData("explode", data)
# myColors = ['red','blue','teal','gold','black']
myColors = getListFromData("color", data)

plt.pie(values, labels = myLabels, counterclock = False, startangle = 180, explode = myExplode, shadow = True, colors = myColors)
plt.legend(title = "Movies:")
plt.show()