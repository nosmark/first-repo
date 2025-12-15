class game:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

megabonk: game = game("megabonk", 499)

print(megabonk.name)
print(megabonk.price)