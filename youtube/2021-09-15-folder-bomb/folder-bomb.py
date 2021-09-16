import os

# uncomment the 'desktop =' line for your OS before running

# windows desktop
# desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# mac desktop
# desktop = os.path.join(os.path.expanduser("~"), "Desktop")

i = 1

while True:
    new_folder = 'Virus'+str(i)
    folder_path = os.path.join(desktop, new_folder)
    os.mkdir(folder_path)
    i += 1
