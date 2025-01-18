import json
#from datetime import datetime

#function to add user to db if does not exists 
def add_user(username, password, qcm_history):
    #handel errors 
    try:
        
        # read the data of existing users 
        with open("donne_users2.json", "r") as f:
            userdata = json.load(f)

        # Check if the user  exists in the data file
        if not any(user['name'] == username for user in userdata['users']):
            new_user = {
                "name": username,
                "password": password,
                "qcm_history": qcm_history
            }
            
            #if it doesn't exist add it to users array
            userdata['users'].append(new_user)
            
            # update the file with the new data
            with open("donne_users2.json", "w") as f:
                json.dump(userdata, f, indent=4)
                
            print(f"User {username} has been successfully created.")
        else:
            
            print(f"User {username} already exists.")
            
    except FileNotFoundError:
        # If this is the first use of the quiz or data file not existing
        userdata = {"users": [{"name": username, "password": password, "qcm_history": qcm_history}]}
        
        with open("donne_users2.json", "w") as f:
            json.dump(userdata, f, indent=4)
            
        print(f"User {username} has been successfully created.")

# Authentication function
def authentication(username, password):
    try:
        with open("donne_users2.json", "r") as f:
            userdata = json.load(f)

        # Check if the user exists and the password matches
        for user in userdata['users']:
            
            if user['name'] == username:
                
                if user['password'] == password:
                    print(f'Welcome to your favourite Quiz, {username}!\n')
                    
                    print("Your QCM History:")
                    history = user['qcm_history']
                    history_str = json.dumps(history, indent=2)
                    print(history_str)
                    return True
                else:
                    #if not desired password
                    print("Wrong password, please try again.")
                    return False
                
        print("Username not found.")
        return False
    #if error opening the data file
    except FileNotFoundError:
        print("User data file not found.")
        return False
            
            
    
    
