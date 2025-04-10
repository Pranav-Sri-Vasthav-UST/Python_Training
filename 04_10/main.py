from task_manager import TaskManager
from storage import Storage

def display_tasks(tasks: list) -> None:
    if not tasks:
        print("No tasks to display")
    else:
        for task in tasks:
            status = "✓" if task.completed else "✗"
            print(f"[{status}] {task.id} - {task.description}")

def main():

    manager = TaskManager()
    store = Storage()

    saved_tasks = store.load()
    manager.load_tasks(saved_tasks)

    while True:

        print("TODO Application: ")
        print("\n1. Add Task\n2. View Tasks\n3.Complete Task\n4. Delete Task\n5. Exit\n")
        choice = input("Choice -> ")

        if choice == '1':
            desc = input("Enter a description: ")
            if desc.strip():
                task = manager.add_task(desc.strip())
                store.save(manager.to_dict_list())
                print(f"Task added with ID: {task.id}")
            else:
                print("Description cannot be empty")
        elif choice == '2':
            display_tasks(manager.get_all_tasks())
        elif choice == '3':
            tid = input("Enter the Task ID to complete: ")
            if manager.complete_task(tid):
                store.save(manager.to_dict_list())
                print("Task Deleted")
            else:
                print("Task ID not found")
        elif choice == '4':
            tid = input("Enter the Task ID to delete: ")
            if manager.delete_task(tid):
                store.save(manager.to_dict_list())
                print("Task Deleted")
            else:
                print("Task ID not found")
        elif choice == '5':
            print("Goodbye !")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":

    main()