import os
import re
import shutil

# pattern to find a parenthetical group like "(something)"
PAREN_PATTERN = re.compile(r"\(([^()]+)\)")

def rename_folders(base_path):
    for root, dirs, files in os.walk(base_path, topdown=True):
        new_dirs = []
        for d in dirs:
            match = PAREN_PATTERN.search(d)
            if match:
                paren_text = match.group(0)  # the whole "(something)"
                new_name = f"{paren_text.strip()} {PAREN_PATTERN.sub('', d).strip()}"
                old_path = os.path.join(root, d)
                new_path = os.path.join(root, new_name)
                if old_path != new_path:
                    print(f"Renaming: {old_path} -> {new_path}")
                    os.rename(old_path, new_path)
                # skip traversing into this renamed folder
                continue
            # keep unmodified dirs for traversal
            new_dirs.append(d)
        # replace dirs list in-place so os.walk knows which subdirs to traverse
        dirs[:] = new_dirs

if __name__ == "__main__":
    base = input("Enter the base directory to start renaming: ").strip()
    if not os.path.isdir(base):
        print("Invalid directory path.")
    else:
        rename_folders(base)