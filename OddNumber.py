even = list(range(2, 51, 2))

print("Even numbers:", even)
print("Min three total:", sum(even[:3]))
print("Max three total:", sum(even[-3:]))
print("Average:", sum(even) / len(even))
