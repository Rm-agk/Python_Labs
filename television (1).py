class RestaurantTv:
    def __init__(self, name, channeltype):
        self.name = name
        self.channeltype = channeltype

    def get_question(self):
        return "What channel would you like to watch: " + self.name

    def get_channeltype(self):
        return "Channel Type: " + self.channeltype

    def get_greeting(self):
        return "Here is the channel you want to watch, Enjoy!"

television = RestaurantTv("Peter", "Sport")

print("Hello, What is your name: " + television.name)
print(television.get_question())
print(television.get_channeltype())
print(television.get_greeting())

television.get_question()
television.get_greeting()