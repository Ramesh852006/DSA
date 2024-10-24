import heapq

def optimal_merge(files):
   
    heapq.heapify(files)
    total_cost = 0

   
    while len(files) > 1:
        
        first = heapq.heappop(files)
        second = heapq.heappop(files)

        merged = first + second
        total_cost += merged
        heapq.heappush(files, merged)

    return total_cost

# Example:
files = [2, 3, 4, 5, 6]
print("Total cost of optimal merge =", optimal_merge(files))
