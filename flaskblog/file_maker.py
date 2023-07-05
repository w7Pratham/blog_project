import os
from pathlib import Path

list_of_files = [
    # "main/__init__.py",
    # "main/routes.py",
    # "posts/__init__.py",
    # "posts/routes.py",
    # "posts/forms.py",
    # "users/__init__.py",
    # "users/routes.py",
    # "users/forms.py",
    # "users/utils.py",
    "errors/__init__.py",
    "errors/handlers.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass