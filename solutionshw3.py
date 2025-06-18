#1
def draw_diamond(height):
    middle = height // 2 #this means that if lets say height is 5 then it will be divided by two and round down to nearest whole number which would be the middle 2

    # Top half
    for i in range(middle + 1): #i acts as line counter and since middle is 2 middle + 1 is 3, meaning i will go from 0-2.
        spaces = middle - i #line zero is 2 - 0 = 2, line one is 2 - 1 = 1, line two is 2 - 2 = 0, and each is the number of spaces it will print out.
        hashes = 2 * i + 1 #same method here as spaces, line zero is 2 * 0 + 1 = 1, line one is 2 * 1 + 1 = 3, line two is 2 * 2 + 1 = 5, each is the number of # printed
        print(" " * spaces + "#" * hashes) #this in a way defines what a space and hash is and multiplies it by the corresponding number of hashes and spaces. Think of it like " " * number of spaces.

    # Bottom half
    for i in (1, 0): #Manually listed lines 1 and 0 to just duplicate them
        spaces = middle - i
        hashes = 2 * i + 1
        print(" " * spaces + "#" * hashes)
draw_diamond(5)

#2
def draw_right_triangle(height):
    for i in range(0, height + 1): #triangle begins in line 0 and goes all the way to 5 since height + 1 in this case is 6.
        print("#" * i) 
draw_right_triangle(5)

#3
def compound_interest(principal, rate, years):
    print(f"Initial amount: {principal:.2f}")
    
    for year in range(1, years + 1):
        interest = principal * rate
        principal = principal + interest
        print(f"Year {year}: {principal:.2f}")
    return principal

final_amount = compound_interest(5500, 0.03, 6)
print(f"\nFinal amount: {final_amount:.2f}")

#4
#HELP HAVE NO CLUE
#5
#in the first problem of last week i missed the ":str -> str"
#in the second problem i missed the "list[str]) -> None"
#in the third problem i missed the "float -> None", instead of using "discriminant" I used "equation" and in else I directly implemented the common factor into the equations of x1 and x2 which is the alternative.
