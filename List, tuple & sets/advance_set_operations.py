friends = {"Bob", "Rofl", "Anne", "ustaad"}
abroad = {"Bob", "Anne"}
# ".differnce"
local_friend = friends.difference(abroad)
local_friend_2 = abroad.difference(friends)
local_friend_3 = abroad.difference(abroad)
print(local_friend)
print(local_friend_2)
print(local_friend_3)
# ".union"
print("UNION :-")
local_friend_4 = friends.union(abroad)
local_friend_5 = abroad.union(friends)
local_friend_6 = abroad.union(abroad)
print(local_friend_4)
print(local_friend_5)
print(local_friend_6)


# important points :-
# 1. Remember that while using ".differnce" operation always the fisrt one should be bigger than the second one like friends length > abroad length otherwise it will return an empty set.
