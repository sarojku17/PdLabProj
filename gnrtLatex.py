import sympy
from collections import defaultdict
import sys
class GenerateSymbols(defaultdict):
    def __missing__(self, key):
        self[key] = sympy.Symbol(key)
        return self[key]

def huteshGauttam(str):
        d = GenerateSymbols()
        s1 = ""
        s2 = ""
        s3 = " = "
        flag = 0
        for i in range(len(str)):
                if str[i] == '=':
                        flag = 1
                elif flag == 0:
                        s1 += str[i]
                else:
                        s2 += str[i]
        if flag ==1:
         print(sympy.latex(sympy.simplify(eval(s1,d)))+s3+sympy.latex(sympy.simplify(eval(s2,d))))
        else:
         print(sympy.latex(sympy.simplify(eval(s1,d))))

huteshGauttam("2*x+1/(3*y)+4*z")