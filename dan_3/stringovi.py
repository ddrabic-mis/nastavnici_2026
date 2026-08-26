n='2600'
# n[1]='9' - error, stringovi su nepromjenjivi
a=list(n)
print(f"{a=}" )
x=reversed(n)
print(f"{x=}" )

# želimo promijeniti znak (znamenku) '6' u znak '9'
a[1]='9'
print(f"{a=}" )
# nakon toga želimo natrag dobiti string
b=''.join(a)
print(f"{b=}" )