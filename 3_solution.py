def climb_stairs(n):
  if n == 1:
    return 1
  elif n == 2:
    return 2
  else:
    return climb_stairs(n - 1) + climb_stairs(n - 2)

n = 4
result = climb_stairs(n)
print(result)  # Output: 5
