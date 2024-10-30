class User:
    def __init__(self, userID, username):
        self.id = userID
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1
        
user1 = User("001","Zeon")
user2 = User("002","Seun")

user1.follow(user2)
user1.follow(user2)
user2.follow(user1)

print(user1.username)
print(f"Followers: {user1.followers}")
print(f"Following: {user1.following}")

print(user2.username)
print(f"Followers: {user2.followers}")
print(f"Following: {user2.following}")
