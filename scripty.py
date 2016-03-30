import numpy
def median(lst):
    return numpy.median(numpy.array(lst))
x = [389,356,359,363,375,369,325,394,402,373,373,370,364,366,364,325,339,393,392,369,374,359,356,403,334,397]
print (sum(x)/len(x))
m = sorted(x)
print median(m)