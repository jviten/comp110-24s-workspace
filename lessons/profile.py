"""Creating Profile object, Practice writing a class"""

class Profile:
    
    username: str
    private: bool

    def __init__(self, username_input: str):
        """Create a new Profile object"""
        self.username = username_input
        self.private = True
    # Its a method so it has to be indented with class. Method is a function that belongs to a tweet
    def tweet(self, msg: str) -> None:
        "If profile is public then print message"
        if self.private is False:
            print(msg)
# instantiation
user1: Profile = Profile("110_rulez") #calls init by saying Profile(), don't need to put self that's whats being created
user1.private = False
user1.tweet("OOP is cool") #first arguement comes in front for method calls ((user 1.tweet))

