s = input("String: ")
symbol = input("Symbol: ")
vowels = "aeiouAEIOU"
for v in vowels:
    s = s.replace(v, symbol)
print(s)