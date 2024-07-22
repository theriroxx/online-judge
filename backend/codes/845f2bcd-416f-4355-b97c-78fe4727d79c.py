n = int(input().strip())
numbers = list(map(int, input().strip().split()))
sum = sum(numbers)
ans = (n*(n+1))/2-sum
print(ans)