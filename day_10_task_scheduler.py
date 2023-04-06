"""Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds."""


import time
def scheduler(f, n:int):
    time.sleep(n/1000)
    f()
    

if __name__ == "__main__":
    f = lambda :print("anlcn")
    scheduler(f, 5000)