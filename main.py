while True:
    # Get input and strip any whitespace
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()
    # Perform necessary action on To do list
    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', "w")
            file.writelines(todos)
            file.close()
        case "show":
            for index, item in enumerate(todos):
                row = f"{index+1}-{item}"
                print(row)
        case "edit":
            number = int(input("Which todo do you want to edit (number): "))
            number = number - 1
            todos[number] = input("Enter the new todo")
        case "complete":
            number = int(input("Number of the todo to complete: "))
            todos.pop(number-1)
        case "exit":
            break

print("Done")
