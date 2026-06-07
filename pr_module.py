class pr:
    """
Use this if you want to be oddly specific when printing,
or use the pr.anypr() that is just the same as python's builtin print()
"""
    def anypr(val: any):
        print(val)
    def strpr(val: str):
        print(str(val))
    def intpr(val: str):
        print(int(val))
    def floatpr(val: float):
        print(float(val))
    def complexpr(val: complex):
        print(complex(val))
    def listpr(val: list):
        print(list(val))
    def tuplepr(val: tuple):
        print(tuple(val))
    def dictpr(val: dict):
        print(dict(val))
    def setpr(val: set):
        print(set(pr))
    def boolpr(val: bool):
        print(bool(val))
