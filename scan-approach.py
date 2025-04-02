import os

def list_files():
    directory = input("Enter the directory to list files: ")
    command = f"ls {directory}"
    output = os.popen(command).read()
    print(output)

def load_data():
    serialized_data = input("Enter serialized data: ")
    data = eval(serialized_data)
    print(f"Data loaded: {data}")

def get_user():
    username = input("Enter username: ")
    query = f"SELECT * FROM users WHERE username = '{username}'"
    print(f"Executing query: {query}")

def greet():
    name = input("Enter your name: ")
    print(f"<h1>Hello, {name}!</h1>")

def main():
    while True:
        print("\nChoose an option:")
        print("1. List files in a directory")
        print("2. Load serialized data")
        print("3. Get user information")
        print("4. Greet user")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_files()
        elif choice == '2':
            load_data()
        elif choice == '3':
            get_user()
        elif choice == '4':
            greet()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
