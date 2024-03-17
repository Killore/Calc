def calculater(fk, a, b):
    if fk == '+':
        return a + b
    elif fk == '-':
        return a - b
    elif fk == '*':
        return a * b
    elif fk == '/':
        try:
            return a / b
        except:
            return 'Нельзя разделить на ноль'
