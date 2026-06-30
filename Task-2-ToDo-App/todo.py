print("=== TO-DO LIST APPLICATION === ")
tasks = []
def save_tasks():
  with open("tasks.txt", "w") as file:
    for task in tasks:
      file.write(task + "\n")
def load_tasks():
  try:
    with open("tasks.txt", "r") as file:
      for line in file:
        tasks.append(line.strip())
  except FileNotFoundError:
    pass
#load_tasks()
while True:
  print("\nMenu")
  print("1.Add task")
  print("2.View task")
  print("3.Remove task")
  print("4.Exit")
  choice=input("Enter your choice: ")
  if choice == "1":
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks()
    print("Task added succesfully!")
  elif choice == "2":
    if len(tasks) == 0:
      print("No tasks found!")
    else:
      print("Yours tasks:")
      for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
  elif choice == "3":
    if len(tasks) == 0:
      print("No tasks to remove!")
    else:
      print("Your tasks:")
      for i, task  in enumerate(tasks, start=1):
        print(f"{i}. {task}")
      try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
          removed_task = tasks.pop(task_num-1)
          save_tasks()
          print(f"'{removed_task}' removed successfully!")

          print("Your updated tasks:")
          for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        else:
          print("Invalid task number!")
      except ValueError:
        print("Please enter a valid number!")
  elif choice == "4":
    print("Thanks for using the To-Do List!")
    break
  else:
    print("Invalid Choice!")

    
