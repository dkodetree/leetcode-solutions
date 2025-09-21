from sortedcontainers import SortedList

class MovieRentingSystem:
    """
    Movie Renting System supporting:
    - search(movie): top 5 unrented shops for a movie, sorted by price, then shop id
    - rent(shop, movie): rent a movie from a shop
    - drop(shop, movie): return a rented movie to a shop
    - report(): top 5 rented movie copies, sorted by price, shop id, movie id
    """

    def __init__(self, n: int, entries: List[List[int]]):
        self.unrented = collections.defaultdict(SortedList) # Hashmap of movie : SortedList of (price, shop)
        self.rented = SortedList()      # SortedList of (price, movie, shop)
        self.price_map = {}             # Hashmap of (shop, movie) : price
        for shop, movie, price in entries:
            self.unrented[movie].add((price, shop))
            self.price_map[(shop, movie)] = price

    def search(self, movie: int) -> List[int]:
        res = []
        for price, shop in self.unrented[movie][:5]:
            res.append(shop)
        return res

    def rent(self, shop: int, movie: int) -> None:
        if (shop, movie) not in self.price_map:
            return
        price = self.price_map[(shop, movie)]
        if movie in self.unrented:
            self.unrented[movie].discard((price, shop))
            self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        if (shop, movie) not in self.price_map:
            return
        price = self.price_map[(shop, movie)]
        if (price, shop, movie) in  self.rented:
            self.rented.remove((price, shop, movie))
            self.unrented[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        res = []
        for price, shop, movie in self.rented[:5]:
            res.append([shop, movie])
        return res


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
