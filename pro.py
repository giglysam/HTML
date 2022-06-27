
from instaloader import Instaloader, Profile

L = Instaloader()

username = "gabzsalem"
password = "gabriels120"
L.login(username, password)

profile = Profile.from_username(L.context, username)

follow_list = []
count = 0

for followee in profile.get_followers():
    follow_list.append(followee.username)
    file = open("prada_followers.txt", "a+")
    file.write(follow_list[count])
    file.write("\n")
    file.close()
    print(follow_list[count])
    count = count + 1
