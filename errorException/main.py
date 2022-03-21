"""
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Somethings")
except KeyError as error_message:
    print(f"That key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")


# Raising my error
height = float(input("Height : "))
weight = float(input("Weight : "))
if height > 3:
    raise ValueError("Human height should not be over 3 meters, due to bmi was not calculated")

bmi = weight / (height ** 2)
print(bmi)


fruits = ["Apple", "Pear", "Orange"]

<<<<<<< Updated upstream
=======


>>>>>>> Stashed changes
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + "pie")


make_pie(4)
"""

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass

print(total_likes)
