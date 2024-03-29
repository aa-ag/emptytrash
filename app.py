############------------ IMPORTS ------------############
from datetime import datetime, timedelta
import time
from redis import Redis
from rq import Queue
from rq.job import Retry
import tasks


############------------ GLOBAL VARIABLE(S) ------------############
queue = Queue(connection=Redis())


############------------ FUNCTION(S) ------------############
def queue_tasks():
    loops = 0
    
    while loops < 3:
        queue.enqueue(tasks.create_test_files, retry=Retry(max=2))
        time.sleep(10)

        queue.enqueue_in(timedelta(seconds=5), tasks.delete_test_files)

        time.sleep(10)
        queue.enqueue_in(timedelta(seconds=5), tasks.buh_bye_trash)

        loops += 1
        time.sleep(10)
    


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    queue_tasks()