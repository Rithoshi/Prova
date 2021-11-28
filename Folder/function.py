'''The goal of this module is to create a dictionary that has the name of a user as key, and the corresponding money balance as values'''


users = {
    "Rita Ghilardi" : "10",
    "Pietro Belligoli" : "12",
    "Marco Visentin" : "5",
    "Francesca Signorello" : "11",
    "Alessandro Bonettoo" : "-10"}
    
def print_users():
    print("These are the users:")
    for user in users:
    	print(user)
    
    
def money_balance(user):
    if user in users:
        print('{}\'s money balance is {}'.format(user, users[user]))
    else:
        print('We don\'t have {}\'s money balance'.format(user))


money_balance("Rita Ghilardi")
