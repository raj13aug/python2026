from pathlib import Path

path = Path("modules/ecom")

# for i in path.iterdir():
#     print(i)
    
path1 = [p for p in path.iterdir() if path.is_dir()]
print(path1)
path = [ p for p in path.rglob("*.txt")]