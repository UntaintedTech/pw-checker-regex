import re
while True:
    password = input("Password: ")

    regex_pattern = "([A-Za-z0-9$%#@]{7,}[0-9])"
    # password should follow this format: Password@#$@1
    hidden_pw = '*' * len(password)

    if re.match(regex_pattern, password):
        print(f"Your password: {hidden_pw} is secure")
        break
    else:
        print(f'Your password: {hidden_pw} is not good at all')