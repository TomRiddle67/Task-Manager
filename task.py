tasks = []
#add_task

def add_task (title, priority ="meduim"):
    task = {
        "title": title,
        "done": False,
        "priority": priority # "high" "meduim" "low"
        }
    tasks.append(task)
    print (f"Added:[{priority}]: {title}")

add_task("Pickup package")
add_task("Buy Fruits")

#view_task
def view_tasks():
    if len(tasks)== 0:
        print("no tasks yet!")
        return
    for i, task in enumerate(tasks):
        status = "[x]" if task ["done"] else "[]"
        pri = task.get("priority","meduim")
        print(f" {i}: {status} [{pri}] {task['title']}")

view_tasks()

#delete_task
def delete_task(index):
    if index < 0 or index >= len(tasks):
        print("Invalid index!")
        return
    removed= tasks.pop(index)
    print(f"Deleted: {removed['title']}")
delete_task (1)