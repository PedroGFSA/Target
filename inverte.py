def inverter(string):
  return string[::-1]

## iterativo
def inverter2(string):
  palavra = ""
  for char in string:
    palavra = char + palavra
  return palavra 

## recursivo
def inverter3(string):
  if string == "":
    return ""
  return string[len(string)-1] + inverter3(string[:len(string)-1:]) 

print(inverter3("hello"))
