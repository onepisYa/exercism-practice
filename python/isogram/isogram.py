def is_isogram(string):
    # 1
    # string = string.lower().replace(' ', '').replace('-', '').replave('_','')

    # 2
    # string = string.lower()
    # r_string = [' ', '-', '_']
    # string = "".join(filter(lambda x: x not in r_string, string))

    # 3
    r_string = [' ', '-', '_']

    def convert(string, i=0) -> str:
        if i > 2:
            return string
        string = string.replace(r_string[i], '')
        i += 1
        return convert(string, i)

    string = convert(string).lower()

    return len(string) == len(set(string))
