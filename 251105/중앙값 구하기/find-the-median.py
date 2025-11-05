A,B,C = map(int,input().split())
if A<B and B<C:
    print (B)
elif B<A and A<C:
    print (A)
else:
    print (C)
