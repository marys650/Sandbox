def main():
    password = get_password()
    asterisks = '*' * len(password)
    print("\n" + asterisks)


def get_password():
    return input("Enter password: ")


main()