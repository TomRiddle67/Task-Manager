tasks = []
#add_task

def add_task (title):
    task = {"title": title, "done": False}
    tasks.append(task)
    print (f"Added: {title}")

add_task("Pickup package")

#view_task
def view_tasks():
    if len(tasks)== 0:
        print("no tasks yet!")
        return
    for i, task in enumerate(tasks):
        status = "[x]" if task ["done"] else "[]"
        print(f" {i}: {status} {task['title']}")

view_tasks()