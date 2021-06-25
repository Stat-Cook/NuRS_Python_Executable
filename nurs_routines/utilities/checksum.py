import hashlib
import tarfile

class ChecksumException(Exception):
    pass


def tar_folder(folder: str, tar_name: str) -> None:
    """
    Convert a folder to a tarball (".tar.gz" file)
    Parameters
    ----------
    folder: str
        Target folder to compress
    tar_name: str
        Name of the archive

    Returns
    -------
    None
    """
    with tarfile.open(f"{tar_name}.tar.gz") as tar:
        tar.add(folder, tar_name)


def calculate_checksum(file: str) -> str:
    """
    Calculate a checksum for verifying file integrity
    Parameters
    ----------
    file: str
        File name for file to hash

    Returns
    -------
    str
    """
    hasher = hashlib.sha512()
    with open(file, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def checksum_to_file(file: str, checksum_path: str):
    check = calculate_checksum(file)
    with open(checksum_path, "w") as f:
        f.write(check)


def compare_checksum(file: str, checksum_path: str):
    check = calculate_checksum(file)
    with open(checksum_path, "r") as f:
        content = f.read()

    if check != content:
        raise ChecksumException("Calculated checksum does not match supplied value.  Use with caution.")
