class Bank():
    def __init__(self,username,password,balance):
        self.accounts = [{
            "username": username,
            "password": password,
            "balance": balance
        }]
        self.logged_in=[]
    
    def get_accounts(self):
        return self.accounts
    def user_registration(self, username, password, amount):
        if len(self.accounts) == 0:
            self.accounts.append({"username": username,"password": password, "balance":amount})
            print("first User registration successful")
        else:
            for i in self.accounts:
                if i["username"] == username and i["password"] == password:
                    print("User already exists")
                    return
                else:
                    self.accounts.append({"username": username,"password": password, "balance":amount})
                    print("User registration successful")
                    return


    def user_login(self,username, password):
        for i in self.accounts:
            # print(i)
            if i["username"]== username and i["password"]==password:
                self.logged_in.append(i)
                print("you are logged in successfuly")
                return 
        print("invalid username or password or you are not registered")
                
    
    def check_balance(self, username, password):
        for i in self.logged_in:
            if i["username"]==username and i["password"]==password:
                print(f"Your current balance is: {i['balance']}")
                return 
            else:
                print("invalid username or passowrd or you need to login to your account")
    
    def deposit(self, username, password, amount):
        for i in self.logged_in:
            if i["username"]==username and i["password"]==password:
                i["balance"]+=amount
                print(f"deposit successful and your current balance is {i['balance']}")
                return 
            else:
                print("invalid username or password or you need to login to your account")
                return "deposit failed"
    
    def withdraw(self, username, password, amount):
        for i in self.logged_in:
            if i["username"]==username and i["password"]==password:
                i["balance"] -= amount
                print (f"withdawal successful and your current balance is {i['balance']}")
                return
                
            else:
                print("invalid username or password or you need to login to your account")
                return "deposit failed"

