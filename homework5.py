immutable_va = 31, 'ira', 25, 'oleg', 'turtle'
print(immutable_va) # кортеж нельзя изменть, потому что он опсывает неизменяемую последовательность
immutable_va [1] = 'yaroslav'
print(immutable_va)
mutable_list = ['banana', 'bool', 'onion']
print (mutable_list)
mutable_list .remove('bool')
print (mutable_list)
mutable_list .append('bread')
print (mutable_list)