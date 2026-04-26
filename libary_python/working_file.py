from pathlib import Path

path = Path("libary_python")

for p in path.iterdir():
    print(p)
    

paths = [ p for p in path.iterdir() if p.is_dir() ]
print(paths)

paths = [ p for p in path.rglob("*.py")]
print(paths)