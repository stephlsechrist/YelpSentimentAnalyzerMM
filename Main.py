
from TextParser import TextParser

t1 = TextParser("Hello, this is my test_data  99 data9 data Hello Data")
t2 = TextParser("After a few weeks into the  shelter in place I have been waiting for Rusty's brunch items.. I had to "
                "start the first day of Rusty's roll up brunch hard.. I have been craving Rusty's chicken and "
                "biscuits with egg cheese and gravy for weeks and today was the day.. I decided to treat my next door "
                "neighbors and support my neighborhoods favorite southern hot spot. I ordered chicken and biscuits "
                "with a 6 pack of miller some ciders and pilsners to go.. and it was hot ready and juicy in less than "
                "20 minutes. Thanks Rusty and Cody and Rusty's team for all that you do for the neighborhood and "
                "community.. keep the chicken rolling and piping hot... Can't wait till your next brunch..")

for text in t2.sortByTotal():
    print(text)

# for text in t2.sortByAlpha():
#     print(text)
