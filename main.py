# Import used to get the texts from the task_template file.
import task_template as t

# Dictionary with existing users and divider
users, divider = {"bob": 123, "ann": "pass123", "mike": "password123", "liz": "pass123"}, 40 * "-"
# Username and password input from user
user, password = input("Username: "), input("Password: ")
print(divider)

# Checking correct user.
if users.get(user):
    if str(users[user]) == str(password):
        print(f"User {user} was succesfully logged in.")
    else:
        print("Provided password was not correct!")
        quit()
else:
    print("Given username does not exists.")

print(f"Welcome to the app {user}.", divider, f"We have {len(t.TEXTS)} texts to be analyzed.", sep="\n")

# Choosing from texts by entering a number between 1 to 3.
number = int(input(f"Enter number from 1 to {len(t.TEXTS)}: "))-1


# Creation of variable text with partialy formated text, result with dict for counting of letters, result_num is.
text, result, result_num = t.TEXTS[number].split(), {
    "titlecase": 0,
    "uppercase": 0,
    "lowercase": 0,
    "numeric": 0,
    "numsum": 0
}, {}

# Further formating of the text usinf for loop in order to create list of words.
text_formated = [word.strip(".,:;\n") for word in text]

# Going through the list and based on condition adding to specific dict key.
for word in text_formated:
    # Checks whther the first letter is capital. Number check could be used here as well.
    if word[0].isupper():
        result["titlecase"] += 1
    # Checks whether the string is a number/numeric.
    if word.isnumeric():
        result["numeric"] += 1
        result["numsum"] += int(word)
    # Checks whether all the letters are capital and checks whether the word contains any number.
    if word.isupper() and not any([True for sign in word if sign.isnumeric()]):
        result["uppercase"] += 1
    # Checks whether are all the letters in the word lower.
    if word.islower():
        result["lowercase"] += 1

for word in text_formated:
    if str(len(word)) not in result_num:
        result_num[str(len(word))] = 1
    else:
        result_num[str(len(word))] += 1

# Printing our results
print(
    divider,
    f"There are {len(text)} words in the selected text.",
    f"There are {result['titlecase']} titlecase words.",
    f"There are {result['uppercase']} uppercase words.",
    f"There are {result['lowercase']} lowercase words.",
    f"There are {result['numeric']} numeric words.",
    f"There are {result['numsum']} numeric words.",
    divider,
    sep="\n"
)

print("LEN|  OCCURENCES  |NR.", divider, sep="\n")

# Prasecina co vypíše slova dle jejich délky, neumím formatovat string zda se -_-
for num in range(1, len(result_num)+1):
    if len(str(num)) < 2:
        print(
            f"  {num}|{result_num[str(num)]*'*'}"
            f"{' '*(14-(len(result_num[str(num)]*'*')))}|{result_num[str(num)]}"
        )
    elif 3 > len(str(num)) > 1:
        print(
            f" {num}|{result_num[str(num)] * '*'}"
            f"{' ' * (14 - (len(result_num[str(num)] * '*')))}|{result_num[str(num)]}"
        )
    else:
        print(
            f"{num}|{result_num[str(num)] * '*'}"
            f"{' ' * (14 - (len(result_num[str(num)] * '*')))}|{result_num[str(num)]}"
        )
