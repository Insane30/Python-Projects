import random
import datetime 

def getBirthdays(year,group):
    months=["January","February","March","April","May","June","July","August","September","October","November","December"]
    days = list(range(1,30))
     
    random_birthdays=[]

    for i in range (group):
        random_month = random.choice(months)
        random_day = random.choice(days)
        random_date = datetime.datetime(year,months.index(random_month) + 1,random_day)
        random_birthdays.append(random_date.strftime(" %b %d "))

    return random_birthdays

# function to get list of matching birthdays
def getMatch(year,group):
    random_birthday = getBirthdays(year,group)
    repeated_birthday = []
    for i in range(0,len(random_birthday)):
        for j in range(i+1,len(random_birthday)):
            if random_birthday[j] == random_birthday[i]:
                repeated_birthday.append(random_birthday[j])
    return repeated_birthday
    
# function for getting the probability
def birthday_probability(group,simulations):
    count = 0
    for i in range(simulations):
        if i % 10000 == 0:
            print(f"{i} simulation run...")
        if getMatch(2004,group):
            count+=1
    prob = (count / simulations) * 100

    print(f'''Out of {simulations} simulations of {group} people, there was a 
      matching birthday in that group {count} times. This means 
      that {group} people have a {prob:.2f}% chance of 
      having a matching birthday in their group.
      That's probably more then would you think !!!''')


#main
print("Birthday Paradox, by Ayush Kachhap (2241011004)")
group = int(input("How many birthdays shall i generate (MAX : 100) "))
random_b = getBirthdays(2004,group)
print(f"Here are {group} birthdays ! ")
print(*random_b)
one_simulation = getMatch(2004,group)

if len(one_simulation) == 0:
    print("No matching birthday in this group")

print("In this simulation, multiple people have a birthday on  ",end="")
for i in one_simulation:
    print(i,end=" ")
print()
print(f"Generating {group} birthdays 100,000 times...")
s=input("Press enter to begin... ")
print("Let's run another 100,000 simulations.")
birthday_probability(group,100000)


