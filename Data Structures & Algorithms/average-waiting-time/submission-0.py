class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        chef_free = 0
        total_wait = 0
        for arrival, prep in customers:
            start = max(arrival, chef_free)
            finish = start + prep
            total_wait += finish - arrival
            chef_free = finish
        return total_wait / len(customers)