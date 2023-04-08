# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

n=int(input("Введите трехзначное число"))
first_dig=n//100
second_dig=(n//10)%10
third_dig=n%10
print(first_dig+second_dig+third_dig)
