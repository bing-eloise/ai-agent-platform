"""第一个实际工具，负责计算"""
def calculator(operation: str, a: float, b: float) -> float:
    """
    简单计算器工具
    operation:
        add
        subtract
        multiply
        divide
    """
    if operation == "add":
        return a + b

    if operation == "subtract":
        return a - b

    if operation == "multiply":
        return a * b

    if operation == "divide":
        if b == 0:
            raise ValueError("division by zero is not allowed")
        return a / b

    raise ValueError(f"unsupported operation: {operation}")