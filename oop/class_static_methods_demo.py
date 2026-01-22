class Calculator:
    calculationg_type = "Arithmetic Operations"
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculationg_type}")
        return a * b

    