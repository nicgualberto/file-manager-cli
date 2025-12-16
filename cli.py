import argparse
from pathlib import Path
from file_manager import (
    list_files,
    create_file,
    rename_file,
    remove_file
)


def main():
    parser = argparse.ArgumentParser(
        description='File Manager - CLI'
    )

    subparsers = parser.add_subparsers(
        dest='command',
        required=True
    )

    # list command
    list_cmd = subparsers.add_parser(
        'list',
        help='List files and directories'
    )
    list_cmd.add_argument('path', type=Path)

    # create command
    create_cmd = subparsers.add_parser(
        'create',
        help='Create a new file'
    )
    create_cmd.add_argument('path', type=Path)
    create_cmd.add_argument('filename')

    # rename command
    rename_cmd = subparsers.add_parser(
        'rename',
        help='Rename a file or directory'
    )
    rename_cmd.add_argument('path', type=Path)
    rename_cmd.add_argument('current_name')
    rename_cmd.add_argument('new_name')

    # remove command
    remove_cmd = subparsers.add_parser(
        'remove',
        help='Remove a file or empty directory'
    )
    remove_cmd.add_argument('path', type=Path)
    remove_cmd.add_argument('filename')

    args = parser.parse_args()

    if args.command == 'list':
        success, message = list_files(args.path)

    elif args.command == 'create':
        success, message = create_file(
            args.path,
            args.filename
        )

    elif args.command == 'rename':
        success, message = rename_file(
            args.path,
            args.current_name,
            args.new_name
        )

    elif args.command == 'remove':
        success, message = remove_file(
            args.path,
            args.filename
        )

    print(message)


if __name__ == '__main__':
    main()
