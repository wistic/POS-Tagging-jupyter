import os


def dirWalk(source_path, file_list):
    listing = os.listdir(source_path)
    for entry in listing:
        absolute_path = os.path.join(source_path, entry)
        if os.path.isdir(absolute_path):
            dirWalk(absolute_path, file_list)
        else:
            if absolute_path.split('.')[-1] == 'xml':
                file_list.append(absolute_path)
    return file_list
