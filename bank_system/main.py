from bank import Bank

the_bank = Bank(username="gehad",password="123",balance=123)

the_bank.user_registration("hakeem","456",456)
print(the_bank.get_accounts())

# the_bank.user_login("hakim","456")
the_bank.user_login("hakeem","456")

the_bank.check_balance("hakeem","456")
# the_bank.check_balance("hakee","456")

the_bank.deposit("hakeem","456",500)
# the_bank.deposit("hakeem","56",500)
the_bank.withdraw("hakeem","456",100)
