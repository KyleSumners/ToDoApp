todos = []

while True:
    # Get input and strip any whitespace
    user_action = input("Type add, show, or exit: ")
    user_action = user_action.strip()
    # Perform necessary action on To do list
    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "exit":
            break

print("Done")
