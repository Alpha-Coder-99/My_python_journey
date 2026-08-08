#yield: kheet
def square_Generator (nums):
    for n in nums:
        yield n ** 2

gen=square_Generator([1,2,3,4])
print(gen)
print(type(gen))
print(list(gen))

# Python mein yield keyword in dono maanon ka mix hai. Jab aap kisi function mein yield likhti hain, toh wo do kaam karta hai:

# Produce: Wo ek value nikaal kar bahar bhejta hai.

# Give Way: Wo wahin Ruk (Pause) jata hai aur computer ko rasta deta hai ke wo baki kaam kar le.