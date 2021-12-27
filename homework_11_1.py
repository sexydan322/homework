class counter:

    def __init__(self, minimal: int, maximal: int):
        self.minimal = minimal
        self.maximal = maximal
        self.actual = minimal

    def upp(self):
        self.actual += 1
        if self.actual > self.maximal:
            self.actual = self.minimal

    def __repr__(self):
        return f'counter(minimal={self.minimal}, maximal={self.maximal}), actual position={self.actual}'


if __name__ == '__main__':
    counter1 = counter(0, 10)
    print(counter1)
    for _ in range(10):
        counter1.upp()
        print(counter1.actual)
    counter1.upp()
    print(counter1.actual)
