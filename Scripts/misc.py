from collections import deque
import heapq


def queue_basic():
    #Build simple queue
    queue = deque(maxlen = 5)
    for i in range(1,6):
        queue.append(i)
    print ('Queue: ', queue)

    #Add additional element:
    queue.append(6)
    print ('Queue: ', queue)

    #Add element on the left
    queue.appendleft(7)
    print ('Queue: ', queue)

    #Pop an element
    p = queue.pop()
    print ('Pop Element: ',p)
    print ('Queue: ', queue)

    #Pop left:
    p_left = queue.popleft()
    print ('Pop Element left: ',p_left)
    print ('Queue: ', queue)


def heap_basic():
    #Build basic heap:
    numbers = [1,2,3,56,23,12,6,67,12,565,16,7]
    max_four = heapq.nlargest(4, numbers)
    min_four = heapq.nsmallest(4, numbers)

    #Bit more complex:
    dict_list = [
                {'Title':'Book1', 'published': 1998},
                {'Title':'Book2', 'published': 1990},
                {'Title':'Book3', 'published': 2010},
                {'Title':'Book4', 'published': 1900},
                {'Title':'Book5', 'published': 2070}
                ]
    #Use key and lambda function:
    earlist = heapq.nsmallest(2, dict_list, key=lambda x: x['published'])
    print ('Earlist published books are: ', earlist)






queue_basic()