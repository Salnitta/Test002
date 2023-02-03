def compression(path_in: str, path_out: str):
    with open (path_in, 'r') as data:
        data = data.read()
    print(f'Данные для сжатия: {data}')
    result = ''
    count = 1
    for i in range(len(data) - 1):
        if data[i] == data[i + 1]:
            count += 1
        else:
            result += str(count) + data[i]
            count = 1
    result += str(count) + data[len(data) - 1]
    with open (path_out, 'w') as data:
        data.write(result)
    return result

def expansion(path_in: str, path_out: str):
    with open (path_in, 'r') as data:
        data = data.read()
    print(f'Данные для восстановления: {data}')
    result = ''
    count = ''
    for i in range(len(data)):
        if data[i].isdigit() == True:
            count += data[i]
        else:
            count = int(count)
            result += data[i] * count
            count = ''
    with open (path_out, 'w') as data:
        data.write(result)
    return result
