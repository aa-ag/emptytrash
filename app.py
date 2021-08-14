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
    pass
    


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    queue_tasks()