from pathlib import Path
from time import ctime
import shutil

source = ""
target = ""

shutil.copy(source, target)
path = Path("libary_python/path.py")

print(ctime(path.stat().st_ctime))

