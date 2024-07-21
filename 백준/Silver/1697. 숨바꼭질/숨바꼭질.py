from collections import deque

def bfs(s):
    queue = deque()
    queue.append(s)

    while queue:
        a = queue.popleft()
        if a == k:
            return visited[k]
        
        for i in (a+1, a-1, a*2):
            if 0 <= i <= mx and not visited[i]: 
                visited[i] = visited[a] + 1
                queue.append(i)
                
n, k = map(int, input().split())
mx = 10 ** 5
visited = [0] * (mx+1)         
                
print(bfs(n))
