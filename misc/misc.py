def output_preparation(filename: str, amount_info_spaces: int, new_line_between_info: []) -> str:
    res = ''

    file = open(filename, 'r')
    lines = file.readlines()
    file.close()

    max_length = max(len(line) for line in lines)
    margin = 5 * ' '
    amount_info_spaces += len(new_line_between_info)


    while amount_info_spaces > 0:

        for index, line in enumerate(lines, start=1):
            if amount_info_spaces > 0:
                line = line.replace(
                    '\n',
                    ((max_length - len(line)) * ' ') + margin + ('\n' if index in new_line_between_info else '{}\n')
                )
                res += line
                amount_info_spaces -= 1
            else:
                res += line

        if amount_info_spaces != 0:
            res = res[:-1] + '\n'
            res += amount_info_spaces * (((max_length - 1) * ' ') + margin + '{}\n')
            amount_info_spaces = 0
        else:
            break

    return res


if __name__=="__main__":
    print(output_preparation('test.txt', 5, [3]))