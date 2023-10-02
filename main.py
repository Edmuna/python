todos = []

while True:
    user_action = input("Type add, show, exit ")

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            print(todos)
        case "exit":
            print("Program is stopped!")
            break
