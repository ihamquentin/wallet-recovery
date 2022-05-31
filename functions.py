import subprocess

#return your seed_words
def seed_words():
    return {} #you may put your own seed words here
  
#copy to clipboard
def copy2clipwin(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

def copy2clipmac(txt):
    cmd='echo '+txt.strip()+'|pbcopy'
    return subprocess.check_call(cmd, shell=True)

#get next permutation
def nextPermutation( arr):
        bPoint, n = -1, len(arr)
        for i in range(n-2,-1,-1):
            if arr[i] >= arr[i+1]: continue                   # Skip the non-increasing sequence
            bPoint = i                                        # Got our breakpoint
            for j in range(n-1,i,-1):                         # again traverse from end
                if arr[j] > arr[bPoint]:                      # Search an element greater the element present at the breakPoint.
                    arr[j], arr[bPoint] = arr[bPoint], arr[j] # Swap it
                    break                                     # We just need to swap once
            break                                             # Break this loop too
        arr[bPoint+1:] = reversed(arr[bPoint+1:])
        return arr   
#get nth permutation:
def getPermutation( n: int, k: int):
        nums = [i for i in range(1,n+1)]
        ret = []       
        while(n):
            f = factorial(n-1)
            index = (k-1)//f 
            ret += [nums[index]]
            nums.remove(nums[index])
            n -= 1
            k %= f
        return ret

def factorial(n: int)->int:
    if n==0: return 1
    elif n==1: return 1
    else: return n*factorial(n-1)



'''
fd = open("a.txt","r")

while True:
    line = fd.readline()
    keeponline += 1

    print "Line:", line
    time.sleep(2)

    #It is just an example condition
    if ( len(line) == 0 ):
        break

fd.close()
'''