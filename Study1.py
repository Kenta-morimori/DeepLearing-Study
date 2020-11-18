import numpy as np

def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7 #theta闘値
    tmp = x1*w1 + x2*x2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
print(AND(0, 0))

#w1x1 + w2x1 + b のbをバイアスという

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.7])
    b = 0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1
print(NAND(0, 0))

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.7])
    b = -0.2
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1
print(OR(0, 0))


def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y
print(XOR(1, 0))