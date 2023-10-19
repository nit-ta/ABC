N = int(input())
D = [[0] * N for _ in range(N)]
for i in range(N - 1):
    d = list(map(int, input().split()))
    for j, v in enumerate(d, start=i + 1):
        D[i][j] = v
        D[j][i] = v

dp = [-1] * (1 << N)
dp[0] = 0
for mask in range(1 << N):
    if bin(mask).count('1') % 2 == 1:  # 奇数の頂点数の場合はスキップ
        continue
    for i in range(N):
        if not mask & (1 << i):
            continue
        for j in range(i + 1, N):
            if not mask & (1 << j):
                continue
            if dp[mask ^ (1 << i) ^ (1 << j)] == -1:
                continue
            dp[mask] = max(dp[mask], dp[mask ^ (1 << i) ^ (1 << j)] + D[i][j])

if N % 2 == 1:
    ans = max(dp[(1 << N) - 1 - (1 << i)] for i in range(N))
else:
    ans = dp[(1 << N) - 1]
print(ans)
