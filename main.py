while True:
    # Get input and strip any whitespace
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    # Perform necessary action on To do list
    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            with open("todos.txt", 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case "show":
            with open("todos.txt", 'r') as file:
                todos = file.readlines()


            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}-{item}"
                print(row)

        case "edit":
            number = int(input("Which todo do you want to edit (number): "))
            number = number - 1

            with open("todos.txt", 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter the new todo: ") + '\n'
            todos[number] = new_todo

            with open("todos.txt", 'w') as file:
                file.writelines(todos)
        case "complete":
            number = int(input("Number of the todo to complete: "))

            with open("todos.txt", 'r') as file:
                todos = file.readlines()

            todos.pop(number-1)

            with open("todos.txt", 'w') as file:
                file.writelines(todos)

        case "exit":
            break

print("Done")
