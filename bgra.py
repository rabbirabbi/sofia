PROGRAM 7
import matplotlib.pyplot as plt

#x-co ordinateof left sides of bars
left=[1,2,3,4,5]

#height of bars
height=[10,24,36,40,5]

#labels for bars
tick_label=['one','two','three','four','five']

#plotting a bar chart
plt.bar(left,height,tick_label=tick_label,width=0.8,color=['red','yellow'])

#naming x-axis
plt.xlabel("x-axis")

#naming y-axis
plt.ylabel("y-axis")

#plot title
plt.title("my first graph")

#function to show the plot
plt.show()
OUTPUT
