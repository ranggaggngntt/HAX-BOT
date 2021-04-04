def main():
    file = input('File: ')
    temp = []
    with open(file, 'r') as f:
        duplicate = f.read().splitlines()
    temp.extend(duplicate)
    temp = list(set(temp))

    print('Wait ....')
    for i in temp:
        if i == '':
            pass
        else:
            save = open('result.txt', 'a')
            save.write(i+'\n')
            save.close()

    return print('Saved As result.txt')