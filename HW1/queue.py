import pyb, uheapq

data = [1,2,3]
uheapq.heapify(data) # Convert to heap
uheapq.heappush(data, 4) # Push to queue
print(data)
uheapq.heappop(data) # Pop from queue

