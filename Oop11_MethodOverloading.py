class Calci:
    def add(self,a,b,*args):
        total = a+b+sum(args)
        return total

Calc1 = Calci()
print(Calc1.add(0, 10, 5))

Calc2 = Calci()
print(Calc2.add(5, 10, 15, 20))

Calc3 = Calci()
print(Calc3.add(5, 10, 15, 20, 25))