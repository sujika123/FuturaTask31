# 4.Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615


n = int(input("Enter a number n: "))
temp = str(n)
t1 = temp+temp
t2 = temp+temp+temp
comp = n+int(t1)+int(t2)
print("The value is:",comp)