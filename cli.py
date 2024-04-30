import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    # Get input and strip any whitespace
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    # Perform necessary action on To do list
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter the new todo: ") + '\n'
            todos[number] = new_todo

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid")

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            removed_todo = todos.pop(number-1).strip('\n')

            functions.write_todos(todos)

            message = f"Todo {removed_todo} was completed and removed"
            print(message)
        except IndexError:
            print("There isn't an item with that number")

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")

print("Done")
