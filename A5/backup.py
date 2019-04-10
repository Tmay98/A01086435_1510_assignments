"""backup function"""

# Tommy May
# A01086435


def backup(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print('File not found')
    else:
        backup_filename = filename[:-4] + '.bak'
        with open(backup_filename, 'w') as f_obj:
            f_obj.write(contents)
        print('generated ' + backup_filename)


def main():
    backup('stuff.txt')


if __name__ == '__main__':
    main()
