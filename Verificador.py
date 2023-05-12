import sys

def are_files_equal(file_path_1, file_path_2):
    with open(file_path_1, 'rb') as file1, open(file_path_2, 'rb') as file2:
        while True:
            byte1 = file1.read(1)
            byte2 = file2.read(1)
            if byte1 != byte2:
                print(byte1)
                print(byte2)
                return False
            if not byte1:
                break
    return True

val = are_files_equal("LaBiblia.txt", "descomprimido_elmejorprofesor.txt")

if val:
    print('ok')
else:
    print('nok')