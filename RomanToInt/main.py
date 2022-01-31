# IV:4, IX:9, XL:40, XC:90, CD:400, CM:900
rom_input = str(input("Enter the Roman numeral : "))


def romToInt(string: str) -> int:
    rom_d = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    x = 0

    for i in rom_input:
        x += rom_d[i]

    if "IV" in string or "IX" in string:
        x -= 2
    if "XL" in string or "XC" in string:
        x -= 20
    if "CD" in string or "CM" in string:
        x -= 200

    return x

print(romToInt(rom_input))
