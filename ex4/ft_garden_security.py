


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
			if not self._initializing:
				print(f"Height updated: {height}cm")
			self._height = height
	def set_age(self, age_self):
		if age_self < 0:
			print(f"{self.name}: Error, age can't be negative\nAge update rejected")
		else:
			if not self._initializing:
				print(f"Age updated: {age_self} days")
			self._age_self = age_self
	def get_height(self) -> float:
		return self._height
	def get_age(self) -> int:
		return self._age_self

def main() -> None:
	rose        = Plant("Rose", 15, 10, 0.8, 0)
	print("=== Garden Security System ===")
	print("Plant created: ", end="")
	rose.show()
	print("")
	rose.set_height(25)
	rose.set_age(30)
	print("")
	rose.set_height(-25)
	rose.set_age(-25)
	print(f"\nCurrent state: ", end="")
	rose.show()

if __name__ == "__main__":
	main()
