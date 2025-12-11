from calculator.basic import Calculator

c = Calculator()
a, b = map(int, input("a, b를 입력하시오: ").split())
print(c.add(a, b))
print(c.sub(a, b))
print(c.mul(a, b))
print(c.div(a, b))
