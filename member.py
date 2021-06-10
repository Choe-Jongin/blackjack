def load_members():
    file = open("members.csv", "r")
    members = {}
    for line in file:
        name, passwd, tries, wins, chips = line.strip('\n').split(',')
        members[name] = (passwd, int(tries), float(wins), int(chips))
    file.close()
    return members

def store_members(members):
    file = open("members.csv","w")
    names = members.keys()
    for name in names:
        passwd, tries, wins, chips = members[name]
        line = name + ',' + passwd + ',' + str(tries) + ',' + \
               str(wins) + "," + str(chips) + '\n'
        file.write(line)
    file.close()

def login(members):
    
    def safe_divide(x,y):
        if y > 0:
            return x/y
        else:
            return 0
    
    username = input("Enter your name: (4 letters max) ")
    while len(username) > 4:
        username = input("Enter your name: (4 letters max) ")
    trypasswd = input("Enter your password: ")
    if members.get(username) != None: # username is in the key of members
        if members.get(username)[0] == trypasswd: # trypasswd is the same as username's password
            tries = members[username][1]
            wins = members[username][2]
            chips = members[username][3]
            # Show the number of games played and the number of wins
            # Example: "You played 101 games and won 54 of them."
            print("You played ", tries," games and won ", int(wins)," of them.")
 
            # Show the winning percentage in percent
            # Example: "Your all-time winning percentage is 53.5%"
            print("Your all-time winning percentage is", "{0:.1f}".format(safe_divide(wins,tries)*100),"%")
            
            # Show the number of chips the player has
            # Example : if the number is 5, "You have 5 chips."
            # Example : if the number is -5, "You owe 5 chips."
            
            if chips >= 0 :
                print("You have",chips,"chips.");
            else:                    
                print("You owe",abs(chips),"chips.");
            
            return username, tries, wins, chips, members
        else:
            return login(members)
    else:
        # Add username to members dictionary.
        members[username] = (trypasswd, 0, 0, 0)
        return username, 0, 0, 0, members
    
def show_top5(members):
    print("---")
    sorted_members = sorted(members.items(), key=lambda x: x[1][3], reverse=True) # Sort the number of chips in reverse order.
    print("All-time Top 5 based on the number of chips earned")
    # Show the elements of sorted_members[:5] in order. 
    # Disregard the record if the number of chips is 0 or less
    index = 1;
    for m in sorted_members:
        if m[1][3] <= 0 or index > 5 :
            break;
        print(str(index)+'.',m[0],":",m[1][3]);
        index += 1

