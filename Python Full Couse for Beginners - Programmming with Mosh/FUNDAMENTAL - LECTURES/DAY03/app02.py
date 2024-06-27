from pathlib import Path


"""
Absolute path: All the way from root directory 
    c:\program files\Microsoft
    

Relative path: within the package

path = Path("emails")
print(path.mkdir())

"""

path = Path()
for file in path.glob('*'):
    print(file)

