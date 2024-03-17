def simple_decore(fn):
    def scet(fr):
        fr = 0
        fr += 1
        print(fr)
        return fr
    print('Декорируемая функция была вызвана:')
    fn()

@simple_decore
def fk():
    print('раз')

# @simple_decore
# def fr():
#     print('rjk')

# def decorator(func):
#     def scet(func):
#         func = 0
#         func += 1
#         return func
