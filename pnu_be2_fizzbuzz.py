def fizzbuzz(n):
    if(n%3==0 and n%5 ==0):
        print("fizzbuzz")
    elif n % 3 == 0 : 
        print('Fizz')
    elif n % 5 == 0 :
        print('Buzz')
    else :
        print(n)

for i in range(1, 101):
    fizzbuzz(i)
