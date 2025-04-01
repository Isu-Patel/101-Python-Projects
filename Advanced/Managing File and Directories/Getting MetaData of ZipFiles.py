import zipfile

def meta_info(names):
    with zipfile.ZipFile(names) as zf:
        for info in zf.infolist():
            print(info.filename)

            if info.create_system == 0:
                print('Created by: Windows')
            elif info.create_system == 3:
                system = 'Unix'
            else:
                system = 'Unknown'

            print('System:', system)

            print("Zip Version:", info.create_version)

            print("Compressed Size:", info.compress_size, "bytes")

            print("Uncompressed Size:", info.file_size, "bytes")

            print()

if __name__ == "__main__":
    meta_info('loops.zip')
