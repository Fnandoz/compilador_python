import re

ATRIBUTOS = ["'='"]
ARITIMETICO = ["'+'", "'-'", "'*'", "'/"]
NUMERO = ["'0'", "'1'", "'2'", "'3'", "'4'", "'5'"]
IDENTIFICADOR = ["'a'", "'b'", "'c'", "'d'"]

expr1 = "b = 2 + a + 5"
expr = "a = 1 + 2"
pos = 0

pattern = re.compile("\s*(?:(\d+)|(\w+)|(.))")

while 1:
    m = pattern.match(expr, pos)
    if not m:
        break

    elif repr(m.group(m.lastindex)) in ATRIBUTOS:
        var = repr(m.group(m.lastindex))
        print ("atr: {} pos: {}").format(var, expr.index(var[1]))

    elif repr(m.group(m.lastindex)) in ARITIMETICO:
        var = repr(m.group(m.lastindex))
        print ("aritimetico: {} pos: {}").format(var, expr.index(var[1]))

    elif repr(m.group(m.lastindex)) in NUMERO:
        var = repr(m.group(m.lastindex))
        print ("numero: {} pos: {}").format(var, expr.index(var[1]))

    elif repr(m.group(m.lastindex)) in IDENTIFICADOR:
        var = repr(m.group(m.lastindex))
        print ("identificador: {} pos: {}").format(var, expr.index(var[1]))

    pos = m.end()
