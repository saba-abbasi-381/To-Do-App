class ToDo:
    
    def __init__(self):
        self.task_lst = self.load_task()
    
    def save_task(self):
        with open("task.txt", "w") as f:
            for t in self.task_lst:
                f.write(t + "\n")
    
    def load_task(self):
        try:
            with open("task.txt", "r") as f:
                return f.read().splitlines()
        except:
            return []
    
    def add_task(self, task):
        self.task_lst.append(task)
        self.save_task()
    
    def view_task(self):
        if not self.task_lst:
            return "Task not exist!"
        
        tasks = []
        for i, task in enumerate(self.task_lst, 1):
            tasks.append(f"{i}.{task}")
        return "\n".join(tasks)
        
        
    def update_task(self, index , new_task):
        self.view_task()
        self.task_lst[index -1] = new_task
        self.save_task()
    
    def delete_task(self, index):
        self.view_task()
        self.task_lst.pop(index - 1)
        self.save_task()
    
    def search_task(self, keyword):
        results = []
        for task in self.task_lst:
            if keyword in task:
                results.append(task)
                
        if results:
            return "/n".join(results)
        else:
            return "Sorry task not exist!"
    
    def clear_all(self):
        self.task_lst.clear()    
        self.save_task()



