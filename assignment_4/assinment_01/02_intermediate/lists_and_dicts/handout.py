# Function to access element by index
def access_element(lst, index):
    if 0 <= index < len(lst):
        return f"Element at index {index}: {lst[index]}"
    else:
        return "Index out of range!"

# Function to modify an element by index
def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        old_value = lst[index]
        lst[index] = new_value
        return f"Replaced '{old_value}' with '{new_value}'."
    else:
        return "Index out of range!"

# Function to slice the list
def slice_list(lst, start, end):
    try:
        sliced = lst[start:end]
        return f"Sliced list from index {start} to {end}: {sliced}"
    except:
        return "Invalid slicing range!"

# Main game function
def index_game():
    my_list = ['red', 'blue', 'green', 'yellow', 'purple']

    while True:
        print("\nCurrent List:", my_list)
        print("Choose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            index = int(input("Enter the index to access: "))
            print(access_element(my_list, index))

        elif choice == '2':
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            print(modify_element(my_list, index, new_value))

        elif choice == '3':
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            print(slice_list(my_list, start, end))

        elif choice == '4':
            print("Exiting game. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
index_game()
