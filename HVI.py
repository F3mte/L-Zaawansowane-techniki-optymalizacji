import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
from shapely.geometry import Polygon

# Przykładowe dane wejściowe
front1 = np.array([[2, 3], [3, 2], [5, 1]])  # Pierwszy front Pareto
front2 = np.array([[2, 3], [4, 2], [5, 1]])  # Drugi front Pareto

# Obliczanie punktu referencyjnego na podstawie największych punktów na każdej osi
reference_point = np.max(np.vstack((front1, front2)), axis=0)

# Generowanie wykresu
fig, ax = plt.subplots()

# Zaznaczenie obszarów hiperobszarowych dla Front 1
front1_sorted = front1[np.argsort(front1[:, 0])]  # Sortowanie punktów frontu 1 względem wartości obiektu 1
front1_sorted = np.vstack((front1_sorted, [reference_point]))  # Dodanie punktu referencyjnego

# Obliczanie pola powierzchni hiperobszaru
polygon1 = Polygon(front1_sorted)
area1 = polygon1.area

# Zaznaczenie obszarów hiperobszarowych dla Front 2
front2_sorted = front2[np.argsort(front2[:, 0])]  # Sortowanie punktów frontu 2 względem wartości obiektu 1
front2_sorted = np.vstack((front2_sorted, [reference_point]))  # Dodanie punktu referencyjnego

# Obliczanie pola powierzchni hiperobszaru
polygon2 = Polygon(front2_sorted)
area2 = polygon2.area

# Obliczanie obszaru wspólnego
intersection = polygon1.intersection(polygon2)
intersection_area = intersection.area

# Obliczanie ostatecznego pola powierzchni z odjęciem obszaru wspólnego
area1 = area1 - intersection_area
area2 = area2 - intersection_area

# Wykres dla Front 1
ax.step(front1_sorted[:, 0], front1_sorted[:, 1], color='orange', label=f'Front 1 (Pole = {area1:.2f})')

# Wykres dla Front 2
ax.step(front2_sorted[:, 0], front2_sorted[:, 1], color='blue', linestyle='dashed', label=f'Front 2 (Pole = {area2:.2f})')

# Tworzenie obszarów ograniczonych schodkami dla Front 1
front1_patch_points = np.vstack((front1_sorted, front1_sorted[-2::-1]))

# Tworzenie obszarów ograniczonych schodkami dla Front 2
front2_patch_points = np.vstack((front2_sorted, front2_sorted[-2::-1]))

# Tworzenie patcha dla obszaru ograniczonego dla Front 1
patch1 = patches.Polygon(front1_patch_points, facecolor='blue', alpha=0.3, zorder=1)
ax.add_patch(patch1)

# Tworzenie patcha dla obszaru ograniczonego dla Front 2
patch2 = patches.Polygon(front2_patch_points, facecolor='orange', alpha=0.3, zorder=1)
ax.add_patch(patch2)

# Dodanie legendy
ax.legend()

# Dodanie etykiet
plt.xlabel('Wartość obiektu 1')
plt.ylabel('Wartość obiektu 2')

# Dodanie tytułu wykresu
plt.title('Porównanie dwóch frontów Pareto')

# Wyświetlenie wykresu
plt.show()