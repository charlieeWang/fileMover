import os
from shutil import copy
from sys import argv

def move_files(dir, dst):
    """
    To iterate over every files (in here is .jpg / .mp4 )
    in a given directory (dir), and copy them to another folder (dst).

    for example, tree structure like this:

    Album
    ├─2018
    │  ├─07
    │  │  ├─07
    │  │  ├─08
    │  │  ├─09
    │  │  ├─10
    │  │  ├─11
    │  │  ├─13
    │  │  └─14
    └─2019
        ├─01
        │  └─17
        ├─02
        │  ├─01
        │  ├─09
        │  └─31
        └─09
    """
    for root, dirs, files in os.walk(dir):
        for name in files:
            # jpg and mp4 files
            if (os.path.splitext(name)[1].lower() in ('.jpg', '.jpeg', '.mp4')):
                # copy to dst
                if not (os.path.exists(os.path.join(dst, name))):
                    file_path = os.path.join(root, name)
                    copy(file_path, dst)

if __name__ == '__main__':
    if(len(argv) == 3):
        print(argv)
        move_files(argv[1], argv[2])
    else:
        output_path = os.getcwd() + '/../all'
        if not(os.path.exists(output_path)):
            os.mkdir(output_path)
        move_files(os.getcwd(), output_path)
