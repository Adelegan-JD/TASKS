# TASK 2: Tuple and Input


friend_name = input("Give me the name of your five best friends. Kindly separate them with commas: ")
split_friends = friend_name.split()
friends = tuple(split_friends)
print(friends[::-1])
