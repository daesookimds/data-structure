import heapq

ls = [4, 6, 8, 1]
heapq.heapify(ls)
print(ls)

heapq.heappop(ls)
print(ls)

heapq.heappushpop(ls, 7)
print(ls)

heapq.heapreplace(ls, 9)
print(ls)

for i in heapq.merge([1, 3, 5], [2, 4, 6]):
    print(i)

heapq.nlargest(1, ls)
heapq.nsmallest(2, ls)


h = []
heapq.heappush(h, (1, 'food'))
heapq.heappush(h, (2, 'have fun'))
heapq.heappush(h, (3, 'work'))
heapq.heappush(h, (4, 'study'))
