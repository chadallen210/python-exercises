# You have rented some movies for your kids: The little mermaid (for 3 days), 
# Brother Bear (for 5 days, they love it), and 
# Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

Little_Mermaid = 3
Brother_Bear = 5
Hercules = 1

rental_fee = 3

(Little_Mermaid * rental_fee) + (Brother_Bear * rental_fee) + (Hercules * rental_fee)

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, and they pay 
# you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? You worked 10 hours for Facebook, 
# 6 hours for Google and 4 hours for Amazon.

Google = 400
Amazon = 380
Facebook = 350

(Google * 6) + (Amazon * 4) + (Facebook * 10)

# A student can be enrolled to a class only if the class is not full and the class 
# schedule does not conflict with her current schedule.

class_is_not_full = True
has_conflict = False

can_be_enrolled = class_is_not_full and has_conflict

# A product offer can be applied only if people buys more than 2 items, and the offer has 
# not expired. Premium members do not need to buy a specific amount of products.

premium_member = False
not_expired = True
