import numpy as np

'''
    W is a 2x2 matrix
    W[col,row] = W(col|row)
'''
class Channel:
    def __init__ (self, w):
        self.w = w

    def goThrough (self, prob):
        return self.w @ prob

    def kullbackLeibler (self, r):
        if r.shape != (2,1):
            r = r.reshape ((2,1))
        tmp = self.w * np.log (self.w / r)
        return tmp.sum (axis=0)

    def nextProb (self, prob):
        r = self.goThrough (prob)
        nProb = prob * np.exp (- self.kullbackLeibler (r))
        return nProb / nProb.sum ()

