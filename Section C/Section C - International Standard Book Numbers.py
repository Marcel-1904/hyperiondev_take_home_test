def isbn13(isbn):

    if len(isbn) == 10: #if the input is an ISBN-10

        # calculate the total sum of products
        total = 0

        for i in range(10):
            if isbn[i] == 'X':
                # if the 10th digit is X, then treat it like a 10
                total += 10*(10-i)
            else:
                # otherwise, multiply the digit with the corresponding weight
                total += int(isbn[i])*(10-i)

        # check if the  sum is divisible by 11
        if total % 11 != 0:
            return "Invalid"
        else:
            # convert the ISBN-10 to ISBN-13
            isbn = '978' + isbn[:-1]

            # calculate the new total sum of products
            total = 0

            for i in range(12):
                if i % 2 == 0:
                    total += int(isbn[i])
                else: 
                    total += 3*int(isbn[i])

            # calculate the check digit to make the ISBN-13 valid
            check = (10 - total % 10) % 10

            #append the check digits to the ISBN-13 and return it
            isbn += str(check)
            return isbn
        
    elif len(isbn) == 13: #if the input is an ISBN-13

        # calculate the total sum of products
        total = 0
        for i in range(13):
            if i % 2 == 0:
                total += int(isbn[i])
            else:
                total += 3*int(isbn[i])

        # check if the sum is divisible by 10
        if total % 10 != 0:
            return "Invalid"
        else: 
            return "Valid"
    else:

        # if the input is neither an ISBN-10 not an ISBN-13, return "Invalid"
        return "Invalid"

#Test cases
# The following test cases will display "Valid"
print(isbn13("9783880531086"))
print(isbn13("9780316066525"))

# The following test cases will display the ISBN-13 numbers
print(isbn13("3880531080")) # Will display the number 9783880531086
print(isbn13("0316066524")) # Will display the number 9870316066525