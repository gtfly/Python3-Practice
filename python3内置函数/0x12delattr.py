class Test:
        x = 1
        y = 2
        z = 3

a = Test()

print(a.x)
print(a.y)
print(a.z)

delattr(Test,'z')
#del Test.z

print(a.x)
print(a.y)
print(a.z)
