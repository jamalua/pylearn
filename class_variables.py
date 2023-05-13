class Box:

    no_of_boxes = 0

    def __init__(self, side_a: int, side_b: int) -> None:
        """
        Some doc
        """

        self.side_a = side_a
        self.side_b = side_b
        Box.no_of_boxes += 1

    def __str__(self) -> str:
        return f"Side A: {self.side_a}, Side B: {self.side_b}"


b1 = Box(3, 4)
print(b1)
print(Box.no_of_boxes)
print(b1.no_of_boxes)


b2 = Box(6, 8)
print(b2)
print(Box.no_of_boxes)
print(b2.no_of_boxes)
