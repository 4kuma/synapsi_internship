from random import randint


def main():
    min_value = 1
    max_value = 0

    while min_value > max_value:
        min_value = randint(0, 150)
        max_value = randint(75, 200)

    while True:
        user_input = input(f'Input number in range {min_value} - {max_value}\n')
        try:
            n = int(user_input)
            if n < min_value:
                print(f'Input number is lesser than min value!!!\n')
            elif n > max_value:
                print(f'Input number is greater than max value!!!\n')
            else:
                input_value = n
                break
        except ValueError:
            print("Input is in wrong format!!!\n")


if __name__ == '__main__':
    main()
