n = int(input())
m = int(input())
k = int(input())

if (n * m > k) and (k % n == 0 or k % m == 0):
    print("YES")
else:
    print("NO")
