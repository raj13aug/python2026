from pathlib import Path

path = Path("../class/abstract.py")

print(path.is_file())
print(path.is_dir())

print(path.stem)
print(path.suffix)
print(path.absolute)
 
path = path.with_name("file.txt")
print(path)