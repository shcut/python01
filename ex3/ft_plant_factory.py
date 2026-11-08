class Plant:
	def __init__(self, name: str, height: float, age_self: int, growt: float, growth: float) -> None:
		self.name = name
		self.height = height
		self.age_self = age_self
		self.growt = growt
		self.growth = growth

	def show(self) -> None:
		print(f"{self.name}: {self.height:.1f}cm, {self.age_self} days old")
	def grow(self) -> None:
		self.height += self.growt
		self.growth += self.growt
	def age(self) -> None:
		self.age_self += 1
def main() -> None:
	rose        = Plant("Rose", 25, 30, 0.8, 0)
	oak         = Plant("Oak", 200, 365, 0.8, 0)
	cactus      = Plant("Cactus", 5, 90, 0.8, 0)
	sunflower   = Plant("Sunflower", 80, 45, 0.8, 0)
	fern        = Plant("Fern", 15, 120, 0.8, 0)
	plants      = [rose, oak, cactus, sunflower, fern]
	print("=== Plant Factory Output ===")
	for plant in plants:
		print("Created: ", end="")
		plant.show()


if __name__ == "__main__":
	main()
