import heapq


def kClosest(points, K):

        heap = []

        for (x, y) in points:
            dist = -(x * x + y * y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
                print(heap)
            else:
                heapq.heappush(heap, (dist, x, y))
                print(heap)

        return [(x, y) for (dist, x, y) in heap]


x = kClosest(points= [[1,3],[-2,2],[9,9],[0,1]], K=1)
print(x)