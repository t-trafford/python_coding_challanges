import heapq
H = [21,1,45,78,3,5]
# Covert to a heap
heapq.heapify(H)
print(H)
# Add element
heapq.heappush(H,2)
heapq.heapify(H)

k = sum(H [:2])
print(H)
print(k)
H = H[2:]
print(H)
