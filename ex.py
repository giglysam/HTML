from matplotlib import pyplot
from instaloader import Instaloader, Profile

L = Instaloader()

username = "gabzsalem"
password = "gabriels120"
L.login(username, password)

profile = Profile.from_username(L.context, username)

count = 0
count1 = 0

for followee0 in profile.get_followees():
    count = count + 1
for followee1 in profile.get_followers():
    count1 = count1 + 1

pyplot.figure(figsize=(8, 8))
o = count / 1000
o0 = count1 / 1000
o1 = o + o0
x = [count / 1000, count1 / 1000, 1 - o1]
if o > o0:
    pyplot.title('YOUR FOLLOWERS ARE LOWER THAN YOUR FOLLOWINGS')
elif o < o0:
    pyplot.title('YOUR FOLLOWERS ARE HIGHER THAN YOUR FOLLOWINGS')
elif o == o0:
    pyplot.title('YOUR FOLLOWERS ARE EQUAL THAN YOUR FOLLOWINGS')
pyplot.pie(x, labels=['following', 'followers', 'other'], normalize=False)
pyplot.legend()
pyplot.show()
