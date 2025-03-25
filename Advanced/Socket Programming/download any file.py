import os
from ftplib import FTP

ftp_domain = ''
ftp_username = ''
ftp_password = ''

ftp = FTP(ftp_domain)

try:
    with ftp:
        ftp.login(ftp_username, ftp_password)
        ftp.cwd('/home/user/Downloads')
        files = ftp.nlst()
        print("Files in remote Directory: ", files)

        local_directory = "D:/101 Python Course 2025/Advanced/Socket Programming/download file.py"

        for file in files:
            if os.path.isfile(os.path.join(local_directory, file)):
                print(f"Skipping Download (file already exists) {file}")
            else:
                print("Downloading", file)
                local_file_path = os.path.join(local_directory, file)

                with open(local_file_path, 'wb') as local_file:
                    ftp.retrbinary("RETR" + file, local_file.write)

                print("Download Complete: ", local_file_path)

except Exception as e:
    print("An Error Occurred: ", e)

ftp.close()
