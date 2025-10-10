class Jar:
    def __init__(self, capacity=12):
        self.size = 0             # uses setter
        self.capacity = capacity  # uses setter
    

    def __str__(self):
        return self.size * '🍪'
    
    # def get_cookie(self):
    #     n = int(input("How many cookies will toy add to the jar? "))
    #     if n > 0:
    #         self.deposit(n)
    #     else:
    #         n = -n
    #         self.withdraw(n)

    def deposit(self, n):
        self.size += n  # setter handles validation

    def withdraw(self, n):
        self.size -= n  # setter handles validation

    # Property for capacity
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 1:
            raise ValueError("Capacity must be at least 1")
        self._capacity = value
        # ensure size never exceeds new capacity
        if self._size > self._capacity:
            raise ValueError

    # Property for size
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value < 0:
            raise ValueError("Size cannot be negative")
        if hasattr(self, '_capacity') and value > self._capacity:
            raise ValueError("Size cannot exceed capacity")
        self._size = value

def main():
    jar = Jar(10)
    jar.get_cookie()
    print(jar)

main()
