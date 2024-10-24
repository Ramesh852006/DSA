class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractional_knapsack(items, capacity):
    items.sort(key=lambda item: item.value / item.weight, reverse=True)

    total_value = 0.0
    for item in items:
        if capacity >= item.weight:
            capacity -= item.weight
            total_value += item.value
        else:
            total_value += item.value * (capacity / item.weight)
            break

    return total_value

# Example:
items = [Item(60, 10), Item(100, 20), Item(120, 30)]
capacity = 50
print("Maximum value in Fractional Knapsack =", fractional_knapsack(items, capacity))
