print("What is the amount that you purchase, in cents?")
purchase= int(raw_input())


if purchase > 1000:
	amount = purchase * .1
	total = purchase * int(amount)
        print("You spent over $10! Your final price is " + str(total) + "cents")
if cents <= 1000:
        print("Your final price is " + str(purchase) + "cents")



