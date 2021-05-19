def black_friday():
    amount = float(input("Cost of the asset you are buying: "))
    prime = float(input("Are you a prime member? (Enter 1 for Yes and 2 for No): "))
    # user input for the amount and membership
    if prime==1:
        amount_p = amount - (amount*(15/100))
    elif prime==2:
        amount_p = amount
    else:
        print("Enter a valid input.")
    # if the member is prime member amount_p would be discounted amount else it would be original
    amount_f = amount_p - (amount_p*(8/100))
    print("The amount you need to pay is Rs. ", amount_f)

black_friday()
