import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("iris.csv")


test_data = {'petal_length': 3, 'petal_width': 1.5}


nearest_points = [
    {'petal_length': 3, 'petal_width': 1.1},
    {'petal_length': 3.3, 'petal_width': 1},
    {'petal_length': 3.3, 'petal_width': 1},
    {'petal_length': 3.6, 'petal_width': 1.3},
    {'petal_length': 3.5, 'petal_width': 1},
    {'petal_length': 3.5, 'petal_width': 1},
    {'petal_length': 3.7, 'petal_width': 1},
    {'petal_length': 3.8, 'petal_width': 1.1},
    {'petal_length': 3.9, 'petal_width': 1.4},
    {'petal_length': 3.9, 'petal_width': 1.2},
    {'petal_length': 3.9, 'petal_width': 1.1},
    {'petal_length': 4, 'petal_width': 1.3},
    {'petal_length': 4, 'petal_width': 1.3}
]


species_colors = {
    'setosa': 'blue',
    'versicolor': 'green',
    'virginica': 'red',

}


nearest_petal_length = [point['petal_length'] for point in nearest_points]
nearest_petal_width = [point['petal_width'] for point in nearest_points]


distances = np.sqrt((test_data['petal_length'] - np.array(nearest_petal_length))**2 +
                    (test_data['petal_width'] - np.array(nearest_petal_width))**2)

radius = max(distances)


for species, color in species_colors.items():
    species_data = df[df['species'] == species]
    if species == 'test_data':
        plt.scatter(test_data['petal_length'],
                    test_data['petal_width'], color=color, label=species)
    else:
        plt.scatter(species_data['petal_length'],
                    species_data['petal_width'], color=color, label=species)


circle = plt.Circle(
    (test_data['petal_length'], test_data['petal_width']), radius, color='gray', fill=False)
plt.gca().add_artist(circle)


for i, point in enumerate(nearest_points):
    plt.plot([test_data['petal_length'], point['petal_length']], [
             test_data['petal_width'], point['petal_width']], linestyle='--', color='black')
    plt.text(point['petal_length'], point['petal_width'],
             str(i+1), fontsize=10, ha='right')


plt.gca().set_aspect('equal', adjustable='box')


plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Petal Length vs Petal Width by Species')
plt.legend()
plt.grid(True)
plt.show()
