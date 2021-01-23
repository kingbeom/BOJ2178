from collections import deque
def bfs(y,x):
    dq=deque()
    dq.append([y,x])
    while dq:
        y,x=dq.popleft()
        dy,dx=[0,0,1,-1],[1,-1,0,0] #동 서 북 남
        for i in range(4):
            ny, nx= y+dy[i],x+dx[i]
            if ny<0 or nx<0 or ny>=n or nx>=m:
                continue
            if mapp[ny][nx]==0:
                continue
            elif mapp[ny][nx]==1:
                dq.append([ny,nx])
                mapp[ny][nx]=mapp[y][x]+1
    return mapp[n-1][m-1]

n,m=map(int, input().split())
mapp=[list(map(int, input())) for _ in range(n)]
print(bfs(0,0))