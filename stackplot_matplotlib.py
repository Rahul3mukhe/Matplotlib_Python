# -*- coding: utf-8 -*-
"""stackplot_matplotlib.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a6T3VMJ2RZDwchfYcqLvtpNZ_DtxxV0y
"""

import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9,10]
y = [1,4,9,16,25,36,49,64,81,100]

plt.stackplot(x,y)
plt.show()

x = [1,2,3,4,5]
area = [2,3,2,5,4]
area2 = [2,3,4,5,6]
area3 = [7,8,9,6,5]
l = ["area1","area2","area3"]
plt.stackplot(x,area,area2,area3,labels = l,colors = ["r","m","y"],baseline = "sym")
plt.legend(loc = 2)
plt.show()

x = [1,2,3,4,5]
area = [2,3,2,5,4]
area2 = [2,3,4,5,6]
area3 = [7,8,9,6,5]
l = ["area1","area2","area3"]
plt.stackplot(x,area,area2,area3,labels = l,colors = ["r","m","y"],baseline = "wiggle")
plt.title("python")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc = 2)
plt.show()

