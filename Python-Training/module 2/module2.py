'''using zip function'''
# l1=[1,2,3]
# l2=['a','b','c']
# c=zip(l1,l2)
# b=list(c)
# print(b)

'''sum function'''
# l1=[1,2,3]
# print(sum(l1))

# def sum(a):
#     b=0
#     for i in  a:
#         b+=i
#     return b
# a=[1,2,3]
# print(sum(a))

# def sum(a):
#     b=""
#     for i in str(a):
#         b+=i
#     return b
# a=["hello","world"]
# print(sum(a))

# def sum(a):
#     b=""
#     for i in  a:
#         b+=i
#     return b
# a=["aa","bb","cc"]
# print(sum(a))

'''product '''

# def product(a):
#     b=1
#     for i in a:
#         b*=i
#     return b
# # a=[1,2,3]
# print(product([1,2,3]))


'''factorial'''
# def factorial(a):
#     b=1
#     for i in range(1,a+1):
#         b*=i
#     return b
# print(factorial(4))

'''reverse'''
# def reverse(a):
#     b=a[::-1]
#     return b
# b=[1,2,3,4]
# print(reverse(b))

'''min and max'''

# list=[1,2,8,4,5]
# print(min(list))
# print(max(list))

# list=["aabcd","efghi","jkl"]
# min_val=min(list)
# max_val=max(list)

# print(min(list))
# print(max(list))

'''cumulative sum'''

# def cumulative_sum(a):
#     c=[]
#     b=0
#     for i in a:
#         b+=i
#         c.append(b)
#     return c
# a=[1,2,3,4]
# print(cumulative_sum(a))


# def cumulative_sum(a):
#     c=[]
#     b=0
#     for i in a:
#         b+=i
#         c.append(b)
#     return c
# a=[4,3,2,1]
# print(cumulative_sum(a))

# def cummulative_product(a):
#     b=[]
#     c=1
#     for i in a:
#         c*=i
#         b.append(c)
#     return b
# a=[1,2,3,4]
# print(cummulative_product(a))

# def cummulative_product(a):
#     b=[]
#     c=1
#     for i in a[::-1]:
#         c*=i
#         b.append(c)
#     return b
# a=[1,2,3,4]
# print(cummulative_product(a))

'''unique elements'''

# def unique(a):
#     b=[]
#     for i in a:
#         if i not in b:
#             b.append(i)
#     return (b)
# a=[1,2,1,3,2,5]
# print(unique(a))

# def dup(a):
#     b=[]
#     c=[]
#     for i in a:
#         if i in b:
#             if i not in c:
#                 c.append(i)
#         else:
#             b.append(i)
#     return (c)
# a=[1,2,1,3,2,5]
# print(dup(a))

# def group(a,b):
#     res=[]
#     for i in range(0,len(a),b):
#         c=a[i:i + b ]
#         res.append(c)
#     return res

# print(group([1,2,3,4,5,6,7,8,9],3))
    
    
'''sorting List'''

# a=[2,10,4,3,7]
# a.sort()
# print(a)

# a=[2,10,4,3,7]
# # sorted(a)
# print(sorted(a))
# print(a)

# a = [[1, 7], [1, 6]]
# print(a.sort())
# print(a)

'''lamda function'''

# a=[[2,3],[4,6],[6,1]]
# a.sort(key=lambda x:x[0])
# print(a)

# def lensort(a):
#     b=[]
#     b=sorted(a)
#     return b  
# print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']))

# def lensort(a):
#     l=sorted(a,key=lambda x:len(x))
#     return l
        
# print(lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby']))

# def unique(a):
#     b=[]
#     # x=sorted(a,key=lambda a:len(a))
#     for i in a:
#         if i not in b:
#             b.append(i)
#     return b
    
# print(unique(["python","java","python","java"]))


'''Tuples'''

# a = (1, 2, 3)
# print(a[0])

# print(a[1:])

'''sets'''

# x = set([3, 1, 2, 1])
# print(x)
# print(type(x))
# set([1, 2, 3])

# def unique(a):
#      print("python" in a)
#         # pass
        

# a=set(["python","java","python","java"])
# (unique(a))

'''list comprehension'''
''''Q.26'''
# op=list(zip([1, 2, 3],["a", "b", "c"]))
# print(op)

'''Q.27'''
# def square(x):
#     return x*x
# op=list(map(square,range(5)))
# print(op)

'''Q.28'''
# def even(x):
#     return x%2==0
# op=list(filter(even,range(10)))
# print(op)

'''Q.29'''
# def arrays(a,b):
#     result=[]
#     for i in range(a):
#         d=[None]*b
#         result.append(d)
#     return result
# c=arrays(2,3)
# print(c)      

'''Q.35'''
def valuesorts(d):
    return [value for key,value in sorted(d.items())]

result=valuesorts({'x':1,'y':2,'z':3})
print((result))

'''Q.36'''

def invertdict(d): 
    return {value: key for key, value in d.items()}

result = invertdict({'x': 1, 'y': 2, 'z': 3})
print(result) 

