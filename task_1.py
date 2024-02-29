def sum_number(num):
    num_list = []
    for i in range(1, num + 1):
        num_list.append(str(i) * i)
    return ''.join(num_list[:num])


if __name__ == '__main__':
    print(sum_number(5))
