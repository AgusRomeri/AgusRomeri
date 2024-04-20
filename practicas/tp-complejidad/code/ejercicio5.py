def contiene_duma(array,n):
    
    for i in range(0,len(array)):
        if (array[i] < n):
            for j in range(0,len(array)):
                if(i != j):
                    if (array[i] + array[j] == n):
                        return True
    return False