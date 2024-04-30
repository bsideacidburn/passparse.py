import os

def search_files(directory, output_file):
    extensions = ['.config', '.bat', '.ps1', '.sql']
    files_with_password = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(tuple(extensions)):
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    try:
                        content = f.read().decode('utf-8')
                        if 'password' in content.lower():
                            files_with_password.append(file_path)
                    except UnicodeDecodeError:
                        pass

    with open(output_file, 'w') as f:
        for file_path in files_with_password:
            f.write(file_path + '\n')

if __name__ == '__main__':
    directory = input('Enter the directory to parse: ')
    output_file = input('Enter the name of the output file: ')
    search_files(directory, output_file)
