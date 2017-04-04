FriendsNumbers = []
nFriends = int(input()) # Number of friends

# For each friend, read their favourite numbers
for i in range(nFriends):
    FriendsNumbers.append(input().split())

# Read the friend who's number we need, and print it.
n = int(input())
print(" ".join(FriendsNumbers[n][1:]))
