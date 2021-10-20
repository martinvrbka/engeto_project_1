import task_template as t
# Dictionary with existing users
users = {"bob": 123, "ann": "pass123", "mike": "password123", "liz": "pass123"}
# Username and password input from user
user, password = input("Username: "), input("Password: ")
print(users[user])

if users.get(user):
    if str(users[user]) == str(password):
        print(f"User {user} was succesfully logged in.")
    else:
        print("Provided password was not correct!")
        quit()
else:
    print("Given username does not exists.")

number = int(input("Enter number from 1 to 3: "))-1
text = t.TEXTS
print(text)

text, text_formated, result, result_num = text[number].split(), [], {"titlecase": 0, "uppercase": 0, "lowercase": 0, "numeric": 0, "numsum": 0}, {}
print(text)
for word in text:
    text_formated.append((word).strip(".,:;\n"))
print(text_formated)

for word in text_formated:
    if word[0].isupper():
        result["titlecase"] += 1

# Znějakýho důvodu dá pro jedna 2 místo 1
for word in text_formated:
    if word.isupper():
        result["uppercase"] += 1

for word in text_formated:
    if word.islower():
        result["lowercase"] += 1

for word in text_formated:
    if word.isnumeric():
        result["numeric"] += 1
        result["numsum"] += int(word)

for word in text_formated:
    if str(len(word)) not in result_num:
        result_num[str(len(word))] = 1
    else:
        result_num[str(len(word))] += 1

print(
    f"""
    There are {len(text)} words in the selected text.
    """
)

#Prasecina
for num in range(1,len(result_num)+1):
    print(f"{num}|{result_num[str(num)]*'*'}|{result_num[str(num)]}")

print(sorted(result_num))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#pokus git
