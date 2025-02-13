import os
import sys
from collections import defaultdict

pairs_dict = defaultdict(list)

# yoinked from https://stackoverflow.com/questions/1094841/get-a-human-readable-version-of-a-file-size
def sizeof_fmt(num, suffix="B"):
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:>6.1f} {unit:>2}{suffix:<2}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

def main():
    
    yeet = 'yeet' in sys.argv
    
    # Walk the media folder and store all files in a dict of inode and list of file paths that share that inode
    for root, dirs, files in os.walk("/mnt/tank/media/"):
        for file in files:
            path = f"{root}/{file}"
            pairs_dict[os.stat(path).st_ino].append(path)

    size_of_junk = 0

    # Delete all files where hardlinks (number of files sharing inode) do not exceed 1 (aka it isn't hardlinked)
    for k,v in pairs_dict.items():
        if len(v) != 1:
            continue

        file_path = v[0]

        # Dont delete metadata, such as posters and stuff
        if file_path.startswith('/mnt/tank/media/links/'):
            continue
        
        s = os.stat(file_path).st_size
        size_of_junk += s 
        print(f'Deleting: {sizeof_fmt(s)} {file_path}')

        if yeet:
            os.unlink(file_path)
    
    print('Size cleared:', sizeof_fmt(size_of_junk))


if __name__ == '__main__':
    main()
