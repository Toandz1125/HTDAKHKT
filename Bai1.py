todo_list = []

print("Các công việc cần làm trong ngày:")

while True:
    task = input("Nhập công việc: ")

    if task.lower() == "done":
        break

    if task.strip() != "":
        todo_list.append(task)

print("\nDanh sách công việc:")

with open("todo_list.txt", "w", encoding="utf-8") as file:
    for index, task in enumerate(todo_list, start=1):
        line = f"{index}. {task}"
        print(line)
        file.write(line + "\n")

print("\nĐã lưu vào file todo_list.txt")