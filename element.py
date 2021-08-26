class Element:
    def __init__(self, v, idx):
        self.value = v
        self.index = idx

    def __repr__(self) -> str:
        return f" (val: {self.value}, index: {self.index})"
