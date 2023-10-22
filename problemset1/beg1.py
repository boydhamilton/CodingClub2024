# note do a test case where number of terms is greater than n (catch slackers who didnt utilize n variable)


n = int(input())
a = input().split(" ")

sum=0
for i in range(0, n):
    sum+=int(a[i])

print(sum)