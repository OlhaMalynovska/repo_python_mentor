# Треба перевірити
#
# You have 2 lists of names friends = ["John", "Marta", "James"] and enamies =
# ["John", "Johnatan", "Artur"]. Loop through the names of friends and write the
# message f"{friend} we are the best friends" if the friend is not in the list of enemy names.
#  And display the message f"{friend} we are not the friends anymore" if the friend is on the list of enemies.
# If the friend's name is James, we don't check him because he is the best friend.

friends = ["John", "Marta", "James"]
enemies = ["John", "Johnatan", "Artur"]

for name in friends:
    if name in enemies:

        print(f'{name},', 'we are not the friends anymore :(')
    else:
        print(f'{name},', 'we are the best friends:) ')
