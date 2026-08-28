brojevi=(
  'ABC',
  'DEF',
  'GHI',
  'JKL',
  'MNO',
  'PQRS',
  'TUV',
  'WXYZ',
)

def odredi_sekunde(slovo):
  for i,slova in enumerate(brojevi):
    if slovo in slova:
      return i+3
  return 0

sekunde=0
for znak in input():
  sekunde+=odredi_sekunde(znak)
print(sekunde)