class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, roman_number):
        roman_numerals = {"I": 1,
                          "V": 5,
                          "X": 10,
                          "L": 50,
                          "C": 100,
                          "D": 500,
                          "M": 1000
                          }
        int_value = 0

        for i in range(len(roman_number)):
            if roman_number[i] in roman_numerals:
                if i + 1 < len(roman_number) and roman_numerals[roman_number[i]] < roman_numerals[roman_number[i + 1]]:
                    int_value -= roman_numerals[roman_number[i]]
                else:
                    int_value += roman_numerals[roman_number[i]]
            else:
                print("Invalid input.")

        return cls(int_value)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        return cls(int(value))


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))