import numpy as np
import matplotlib.pyplot as plt

x = [160, 162, 180, 182, 172, 172, 160, 178, 175, 190, 175, 168, 165]
y = [50, 58, 80, 85, 57, 65, 45, 80, 78, 100, 60, 55, 55]
# test = np.loadtxt("body_dimensions_data.txt", usecols=(0))
data = np.loadtxt("body_dimensions_data.txt")
height = data[:, -2]
weight = data[:, -3]
s = data[:, -1]
male = s == 1
female = s == 0

fig, axes = plt.subplots(nrows=2)
scat_male = axes[0].scatter(height[male], weight[male], color='b')
scat_female = axes[0].scatter(height[female], weight[female], color='r')
axes[0].set_xlabel('Groesse (cm)', fontsize=14)
axes[0].set_ylabel('Gewicht (kg) ', fontsize=14)
axes[0].legend((scat_male, scat_female), ('Male', 'Female'), fontsize=8)
# other example of scatter-----------------
from sklearn.datasets import load_iris
iris = load_iris()
features = iris.data.T
scat = axes[1].scatter(features[0], features[1], alpha=0.2, s=100*features[3],
                       c=iris.target, cmap='viridis')
axes[1].set_xlabel(iris.feature_names[0], fontsize='16')
axes[1].set_ylabel(iris.feature_names[1], fontsize='16')
axes[1].legend(handles=scat.legend_elements()[0],
               labels=list(iris.target_names), loc='upper left')