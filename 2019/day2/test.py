#!/usr/bin/env python3


class DynaMet(type):
    def __new__(cls, name, bases, ns, **kargs):
        exec(f'''def _(self): print("Mr. Chambers, {kargs['m']}")''')
        ns[f"{kargs['methodName']}"] = locals()["_"]
        return super().__new__(cls, name, bases, ns)

class DynaClass(metaclass=DynaMet, m='''It's a cookbook!''',                    methodName="warn"):
    pass

d = DynaClass()
d.warn()