for i,v in enumerate(input()):
  if i%2 and ord(v)>ord('Z'):
    print(chr(ord(v)-32),end="")
  else:
    print(v,end="")