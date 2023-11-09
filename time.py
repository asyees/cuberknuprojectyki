import time
import winsound

class Timer:
    def __init__(self, duration, action=None):
        self.duration = duration
        self.action = action
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def is_expired(self):
        if self.start_time is None:
            return False
        elapsed_time = time.time() - self.start_time
        return elapsed_time >= self.duration

    def execute_action(self):
        if self.action is not None:
            self.action()

class SmartTimer:
    def __init__(self):
        self.timers = []

    def add_timer(self, timer):
        self.timers.append(timer)

    def remove_timer(self, timer):
        self.timers.remove(timer)

    def run(self):
        while True:
            for timer in self.timers:
                if timer.is_expired():
                    timer.execute_action()
                    self.remove_timer(timer)
            time.sleep(1)

def beep():
    winsound.Beep(1000, 1000)

def open_document():
    # открытие документа


timer1 = Timer(10, beep)
timer2 = Timer(30, open_document)


smart_timer = SmartTimer()
smart_timer.add_timer(timer1)
smart_timer.add_timer(timer2)

# Запуск
smart_timer.run()
