class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_info = {}                                     # food : [cuisine, current rating]
        self.cuisine_heaps = collections.defaultdict(list)      # cuisine : max_heap with lazy deletion

        for idx, food in enumerate(foods):
            self.food_info[food] = [cuisines[idx], ratings[idx]]
            heapq.heappush(self.cuisine_heaps[cuisines[idx]], (-ratings[idx], food))

    def changeRating(self, food: str, new_rating: int) -> None:
        self.food_info[food][1] = new_rating
        cuisine = self.food_info[food][0]
        heapq.heappush(self.cuisine_heaps[cuisine], (-new_rating, food))

    def highestRated(self, cuisine: str) -> str:
        max_heap = self.cuisine_heaps[cuisine]
        # Lazy Deletion: Pop until the rating at top matches the current rating
        while max_heap:
            top = max_heap[0]               # (-rating, food)
            rating, food = -top[0], top[1]

            if rating == self.food_info[food][1] and cuisine == self.food_info[food][0]:
                return food
            heapq.heappop(max_heap)
        return ""


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
