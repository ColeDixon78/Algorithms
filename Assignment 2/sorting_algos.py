#Sorting algorithms

def bubblesort(A):
    n = len(A)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
                swapped = True
        if swapped == False: break
    return A

def insertionsort(A):
    for i in range(0,len(A)-1):
        if A[i] > A[i+1]:
            insert = i+1
            for j in range(0,i+1):
                if A[insert] < A[i-j]:
                    A[insert],A[i-j] = A[i-j],A[insert]
                    insert = i-j
    return A

def selectionsort(A):
    for i in range(0,len(A)):
        largest_index = 0
        for j in range(0,len(A)-i):
            if A[j] > A[largest_index]: largest_index = j
        A[len(A)-i-1],A[largest_index] = A[largest_index], A[len(A)-i-1]
    return A

#if __name__ = "__main__":
