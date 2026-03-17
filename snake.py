# This is a placeholder for a snake game, but it only prints a snake pattern.

def print_snake(length=10):
    for i in range(length):
        print(' ' * i + '\ud83d\udc0d')

if __name__ == '__main__':
    print('Welcome to the non-interactive snake demo!')
    print_snake(15)
