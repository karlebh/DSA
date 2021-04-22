from Queue import Queue
from Task import Task
from Printer import Printer
import random

def simulation(num_seconds, page_per_minute):
	printer = Printer(page_per_minute)
	queue = Queue()
	waiting_time = []

	for current_second in range(num_seconds):
		if new_print_task():
			task = Task(current_second)
			queue.enqueue(task)

		if (not printer.busy()) and (not queue.is_empty()):
			new_task = queue.dequeue()
			waiting_times.append(new_task.wait_time(current_second))
			printer.start_next(new_task)

		printer.tick()

	average_wait = sum(waiting_times) / len(waiting_times)
	print("Average Wait %6.2f sec %3d task remaining." %(average_wait, queue.size()))


def new_print_task():
	num = random.randrange(1, 181)
	if num == 180:
		return True
	else:
		return False

for i in range(10):
	simulation(3600, 5)

