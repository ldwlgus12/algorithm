import heapq

n = int(input())
heap = []

for i in range(n):
    num = map(int, input().split())
    
    for j in num:
        if len(heap) < n:
            heapq.heappush(heap, j)
        else:
            if heap[0] < j:
                heapq.heappop(heap)
                heapq.heappush(heap, j)
                
print(heap[0])
