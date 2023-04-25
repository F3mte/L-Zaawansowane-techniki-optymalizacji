def tsp_bs(cities, beam_width=2):
    """
    Travelling Salesman Problem, using Beam Search method.
    """
    n = len(cities)
    current_tours = [[0]]
    current_costs = [0]
    best_tour = None
    
    while current_tours:
        beam = []
        for i, tour in enumerate(current_tours):
            for city in range(n):
                if city not in tour:
                    new_cost = current_costs[i] + cities[tour[-1], city]
                    if len(tour) == n-1:
                        new_cost += cities[city, 0]  # add cost to return to start city
                        if best_tour is None or new_cost < best_tour[0]:
                            best_tour = (new_cost, tour + [city, 0])
                    else:
                        beam.append((new_cost, tour + [city]))
        beam = sorted(beam, key=lambda x: x[0])[:beam_width]
        current_tours = [tour for cost, tour in beam]
        current_costs = [cost for cost, tour in beam]

    return best_tour
