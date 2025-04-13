m = 10_000_000

sigma = 0
for n in range(1, m+1):
    sigma += (-1) ** (n+1) / (2*n - 1)

pi = 4 * sigma

print(pi)
