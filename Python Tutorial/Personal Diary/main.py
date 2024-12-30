import os
from datetime import datetime


def create_new_dairy_entry(file_name):
    try:
        print("\nwrite you dairy entry then type 'SAVE' in a single line\n")
        line_entry_list = []
        while True:
            line = input()
            if line.strip().upper() == "SAVE":
                break

            line_entry_list.append(line)

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(file=file_name, mode='a') as my_file:
                my_file.write("\n" + "-" * 40 + "\n")
                my_file.write(f"Entry Date: {timestamp}\n")
                my_file.write("\n".join(line_entry_list))
                my_file.write("\n" + "-" * 40 + "\n")

    except PermissionError:
        print("\nError: Permission denied. Unable to write to the file.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


def view_diary_entry(file_name):
    try: 
        if not os.path.exists(file_name):
            raise IOError("File does not exist!!!")

        with open(file=file_name,mode='r') as my_file:
            file_content = my_file.read()
            if file_content.strip():
                print("\n--- Diary Entries ---\n")
                print(file_content)
            else:
                print("\nThe diary file is empty")
    except PermissionError:
        print("\nError: Permission denied. Unable to read the file.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")



def main():
    my_file = "diary.txt"

    while True:
        print("\n--- Personal Diary Application ---")
        print("1. Write a new diary entry")
        print("2. View previous diary entries")
        print("3. Exit")
        
        try:
            choice = int(input("\nEnter your choice (1-3): "))
        except ValueError:
            print("\nInvalid input. Please enter a number between 1 and 3.")
            continue
        
        match choice :
            case 1:
                create_new_dairy_entry(my_file)
            case 2:
                view_diary_entry(my_file)
            case 3:
                print("\nThank you for using the Personal Diary Application. Goodbye!")
                break
            case _ : 
                print("\nInvalid choice. Please enter a number between 1 and 3.")


main()
