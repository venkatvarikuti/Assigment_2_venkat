import numpy as np

class FibonacciMod:
    
    def __init__(self,n):
        #self.n = n  
    def fib2(self):   # return Fibonacci series up to n
        result = []
        a, b = 0, 1
        while b < self.n:
            result.append(b)
            a, b = b, a+b
        return result           
            
        