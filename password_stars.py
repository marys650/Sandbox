"""Password Star Program"""


def main():
    password = enter_password()
    stars = display_stars(password)
    print(stars)

def enter_password():
    password = input("Enter password : ")
    return password

def display_stars(password):
    return '*' * len(password)


main()