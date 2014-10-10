romano_búsqueda = (
        (1000,'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50,  'L'),
        (40,  'XL'),
        (10,  'X'),
        (9,   'IX'),
        (5,   'V'),
        (4,   'IV'),
        (1,   'I'),
        )

def toRoman(num):
    resultado = ''
    dato = num
    for número, Nromano in romano_búsqueda:
        while dato >= número:
            resultado += Nromano
            dato -= número
    return resultado

    raise NotImplementedError
