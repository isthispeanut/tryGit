import matplotlib.pyplot as plt
import pandas as pd

colors = ['Red', 'Green', 'Blue', 'Yellow', 'Orange']
students = [45, 15, 55, 50, 35]
bar_colors = ['red', 'green', 'cyan', 'yellow', 'orange']

plt.figure(figsize=(9,5))
bars = plt.bar(colors, students, color=bar_colors, edgecolor='black', linewidth=1.5)

for bar, label in zip(bars, colors):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() - 5, label, 
             ha='center', va='top', rotation=90, fontsize=12, color='black', fontweight='bold')

# Labels and title
plt.title("Activity 3: Pandas and Mathplotlib", fontsize=14, fontweight='bold', pad=15)
plt.ylabel("Number of students", fontsize=12, fontweight='bold')
plt.ylim(0, 70)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# import matplotlib.pyplot as plt
'''
colors = ['Red', 'Green', 'Blue', 'Yellow', 'Orange']
students = [45, 15, 55, 50, 35]
bar_colors = ['red', 'green', 'cyan', 'yellow', 'orange']

plt.figure(figsize=(9,5))
bars = plt.bar(colors, students, color=bar_colors, edgecolor='black', linewidth=1.5)

for bar, label in zip(bars, colors):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() - 5, label, 
             ha='center', va='top', rotation=90, fontsize=12, color='black', fontweight='bold')


plt.title("Activity 3: Pandas and Mathplotlib", fontsize=14, fontweight='bold', pad=15)
plt.ylabel("Number of students", fontsize=12, fontweight='bold')
plt.ylim(0, 70)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
'''
