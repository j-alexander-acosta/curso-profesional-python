def del_duplicates(random_list):
    return list(set(random_list))


def main():
    random_list = [ 11, 55, 2, 2, 55]
    print(del_duplicates(random_list))


if __name__ == '__main__':
    main()