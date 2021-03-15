# how many ways can you climb to the top, each climb is 1 or 2 steps?
def climb_stairs(n):
    if n==1 or n==2:
        return n
    dp=[0]*n
    # one way to reach step 0: by taking 1 step
    # two ways to reach step 1: by taking 1 2-step or 2 1-steps
    dp[0],dp[1] = 1,2
    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1]
def main():
    if climb_stairs(2) != 2:
        print("test 1 failed")
    if climb_stairs(3) !=3:
        print("test 2 failed")
    if climb_stairs(100) != climb_stairs(98) + climb_stairs(99):
        print("test 3 failed")
    

if __name__ == '__main__':
    main()