class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())

'''Answer:AB 
  AB'''
  
'''Q.2-- 
a c d'''

'''Q.3--
a b d'''

'''Q.4--
a d'''