import threading
import queue
import time

# Shared queue between producers and consumers
shared_queue = queue.Queue()
print_lock = threading.Lock()  # To prevent jumbled print output

# Producer function
def producer(id, num_items):
    for i in range(num_items):
        item = f'Producer {id} - Item {i}'
        shared_queue.put(item)
        with print_lock:
            print(f'{item} produced')
        time.sleep(1)

# Consumer function
def consumer(id):
    while True:
        try:
            item = shared_queue.get(timeout=2)
            with print_lock:
                print(f'{item} consumed by Consumer {id}')
            shared_queue.task_done()
        except queue.Empty:
            with print_lock:
                print(f'Consumer {id} timed out')
            break

def main():
    # Get number of producers and consumers from user input
    num_producers = int(input("Enter the number of producers: "))
    num_consumers = int(input("Enter the number of consumers: "))
    
    # Create producer threads
    producer_threads = []
    for i in range(num_producers):
        num_items = int(input(f"\nEnter the number of items for Producer {i}: "))
        thread = threading.Thread(target=producer, args=(i, num_items))
        producer_threads.append(thread)
        thread.start()

    # Create consumer threads
    consumer_threads = []
    for i in range(num_consumers):
        thread = threading.Thread(target=consumer, args=(i,))
        consumer_threads.append(thread)
        thread.start()

    # Wait for all producers to finish
    for thread in producer_threads:
        thread.join()

    # Wait for all consumers to finish
    shared_queue.join()
    for thread in consumer_threads:
        thread.join()

    print("All producers and consumers have finished.")

if __name__ == "__main__":
    main()
