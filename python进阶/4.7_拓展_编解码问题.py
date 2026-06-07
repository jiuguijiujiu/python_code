s1 = '123哈哈hehe~!@#'
print(s1.encode())          # b'123\xe5\x93\x88\xe5\x93\x88hehe~!@#'
print(s1.encode('utf-8'))   # b'123\xe5\x93\x88\xe5\x93\x88hehe~!@#'
print(s1.encode('gbk'))     # b'123\xb9\xfe\xb9\xfehehe~!@#'

print('-' * 50)

bys1 = b'123\xe5\x93\x88\xe5\x93\x88hehe~!@#'
print(bys1.decode())
print(bys1.decode('utf-8'))
print(bys1.decode('gbk'))

print('-' * 50)

bys2 = b'123\xb9\xfe\xb9\xfehehe~!@#'
print(bys2.decode('gbk'))