import datetime
from settings import work_list


class Game:
    def __init__(self, user_id, user_name, task=work_list):
        self.user_id = user_id
        self.user_name = user_name
        self.task = task.copy()
        self.tek_n = 1

    def __str__(self):
        return f"{self.user_id}-{self.user_name}-in task {self.tek_n}"

    def output_list(self):
        return "\n".join([str(key)+") "+val for key, val in self.task.items()])

    def now_task(self):
        if self.tek_n <= len(self.task):
            text = f"Текущее задание: {self.task[self.tek_n]}"
        else:
            text = "Нет текущего задания"
        return text

    def now_finish(self):
        if self.tek_n <= len(self.task):
            text = f"{self.task[self.tek_n]} выполнено!"
            now = datetime.datetime.now()
            self.task[self.tek_n] += f""", готово {now.strftime("%d-%m-%Y %H:%M")}"""
            self.tek_n += 1
        else:
            text = "Все задания выполнены"
        return text

    def reset(self):
        self.tek_n = 1
        self.task = work_list.copy()
        return "Начинаем заново"
