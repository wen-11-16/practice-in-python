import tkinter
class Task:
    def __init__(self, id, title, descript):
        self.id=id
        self.title=title
        self.descript=descript
        self.comp=False

    def complete(self):
        self.comp=True

class ToDoList:
    def __init__(self):
        self.task=[]
    def add(self):
        id=len(self.task)+1
        title=input('輸入一個名稱:')
        des=input('輸入一段敘述:')
        self.task.append(Task(id, title, des))
    def reassign_ids(self):
        for i, task in enumerate(self.task):
            task.id = i + 1
    def delete(self,tar):
        for task in self.task:
            if task.id == tar:
                self.task.remove(task)
                print(f'task {tar} removed')
                self.reassign_ids()
                break
        else :print(f'id {tar} not found')
    def mark(self,id):
        for task in self.task:
            if task.id == id:
                task.complete()
                de=input('要刪除該任務嗎?(y/n)').lower()
                if de == 'y':
                    self.delete(id)
                break
        else:
            print(f'id {id} not found')
    def TaskPrint(self):
        for task in self.task:
            print([f'id:{task.id} title:{task.title} descript:{task.descript} completeness:{task.comp}'])
            
    
tasks=ToDoList()
while True:
    order=input('輸入指令: ').lower()
    if order == 'exit':
        break
    elif order == 'add':
        tasks.add()
    elif order == 'del':
        id=int(input('輸入要刪除的編號:'))
        tasks.delete(id)
    elif order == 'print':
        tasks.TaskPrint()
    elif order == 'mark':
        id=int(input('輸入完成的編號:'))
        tasks.mark(id)
    else:
        print('指令錯誤')