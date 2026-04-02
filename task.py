tasks = []
"add task"

def add_task (title):
    task = {"title": title, "done": False}
    tasks.append(task)
    print (f"Added: {title}")
    
add_task("Pickup package")