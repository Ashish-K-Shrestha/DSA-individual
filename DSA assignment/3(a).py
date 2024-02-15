import heapq

class ScoreTrackerQ3_a:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def add_score(self, score):
        if not self.max_heap or score <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -score)
        else:
            heapq.heappush(self.min_heap, score)

        # Balance the heaps to make sure the difference in size is at most 1
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def get_median_score(self):
        if not self.max_heap:
            raise ValueError("No scores available.")

        if len(self.max_heap) == len(self.min_heap):
            # If the number of scores is even, return the average of the two middle scores
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            # If the number of scores is odd, return the middle score from the larger heap
            return -self.max_heap[0]

if __name__ == "__main__":
    score_tracker = ScoreTrackerQ3_a()
    score_tracker.add_score(85.5)
    score_tracker.add_score(92.3)
    score_tracker.add_score(77.8)
    score_tracker.add_score(90.1)
    median1 = score_tracker.get_median_score()
    print("Median 1:", median1)

    score_tracker.add_score(81.2)
    score_tracker.add_score(88.7)
    median2 = score_tracker.get_median_score()
    print("Median 2:", median2)
