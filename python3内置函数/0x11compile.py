num = 0
strs = 'for i in range(10):    num+=1;print(i)'

c = compile(strs, '', 'exec')

print(c)

print(exec(c))
print(eval(c))

print(num)
