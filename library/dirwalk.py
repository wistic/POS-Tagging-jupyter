import os


def dirWalk(source_path, output_path, file_list):
    listing = os.listdir(source_path)
    for entry in listing:
        absolute_path = source_path + entry
        if os.path.isdir(absolute_path):
            if absolute_path[-1] != '/':
                absolute_path = absolute_path + '/'
            dirWalk(absolute_path, output_path, file_list)
        else:
            if absolute_path.split('.')[-1] == 'xml':
                file_entry = (source_path, entry, output_path)
                file_list.append(file_entry)
    return file_list
