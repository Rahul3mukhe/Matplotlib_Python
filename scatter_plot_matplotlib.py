# -*- coding: utf-8 -*-
"""Scatter_plot_Matplotlib.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OUZjG5rLZLArhTSaRg2j8LBQwqo90oLF
"""

import matplotlib.pyplot as plt
day = [1,2,3,4,5,6,7]
night = [4,7,2,8,0,1,6]
plt.scatter(day,night)
plt.title("Scatter Plot",fontsize = 20)
plt.xlabel("Day")
plt.ylabel("Night")
plt.show()

day = [1,2,3,4,5,6,7]
night = [4,7,2,8,0,1,6]
colors = ['r','g','b','y','m','c','k']
sizes = [100,200,300,400,500,600,700]
plt.scatter(day,night,c = colors,s = sizes)
plt.title("Scatter Plot",fontsize = 20)
plt.xlabel("Day")
plt.ylabel("Night")
plt.show()

day = [1,2,3,4,5,6,7]
night = [4,7,2,8,0,1,6]
colors = ['r','g','b','y','m','c','k']
sizes = [100,200,300,400,500,600,700]
plt.scatter(day,night,c = colors,s = sizes,alpha = 0.5,marker = "*",edgecolor ="black",linewidth = 2)
plt.title("Scatter Plot",fontsize = 20)
plt.xlabel("Day")
plt.ylabel("Night")
plt.show()

day = [1,2,3,4,5,6,7]
night = [4,7,2,8,0,1,6]
colors = [10,45,34,67,23,46,99]
sizes = [100,200,300,400,500,600,700]
plt.scatter(day,night,c = colors,s = sizes, cmap = "viridis")
plt.colorbar()
plt.title("Scatter Plot",fontsize = 20)
plt.xlabel("Day")
plt.ylabel("Night")
plt.show()

day = [1,2,3,4,5,6,7]
night = [4,7,2,8,0,1,6]
sunrise = [1,2,3,4,5,6,7]
sunset = [4,7,2,8,0,1,6]

colors = [10,45,34,67,23,46,99]
sizes = [100,200,300,400,500,600,700]

plt.scatter(day,night,sunrise,c = colors)
plt.scatter(night,sunrise,sunset,color = "r",s = sizes, cmap = "viridis")

t = plt.colorbar()
t.set_label("colorbar")

plt.title("Scatter Plot",fontsize = 20)
plt.xlabel("Day")
plt.ylabel("Night")
plt.show()

