import matplotlib.pyplot as plt
import numpy as np

def generate_points(criterion_1_range, criterion_2_range, num_points):
    """
    Generowanie punktów dla przykładu
    """
    points = []
    for _ in range(num_points):
        x = np.random.randint(criterion_1_range[0], criterion_1_range[1])
        y = np.random.randint(criterion_2_range[0], criterion_2_range[1])
        points.append((x, y))
    return points

def pareto_front(points):
    """
    1. F ← P.
        2. Dla każdego a ∈ F:
        2.1. Dla każdego b ∈ F, takiego że a 6= b:
        2.1.1. jeśli b ≺ a, to wykonaj F ← F - {a} oraz break.
    """
    pareto_front = points.copy()

    for a in points:
        for b in points:
            if a != b:
                if all(x <= y for x, y in zip(b, a)) and any(x < y for x, y in zip(b, a)):
                    pareto_front.remove(a)
                    break

    pareto_front.sort(key=lambda p: p[0])

    pareto_x = [p[0] for p in pareto_front]
    pareto_y = [p[1] for p in pareto_front]

    pareto_x = np.array(pareto_x)
    pareto_y = np.array(pareto_y)

    return pareto_x, pareto_y

if __name__ == "__main__":
    criterion_1_range = (15, 22)
    criterion_2_range = (5, 50) 
    num_points = 10
    
    points = generate_points(criterion_1_range, criterion_2_range, num_points)
    
    pareto_x, pareto_y = pareto_front(points)
    
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    
    x = np.array(x)
    y = np.array(y)
    
    plt.scatter(x, y, color='blue', label='Punkty')
    plt.plot(pareto_x, pareto_y, color='red', label='Front Pareto')
    plt.scatter(pareto_x, pareto_y, color='red')
    plt.xlabel('Kryterium 1')
    plt.ylabel('Kryterium 2')
    plt.title('Front Pareto')
    plt.legend()
    plt.grid(True)
    plt.show()