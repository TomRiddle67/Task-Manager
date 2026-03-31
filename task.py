tasks = []
#add_task

def add_task (title):
    task = {"title": title, "done": False}
    tasks.append(task)
    print (f"Added: {title}")

add_task("Pickup package")
add_task("Buy Fruits")

#view_task
def view_tasks():
    if len(tasks)== 0:
        print("no tasks yet!")
        return
    for i, task in enumerate(tasks):
        status = "[x]" if task ["done"] else "[]"
        print(f" {i}: {status} {task['title']}")

view_tasks()

def delete_task(index):
    if index < 0 or index >= len(tasks):
        print("Invalid index!")
        return
    removed= tasks.pop(index)
    print(f"Deleted: {removed['title']}")
delete_task (1)