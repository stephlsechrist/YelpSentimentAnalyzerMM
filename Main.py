
from TextParser import TextParser
from StopList import StopList

s1 = StopList()
t1 = TextParser("Hello, this is my test_data  99 data9 data Hello Data")
# 5 star reviews
t2 = TextParser("After a few weeks into the  shelter in place I have been waiting for Rusty's brunch items.. I had to "
                "start the first day of Rusty's roll up brunch hard.. I have been craving Rusty's chicken and "
                "biscuits with egg cheese and gravy for weeks and today was the day.. I decided to treat my next door "
                "neighbors and support my neighborhoods favorite southern hot spot. I ordered chicken and biscuits "
                "with a 6 pack of miller some ciders and pilsners to go.. and it was hot ready and juicy in less than "
                "20 minutes. Thanks Rusty and Cody and Rusty's team for all that you do for the neighborhood and "
                "community.. keep the chicken rolling and piping hot... Can't wait till your next brunch..")
t3 = TextParser("Good! The chicken clay pot was full of flavor.  I also felt that the bavette and dumplings were great. I will return!")
t4 = TextParser("We were a group of 5 and snagged a brunch reservation here (thumbs up for the fact that it was easy to snag a brunch reservation)."
                "There is no reserved parking up in this area, but street parking is pretty abundant and we found parking pretty easily on a Sunday.")
t5 = TextParser("The food is absolutely amazing & second to none! Fresh and flavorful dishes, I will be coming back! Very nice restuarant. "
                "Sia was super & welcoming. Love this place!")
t6 = TextParser("So I did come back......several times actually. I absolutely love it! I guess I don't like lettuce in my burritos. Never did. "
                "I've tried their quesadillas, fish and shrimp tacos and they are all super good! They also fry their chips in house. "
                "This place is the only place I get my burrito/taco fix. Yes, I've tried the ones in the mission. This place tops it. HANDS DOWN. "
                "I used to live in San Jose. And go to Jalisco's. I couldn't find a place in the city similar. And this is totally similar to it! "
                "Glad to finally find my fav spot. I drive all the way from the other side of the city for it! Wish they could add lengua to the menu. "
                "Highly recommend coming here!")
t7 = TextParser("Thank you to all the staff that bravely go to work everyday (amidst the ever changing news and being in SUCH close quarters to so many ppl) "
                "and work the cashiers and stock the shelves and sanitize the place and help customers with petty questions ( lolz ) and still have a smile "
                "on your face through all the chaos and dealing with so many civilians and and and...just thank you :') Hope you all realize how much I "
                "appreciate you guys!! I've been shopping at this location since I was a freshie in college... woofff. Decade plus?? thanks again !")

# t2 = TextParser("After a few weeks into the  shelter in place I have been waiting for Rusty's brunch items.. I had to "
#                 "start the first day of Rusty's roll up brunch hard.. I have been craving Rusty's chicken and "
#                 "biscuits with egg cheese and gravy for weeks and today was the day.. I decided to treat my next door "
#                 "neighbors and support my neighborhoods favorite southern hot spot. I ordered chicken and biscuits "
#                 "with a 6 pack of miller some ciders and pilsners to go.. and it was hot ready and juicy in less than "
#                 "20 minutes. Thanks Rusty and Cody and Rusty's team for all that you do for the neighborhood and "
#                 "community.. keep the chicken rolling and piping hot... Can't wait till your next brunch.."
#                 "Good! The chicken clay pot was full of flavor.  I also felt that the bavette and dumplings were great. I will return!"
#                 "We were a group of 5 and snagged a brunch reservation here (thumbs up for the fact that it was easy to snag a brunch reservation)."
#                 "There is no reserved parking up in this area, but street parking is pretty abundant and we found parking pretty easily on a Sunday."
#                 "The food is absolutely amazing & second to none! Fresh and flavorful dishes, I will be coming back! Very nice restuarant. "
#                 "Sia was super & welcoming. Love this place!"
#                 "So I did come back......several times actually. I absolutely love it! I guess I don't like lettuce in my burritos. Never did. "
#                 "I've tried their quesadillas, fish and shrimp tacos and they are all super good! They also fry their chips in house. "
#                 "This place is the only place I get my burrito/taco fix. Yes, I've tried the ones in the mission. This place tops it. HANDS DOWN. "
#                 "I used to live in San Jose. And go to Jalisco's. I couldn't find a place in the city similar. And this is totally similar to it! "
#                 "Glad to finally find my fav spot. I drive all the way from the other side of the city for it! Wish they could add lengua to the menu. "
#                 "Highly recommend coming here!"
#                 "Thank you to all the staff that bravely go to work everyday (amidst the ever changing news and being in SUCH close quarters to so many ppl) "
#                 "and work the cashiers and stock the shelves and sanitize the place and help customers with petty questions ( lolz ) and still have a smile "
#                 "on your face through all the chaos and dealing with so many civilians and and and...just thank you :') Hope you all realize how much I "
#                 "appreciate you guys!! I've been shopping at this location since I was a freshie in college... woofff. Decade plus?? thanks again !")

print(len(s1.list))

# for text in t2.sortByTotal():
#     print(text)

for text in t2.sortByAlpha():
    print(text)

print()

for text in t3.sortByAlpha():
    print(text)
print()

for text in t4.sortByAlpha():
    print(text)
print()

for text in t5.sortByAlpha():
    print(text)
print()

for text in t6.sortByAlpha():
    print(text)
print()

for text in t7.sortByAlpha():
    print(text)
print()