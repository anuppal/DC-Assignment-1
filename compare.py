import filecmp

a = "Data/abc.txt"
b = "Content/pqrs.txt"

# Comparison
result = filecmp.cmp(a,b,shallow=False)
print(result)