import numpy as np
import matplotlib.pyplot as plt

x = list(map(int, open('inputs.txt', 'r').readlines()))
y1 = list(map(int, open('outputs/PrimeNumberSimple/algorithm1.txt', 'r').readlines()))
y2 = list(map(int, open('outputs/PrimeNumberSimple/algorithm2.txt', 'r').readlines()))
y3 = list(map(int, open('outputs/PrimeNumberSimple/algorithm3.txt', 'r').readlines()))
y4 = list(map(int, open('outputs/PrimeNumberSimple/algorithm4.txt', 'r').readlines()))
plt.figure(figsize=(8, 4.5), layout='constrained')
plt.plot(x, y1, label='Algorithm 1')
plt.plot(x, y2, label='Algorithm 2')
plt.plot(x, y3, label='Algorithm 3')
plt.plot(x, y4, label='Algorithm 4')
plt.xlabel("n")
plt.ylabel("time (ms)")
plt.legend()
plt.show()