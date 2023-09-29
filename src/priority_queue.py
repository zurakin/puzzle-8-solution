import heapq


class PriorityQueueItem:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def __lt__(self, other):
        return 0

    def __gt__(self, other):
        return 1


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item: object, priority: object) -> object:
        heapq.heappush(self.queue, (priority, PriorityQueueItem(item)))

    def pop(self):
        if not self.is_empty():
            return heapq.heappop(self.queue)[1].get_value()

    def is_empty(self):
        return len(self.queue) == 0
