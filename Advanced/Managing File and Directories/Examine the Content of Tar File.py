import tarfile

with tarfile.open("archive.tar", 'r') as tar:
    tar_contents = tar.getnames()
    print("Contents of the tar file:", tar_contents)