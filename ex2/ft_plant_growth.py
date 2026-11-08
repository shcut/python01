#!/usr/bin/env python3

class Plant:
	def __init__(self, name: str, height: float, age_self: int, growt: float, growth: float) -> None:
		self.name = name
		self.height = height
		self.age_self = age_self
		self.growt = growt
		self.growth = growth

	def show(self) -> None:
		print(f"{self.name}: {self.height:.1f}cm {self.age_self} days old")
	def grow(self) -> None:
		self.height += self.growt
		self.growth += self.growt
	def age(self) -> None:
		self.age_self += 1
def main() -> None:
	rose = Plant("Rose", 25, 30, 0.8, 0)
	print("=== Garden Plant Growth ===")
	rose.show()
	for day in range(1, 8):
		print(f"=== Day {day}===")
		rose.grow()
		rose.age()
		rose.show()
	print(f"Growth this week: {rose.growth}cm")

if __name__ == "__main__":
	main()
