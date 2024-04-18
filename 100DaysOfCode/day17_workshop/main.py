class User:

    def __init__(self, user_id, username):
        self.username = username
        self.id = user_id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "james")
user_2 = User("002", "Not James")

user_1.follow(user_2)

print(user_2.followers)
