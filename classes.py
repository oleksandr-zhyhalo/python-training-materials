# type -> User
from idlelib.autocomplete import TRY_A

counter = 20

class User:
    def __init__(self, firstname, lastname):
        self.age_in_days = None
        self.firstname = firstname # User.firstname
        self.lastname = lastname # User.lastname
        self.level_permission = None
        # save into the database
    def login(self, login, password):
        # connect to db
        # encrypt user password
        # search if user's login are into database
        # compare if encryped password sumbminted by user is same as encprypted pass in database
        # read from database and compare login and password that were entered
        auth_succ = True
        if auth_succ == True:
            return "200", # redirect to homepage
        else:
            return "401" # redirect back to login sreen
    def make_modr(self):
        self.level_permission = "moderator"

    def check_permission(self):
        if self.level_permission == "moderator":
            pass # Can do
        else:
            pass # Can't do



    def print_hello(self):
        print(f"Hello {self.firstname}")

    def print_bye(self):
        print(f"Bye {self.lastname}")

    def get_age_to_days(self, age):
        age_in_days = age * 365
        self.age_in_days = age_in_days



user1 = User("Marta", "Nowak")
user1.get_age_to_days(35)
print(user1.age_in_days)


class Logger:
    def __init__(self):
        self.log = []
        self.counter = 0
    def add(self, msg):
        self.log.append(msg)
    def show(self):
        print("\n".join(self.log))
    def clear_log(self):
        self.log.clear()
    def set_counter(self):
        self.counter = counter


logger = Logger()
logger.add("this is a first message")
logger.add("this is a second message")
logger.add("this is a third message")
logger.set_counter()
print(logger.counter)