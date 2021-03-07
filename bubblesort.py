import time

def bubblesort(data, draw, timer):
    n=len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j]>data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['g' if x == j + 1 else 'r' for x in range(len(data))]) 
                time.sleep(timer) 
          
    # sorted elements geneated with g color 
    drawData(data, ['g' for x in range(len(data))]) 