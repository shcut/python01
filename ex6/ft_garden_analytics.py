#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def record_grow(self) -> None:
            self._grow_count += 1

        def record_age(self) -> None:
            self._age_count += 1

        def record_show(self) -> None:
            self._show_count += 1

        def show(self) -> None:
            print(f"Stats: {self._grow_count} grow, "
                  f"{self._age_count} age, {self._show_count} show")

    def __init__(self, name: str, height: float, age_self: int,
                 growt: float = 0, growth: float = 0) -> None:
        self.name = name
        self._height: float = 0
        self._age_self = 0
        self.growt = growt
        self.growth = growth
        self.set_height(height)
        self.set_age(age_self)
        self._stats = self.Stats()

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, "
              f"{self._age_self} days old")
        self._stats.record_show()

    def show_stats(self) -> None:
        self._stats.show()

    def grow(self) -> None:
        previous_height = self._height
        self.set_height(self._height + self.growt)
        self.growth += self._height - previous_height
        self._stats.record_grow()

    def age(self, days: int = 1) -> None:
        self.set_age(self._age_self + days)
        self._stats.record_age()

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height

    def set_age(self, age_self: int) -> None:
        if age_self < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age_self = age_self

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age_self

    @staticmethod
    def older_year(c_age: int) -> bool:
        return c_age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age_self: int,
                 growt: float = 0, growth: float = 0,
                 color: str = "unknown") -> None:
        super().__init__(name, height, age_self, growt, growth)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_blooming:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def record_shade(self) -> None:
            self._shade_count += 1

        def show(self) -> None:
            super().show()
            print(f" {self._shade_count} shade")

    _stats: Stats

    def __init__(self, name: str, height: float, age_self: int,
                 growt: float = 0, growth: float = 0,
                 trunk_diameter: float = 0) -> None:
        super().__init__(name, height, age_self, growt, growth)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        self._stats.record_shade()
        print(f"Tree {self.name} now produces a shade of "
              f"{self._height:.1f}cm long and "
              f"{self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age_self: int,
                 growt: float = 0, growth: float = 0,
                 harvest_season: str = "unknown") -> None:
        super().__init__(name, height, age_self, growt, growth)
        self.harvest_season = harvest_season
        self.nutritional_value: float = 0

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 0.5

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value:g}")


class Seed(Flower):
    def __init__(self, name: str, height: float, age_self: int,
                 growt: float = 0, growth: float = 0,
                 color: str = "unknown", seeds: int = 42) -> None:
        super().__init__(name, height, age_self, growt, growth, color)
        self.seeds = 0
        self._seeds_per_bloom = seeds

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")

    def bloom(self) -> None:
        super().bloom()
        self.seeds += self._seeds_per_bloom


def print_stat(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.show_stats()


def main() -> None:
    rose = Flower("Rose", 15, 10, 8, 0, "red")
    oak = Tree("Oak", 200, 365, 0, 0, 5)
    sunflower = Seed("Sunflower", 80, 45, 30, 0, "yellow", 42)
    anonymous = Plant.anonymous()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    for days in (30, 400):
        print(f"Is {days} days more than a year? -> "
              f"{Plant.older_year(days)}")

    print("\n=== Flower")
    rose.show()
    print_stat(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print_stat(rose)

    print("\n=== Tree")
    oak.show()
    print_stat(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print_stat(oak)

    print("\n=== Seed")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    print_stat(sunflower)

    print("\n=== Anonymous")
    anonymous.show()
    print_stat(anonymous)


if __name__ == "__main__":
    main()
