ALPHABET = "АБВГДЕЖЗИЙКЛМОПРСТУФХЦЧШЩЪЫЬЭЮЯ "


def calc(input: str) -> list:
    input_len = len(input)
    result = []
    counter = 1
    j = 0
    while len(input) != 0:
        while j < len(input):
            if input[j] == input[0]:
                counter += 1
            j += 1
        if len(input):
            result.append((round(counter / input_len, 6), input[0]))
            input = input.replace(input[0], '')
            counter = 1
            j = 1
    result.sort(reverse=True)
    return result


if __name__ == "__main__":
    text = ""
    with open("code6.txt", "r", encoding="utf-8") as file:
        text = file.read()
    result_list = calc(text.replace('\n', ''))
    for elem in result_list:
        print(elem)
