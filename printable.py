class Printable:
    def __str__(self) -> str:
        return f"{self.__class__.__name__}({str(self.__dict__)})"
