import time
def sol_memory(n):
    a = 1
    b=1
    for i in range(2,n):
        temp = a
        a = a+b
        b = temp
    return a+b


#Solution from https://blog.devgenius.io/daily-coding-problem-problem-12-8056960a3b61
def sol_time(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    dp = [0] * n
    dp[0], dp[1] = 1, 2
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1]

def sol_k_ways(n, ways):
    rec_list = [0 for _ in range(0,n+1)]
    rec_list[0]=1

    for e in range(1, n+1):
        for way in ways:
            if e-way >= 0:
                rec_list[e] += rec_list[e-way]
    return rec_list[n]




if __name__ == "__main__":
    now = time.time()
    for i in range(1,50):
        sol_memory(5000)
    print("Own solution time: ",time.time()-now)
    print(sol_memory(4))
    print(sol_time(4))
    now = time.time()
    for i in range(1,50):
        sol_time(5000)
    print("Internet solution time: ",time.time()-now)

    print(sol_k_ways(5, {1,3,5}))
    print(solution(5, [1,3,5]))