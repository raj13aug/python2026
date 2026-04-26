from pathlib import Path
from zipfile import ZipFile

with ZipFile("file.zip", "w") as zip:
    for path in Path("libary_python").rglob("*"):
        zip.write(path)