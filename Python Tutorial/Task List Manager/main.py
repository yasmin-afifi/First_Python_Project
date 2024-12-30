import os

def add_task_to_list(task_list,task):
    task_list.append(task)
    print(f'task {task} was added to the task list')

def remove_task_from_list(task_list,task):
    try:
        task_list.remove(task)
        print(f'task {task} was removed from the task list')
    except ValueError:
        print(f'task {task} was not found in the task list')

def view_task_list(task_list):
    if not task_list:
        print("No task list is found")
    else:
        print("Task list:")
        for index ,task in enumerate(task_list ,start=1):
            print(f'{index}. {task}')

def store_task_list_to_file(file_name,task_list):
    try: 
        with open(file=file_name,mode='w') as my_file:
            for task in task_list:
                my_file.write(task+"\n")
        print("Task list has been saved successfully")
    
    except IOError as err:
        print(f'can not write to file {err}')
    

def  load_tasks_from_file(file_name):
    if not os.path.exists(file_name):
        print(f"file {file_name} does not exist")
        return []
    
    task_list = []
    try:
        with open(file=file_name) as my_file:
            task_list = [line.strip() for line in my_file.readline()]
        print("task_list is loaded successfully")
    except IOError as err:
        print(f'can not read from file {err}')
    return task_list

def main():
    filename="tasks.txt"
    task_list = load_tasks_from_file(filename)  
    while True:
        print("\nWelcome to Task List Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Task List")
        print("4. Save Task List")
        print("5. Exit")
        
        choice = input("Select an option: ")

        match choice :
            case '1':
                task = input("Enter the task to add: ")
                add_task_to_list(task_list, task)
            case '2':
                task = input("Enter the task to remove: ")
                remove_task_from_list(task_list, task)
            case '3':
                view_task_list(task_list)
            case '4':
                store_task_list_to_file(filename,task_list)
            case '5':
                # my_tasks = load_tasks_from_file(filename)
                # print(my_tasks)
                print("\nGoodbye!")
                break
            case _ : 
                print("\nInvalid choice. Please enter a number between 1 and 3.")

main()