number = int(input("Please enter a number: "))
factors = []

def find_factors(number, factors):
    for i in range(1, number + 1):
        if (number % i == 0):
            factors.append(i)
        

    return factors

print(find_factors(number, factors))