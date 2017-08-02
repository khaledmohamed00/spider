import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *



#PROJECT_NAME= 'thenewboston'
#HOMEPAGE='https://thenewboston.com/'
PROJECT_NAME='imdb'
HOMEPAGE='http://www.imdb.com/'
DOMAIN_NAME=get_domain_name(HOMEPAGE)
QUEUE_FILE=PROJECT_NAME + '/queue.txt'
CRAWLED_FILE=PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS=8
queue=Queue()

Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

#Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t=threading.Thread(target=work)
        t.daemon=True
        t.start()


# Do the next job in the queue
def work():
   # c=0
    while True:
       # print(c)
         url=queue.get()
         Spider.crawl_page(threading.current_thread().name,url)
         queue.task_done()
       # c+=1


# Each queued link is a new job

def create_jobs():

    for link in file_to_set(QUEUE_FILE):
       # queue.put(link)
        #queue.join()
        queue.put(link)

    queue.join()
        #create_workers()
    crawl()


 #check if there are items in the queue , if so crawl them

def crawl():
    queued_links=file_to_set(QUEUE_FILE)
    if len(queued_links)>0:
        print(str(len(queued_links)) + 'links in the queue')
        create_jobs()


create_workers()
crawl()