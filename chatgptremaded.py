import os
import argparse

def main():
    parser = argparse.ArgumentParser(description='Print information about files in a directory')
    parser.add_argument('dir', help='the directory to scan')
    parser.add_argument('-f', '--format', choices=['Y', 'N'], default='N', help='the format to display file sizes (Y or N)')
    parser.add_argument('-s', '--sort', choices=['asc', 'desc'], default='desc', help='the sort order (asc or desc)')

    args = parser.parse_args()

    try:
        files = [f for f in os.scandir(args.dir) if f.is_file()]
    except OSError as e:
        print(f'Error: {e}')
        return

    files = sorted(files, key=lambda f: os.path.getsize(f), reverse=args.sort == 'desc')

    for f in files:
        if args.format == 'Y':
            print(f.name, os.path.getsize(f), "bytes")
        elif args.format == 'N':
            size = format_file_size(f)
            print(f.name, size)

def format_file_size(file):
    size = os.path.getsize(file)
    units = ['bytes', 'KB', 'MB', 'GB']
    i = 0
    while size > 1024 and i < len(units)-1:
        size /= 1024
        i += 1
    return f'{size:.2f} {units[i]}'

if __name__ == '__main__':
    main()
