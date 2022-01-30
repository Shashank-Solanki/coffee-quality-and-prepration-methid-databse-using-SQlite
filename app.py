import sqlite


MENU_PROMPT = '''-- coffee bean app --

Please choose one of these options:
1 - add new bean.
2 - see all beans
3 - find a bean by name
4 - EXIT

your selection:
'''


def menu():
    conn = sqlite.connect()
    sqlite.create_tables(conn)

    while (user_input := input(MENU_PROMPT)) != "5":
        if user_input == '1':
            name = input("enter bean name: ")
            method = input("enter how you prepare it: ")
            ratings = int(input("enter your rating score (0-100): "))

            sqlite.add_beans(conn, name, method, ratings)

        elif user_input == '2':
            beans = sqlite.get_all_beans(conn)
            for bean in beans:
                print(bean)

        elif user_input == '3':
            name = input("enter the name: ")
            beans = sqlite.get_beans_by_name(conn, name)
            for bean in beans:
                print(bean)
        else:
            print('invalid input, try again')


menu()


