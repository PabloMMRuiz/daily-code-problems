"""Let's define a "sevenish" number to be one which is either a power of 7,
 or the sum of unique powers of 7. The first few sevenish numbers
 are 1, 7, 8, 49, and so on. Create an algorithm to find the nth sevenish number."""
     
def getNsevenishNumber(n):
    sevenishNumbers=[]
    it = 0
    while len(sevenishNumbers) <=n:
        sevenishNumbers.append(7**it)
        if len(sevenishNumbers) == n:
            return(sevenishNumbers[-1])
        untilIt = sevenishNumbers[:-1]
        for i in untilIt:
            sevenishNumbers.append(i+7**it)
            if(len(sevenishNumbers)==n):
                return(sevenishNumbers[-1])
        it +=1
    return(sevenishNumbers[-1])

if __name__ == "__main__":
    print(getNsevenishNumber(8))