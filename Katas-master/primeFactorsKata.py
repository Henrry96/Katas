def primeFactors(number):
    factores = []
    FactorActual = 2
    NumeroActual = number
    while NumeroActual > 1:
        while Esdivisible(NumeroActual, FactorActual):
            factores.append(FactorActual)
            NumeroActual /= FactorActual
        FactorActual += 1 
    return factores

def Esdivisible(number, divisor):
    return number % divisor == 0

    raise NotImplementedError
