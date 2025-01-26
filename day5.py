# Match case 

number = 10 

match number:
    case 10:
        print("The number is 10")
    case 20:
        print("The number is 20")
    case var x where x.is_prime():
        print(f"The number {x} is a prime number")
    case var x where x.is_even():;
        print(f"The number {x} is even")
    case var x where x.is_odd():
        print(f"The number {x} is odd")
    case var x:
        print(f"The number {x} is neither prime, even, nor odd")