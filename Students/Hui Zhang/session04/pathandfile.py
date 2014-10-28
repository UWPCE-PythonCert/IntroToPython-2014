
import pathlib
path_string = str(pth.absolute()) + '/'
for f in pth.iterdir():
        print path_string + str(f)
