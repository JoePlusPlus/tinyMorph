import os

for file in os.listdir('trainA'):
    new_file = file.replace('train_', '')
    path = os.path.join('trainA', file)
    new_path = os.path.join('trainA', new_file)
    os.rename(path, new_path)
