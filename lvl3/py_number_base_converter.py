def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    try:
        if not 2 <= from_base <= 36 or not 2 <= to_base <= 36 or not number:
            return "ERROR"

        n = int(number, from_base)
        result = ""
        while n:
            result = digits[n % to_base] + result
            n //= to_base
        return result or "0"
    except ValueError:
        return "ERROR"


# Tests
print(number_base_converter("1010", 2, 10))  # 10
print(number_base_converter("FF", 16, 10))   # 255
print(number_base_converter("255", 10, 16))  # FF
print(number_base_converter("101", 2, 16))   # 5
print(number_base_converter("Z", 36, 10))     # 35
print(number_base_converter("102", 2, 10))   # ERROR
print(number_base_converter("123", 1, 10))   # ERROR
print(number_base_converter("", 10, 2))      # ERROR
print(number_base_converter("0", 10, 2))     # 0
