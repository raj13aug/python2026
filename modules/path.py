from pathlib import Path

path = Path("ecom\__init__.py")
print(path.exists())
print(path.is_file())
print(path.is_dir())
print(path.absolute())

print(path.name)
print(path.stem)
print(path.parent)
print(path.suffix)