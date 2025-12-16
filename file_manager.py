from pathlib import Path


def list_files(path: Path):
    """
    List files and directories inside a given directory.

    Args:
        path (Path): Directory path

    Returns:
        (bool, list | str): Operation success and list of items or error message
    """
    if not path.exists():
        return False, 'The provided path does not exist.'

    if not path.is_dir():
        return False, 'The provided path is not a directory.'

    items = list(path.iterdir())
    return True, items


def create_file(path: Path, filename: str):
    """
    Create a new file in the given directory.

    Args:
        path (Path): Directory path
        filename (str): File name

    Returns:
        (bool, str): Operation success and descriptive message
    """
    if not filename.strip():
        return False, 'Invalid file name.'

    if not path.exists():
        return False, 'The provided path does not exist.'

    file_path = path / filename

    if file_path.exists():
        return False, 'The file already exists.'

    try:
        file_path.touch()
        return True, f'File "{file_path.name}" created successfully.'
    except PermissionError:
        return False, 'Permission denied while creating the file.'
    except OSError:
        return False, 'System error occurred while creating the file.'


def rename_file(path: Path, current_name: str, new_name: str):
    """
    Rename a file or directory.

    Args:
        path (Path): Directory path
        current_name (str): Current file or directory name
        new_name (str): New name

    Returns:
        (bool, str): Operation success and descriptive message
    """
    if not path.exists():
        return False, 'The provided path does not exist.'

    source = path / current_name

    if not source.exists():
        return False, 'The selected file or directory does not exist.'

    destination = path / new_name

    if destination.exists():
        return False, 'A file or directory with the new name already exists.'

    try:
        source.rename(destination)
        return True, f'"{current_name}" renamed to "{new_name}".'
    except PermissionError:
        return False, 'Permission denied while renaming.'
    except OSError:
        return False, 'System error occurred while renaming.'


def remove_file(path: Path, filename: str):
    """
    Remove a file or an empty directory.

    Args:
        path (Path): Directory path
        filename (str): File or directory name

    Returns:
        (bool, str): Operation success and descriptive message
    """
    if not path.exists():
        return False, 'The provided path does not exist.'

    target = path / filename

    if not target.exists():
        return False, 'The selected file or directory does not exist.'

    if target.is_file():
        try:
            target.unlink()
            return True, f'File "{target.name}" removed successfully.'
        except PermissionError:
            return False, 'Permission denied while removing the file.'
        except OSError:
            return False, 'System error occurred while removing the file.'

    if target.is_dir():
        items = list(target.iterdir())
        if items:
            return False, f'Directory "{target.name}" is not empty.'

        try:
            target.rmdir()
            return True, f'Directory "{target.name}" removed successfully.'
        except PermissionError:
            return False, 'Permission denied while removing the directory.'
        except OSError:
            return False, 'System error occurred while removing the directory.'
