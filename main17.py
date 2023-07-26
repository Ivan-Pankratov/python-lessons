# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

n = [ int(i) for i in input().split( )]
n = set (n)
print (len(n))