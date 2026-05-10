s1={1,2,3}
s2={4,5,6}
a=list(zip(s1,s2))
print(a)
l1=[1,2,3]
l2=[6,7,8]
for x,y in zip(l1,l2[::-1]):
    print(x,y)
stocks=["relaebel","infony","tcs"]
price=[2103,1234,984]
d1={stocks:price for stocks,price in zip(stocks,price) }
print("\n{}",format(d1))