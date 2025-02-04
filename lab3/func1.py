def myFunction(grams):
    print(28.3495231 * grams)

grams = float(input())
myFunction(grams)


#2
def myFunction(F):
    return (5 / 9) * (F - 32)

F = int(input())
print("Centigrate temperature : " , myFunction(F))


#3
def myFunction():
    for y in range(36):
        x = 36 - y
        if 2*x +  4*y == 94:
            return x,y
        
        
chickens , rabbits = myFunction()
print(chickens)
print(rabbits)


#4
def filter_prime(numbers):
    primes = []
    for num in numbers:
        if num > 1 and (num == 2 or num % 2 != 0): 
            primes.append(num) 
    return primes

input_numbers = list(map(int, input().split()))

prime_numbers = filter_prime(input_numbers)

print(prime_numbers)

#5
import itertools

def myFunction():
    str1 = input()
    permutations = itertools.permutations(str1)
    for perm in permutations:
        print(''.join(perm))
        
myFunction()

#6

def reverse_string(s):
    return s[::-1]
input_str = input()
print(reverse_string(input_str))

#7
def has_33(n):
    for i in range(len(n) - 1):
        if n[i] == 3 and n[i+1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))  
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))  

#8
def spy_game(nums):
    sequence = [0, 0, 7]
    seq_index = 0

    for num in nums:
        if num == sequence[seq_index]:
            seq_index += 1
        if seq_index == 3:
            return True

    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5])) 
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  


#9
import math
def myFunction(r):
    return round(4/3 * math.pi * r**3)
r = int(input())
print("The volume of a sphere:" ,myFunction(r))

#10

def unique_list(n):
    new_list = []
    for item in n:
        if item not in new_list:
            new_list.append(item)
    return new_list
input_numbers = list(map(int, input().split()))
result = unique_list(input_numbers)
print(result)


 #11
def palindrome(s): 
    return s == s[::-1]
word = input()
print(palindrome(word))

#12
def histogram(n): 
    for num in n:
        print('*' * num)

histogram([4,9,7])

#13
import random
def game_guess():
    print("Hello! What is your name?")
    name = input()
    num = random.randint(1,20)
    print("Well " , name , "I am thinking of a number between 1 and 20. Take a guess.")


    while True:
        num1 = int(input())
        if num > num1:  
            print("Your guess is too low.Take a guess.")
        elif num < num1:
            print("Your guess is too high.Take a guess.")
        else: 
            print("Good job " , name, "! You guessed my number in 3 guesses!")
            break
    
game_guess()




