import os

address_root_folder = input('Ввеите адрес: ')

folders = os.listdir(address_root_folder)

end_file_dict = []


def take_end_file_dict():
    '''
    - получаем библиотеку формата файлов без .txt формата
    :return:
    '''
    for folder in folders:
        folder_path = f'{address_root_folder}\\{folder}'
        directory = os.path.isdir(folder_path)
        if directory:
            folder2 = os.listdir(folder_path)
            for file in folder2:
                folder_path2 = f'{address_root_folder}\\{folder}\\{file}'
                file_split = file.strip().split('.')
                end_file = file_split[-1]
                end_file2 = f'.{end_file}'
                if end_file != 'txt':
                    if end_file2 not in end_file_dict:
                        end_file_dict.append(end_file2)
        else:
            pass

    return end_file_dict


take_end_file_dict()


def rename_file():
    '''
    - примиеняет имя папки к файлам которые внутри:
    :return:
    '''
    for folder in folders:
        name_folder = folder
        folder_path = f'{address_root_folder}\\{folder}'
        all_files_in_folder = os.listdir(folder_path)
        for file in all_files_in_folder:
            file_split = file.strip().split('.')
            end_file = file_split[-1]
            end_file2 = f'.{end_file}'
            name_file = file.replace(end_file2, '')
            if name_file != name_folder:
                if end_file2 in end_file_dict:
                    print(f'{file} - {name_folder}{end_file2}')
                    os.replace(f'{address_root_folder}\\{folder}\\{file}',
                               f'{address_root_folder}\\{folder}\\{name_folder}{end_file2}')
                    print(f'{file} - {name_folder}{end_file2}')
            else:
                pass


rename_file()
