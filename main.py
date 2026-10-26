
import hashlib
from pathlib import Path


def calculate_sha256(file_path):
    """Calculate a file's SHA-256 hash."""
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def main():
    print("=" * 40)
    print("       FILE INTEGRITY CHECKER")
    print("=" * 40)

    file_name = input("Enter the file path: ").strip().strip('"')
    file_path = Path(file_name)

    if not file_path.is_file():
        print("Error: File not found.")
        return

    original_hash = calculate_sha256(file_path)
    print("\nSHA-256 Hash:", original_hash)

    print("\nSave this hash for future comparison.")
    print("If the file changes, its hash will usually change.")


if __name__ == "__main__":
    main()
