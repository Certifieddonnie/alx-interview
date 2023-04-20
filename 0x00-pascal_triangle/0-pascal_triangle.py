# This Script solves the pascal principle

def factorial(num):
    if (num == 1) or (num == 0):
        return 1
    return (num * factorial(num-1))

def pascal_triangle(n):
    triangle = []
    if (n <= 0):
        return triangle
    for x in range(0, n):
        temp = []
        for y in range(0, x+1):
            # print(x,y)
            temp.append(Combination(x, y))
            
        
        triangle.append(temp)
    
    return (triangle)


def Combination(x, y):
    # print("I am base fact",factorial(y) * factorial(x-y))
    return int(factorial(x)/(factorial(y)*factorial(x-y)))