tasks = []
#add_task

def add_task (title, priority ="medium"):
    task = {
        "title": title,
        "done": False,
        "priority": priority # "high" "medium" "low"
        }
    tasks.append(task)
    
#view_task
def view_tasks():
    if len(tasks)== 0:
        print("no tasks yet!")
        return
    for i, task in enumerate(tasks):
        status = "[x]" if task ["done"] else "[]"
        pri = task.get("priority","medium")
        print(f" {i}: {status} [{pri}] {task['title']}")

def mark_done(index):
    tasks[index] ["done"]= True

#delete_task
def delete_task(index):
    if index < 0 or index >= len(tasks):
        print("Invalid index!")
        return
    removed= tasks.pop(index)
    print(f"Deleted: {removed['title']}")


def main():
    while True:
        cmd = input("\n [a]dd [v]iew [d]one [x] delete [q]uit:")
        if cmd == "a":
            title = input("Task:")
            pri = input("Priority (high/medium/low):")
            add_task(title, pri)
        elif cmd == "v":
            view_tasks()
        elif cmd == "d":
            view_tasks()
            i = int(input("Mark done #:"))
            mark_done(i)
        elif cmd == "x":
            view_tasks()
            i = int(input("Delete #:"))
            delete_task(i)
        elif cmd == "q":
            print("Bye!")
            break
main() 
