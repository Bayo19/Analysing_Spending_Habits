import os
def grab_file():
    csv_files_in_dir = []
    for root, dirs, files in os.walk('.'):
        for name in files:
            if 'csv_files' in root and '.csv' in name:
                csv_files_in_dir.append(os.path.join(root,name))
    return ['.'+i.replace('\\','/') for i in csv_files_in_dir] # hacky reformatting of filepath
                

print(grab_file())