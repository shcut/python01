class Plant:
	def __init__(self, name: str, height: float, age_self: int, growt: float, growth: float) -> None:
		self.name = name
		self._height = 0
		self._age_self = 0
		self.growt = growt
		self.growth = growth
		self._initializing = True

		self.set_height(height)
		self.set_age(age_self)
		self._initializing = False
	def show(self) -> None:
		print(f"{self.name}: {self._height:.1f}cm, {self._age_self} days old")
	def grow(self) -> None:
		self.set_height(self._height + self.growt)
		self.growth += self.growt
	def age(self) -> None:
		self.set_age(self._age_self + 1)
	def set_height(self, height):
		if height < 0:
			print(f"{self.name}: Error, height can't be negative\nHeight update rejected")
		else:
			self._height = height
	def set_age(self, age_self):
		if age_self < 0:
			print(f"{self.name}: Error, age can't be negative\nAge update rejected")
		else:
			self._age_self = age_self
	def get_height(self) -> float:
		return self._height
	def get_age(self) -> int:
		return self._age_self

class Flower(Plant):
	def __init__(self, name: str, height: float, age_self: int, growt: float, growth: float, color: str):
		super().__init__(name, height, age_self, growt , growth)
		self.color = color
		self.is_blooming = False
	def bloom(self) -> None:
		print("[asking the rose to bloom]")
		self.is_blooming = True
	def show(self) -> None:
		super().show()
		print(f" Color: {self.color}")
		if self.is_blooming:
			print(f"{self.name} is blooming beautifully!")
		else:
			print(f" {self.name} has not bloomed yet")

class Tree(Plant):
	def __init__(self, name: str, height: float, age_self: int, growt: float, growth: float, trunk_diameter: float):
		super().__init__(name, height, age_self, growt , growth)
		self.trunk_diameter = trunk_diameter
	def produce_shade(self) -> None:
		print(f"[asking the {self.name} to produce shade]")
		print(f"Tree {self.name} now produces a shade of {self._height:.1f}cm long and {self.trunk_diameter:.1f}cm wide.")
	def show(self)->None:
		super().show()
		print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

class Vegetable(Plant):
	def __init__(self, name: str, height: float, age_self: int, growt: float, growth: float, Harvest_season: str):
		super().__init__(name, height, age_self, growt , growth)
		self.harvest_season = Harvest_season
		self.nutritional_value = 0
	def grow(self)-> None:
		super().grow()
		self.nutritional_value += 0.5
	def age(self)-> None:
		super().age()
		self.nutritional_value += 0.5
	def show(self)-> None:
		super().show()
		print(f" Harvest season: {self.harvest_season}")
		print(f" Nutritional value: {self.nutritional_value}")

def main() -> None:
	rose        = Flower("Rose", 15, 10, 0.8, 0, "blanche")
	oak			= Tree("Oak", 200, 365, 0, 0, 5)
	tomato		= Vegetable("Tomato", 5, 10, 2.1, 0, "April")
	print("=== Garden Plant types ===")
	print("=== Flower")
	rose.show()
	rose.bloom()
	rose.show()
	print("\n=== Tree")
	oak.show()
	oak.produce_shade()
	print("\n=== Vegetables")
	tomato.show()
	print(f"[Make {tomato.name} grow and age for 20 days]")
	for harvest in range (20):
		tomato.grow()
		tomato.age()
	tomato.show()


if __name__ == "__main__":
	main()
