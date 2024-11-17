import os
import zipfile
import pathlib
import rarfile
 zip_src=c:\Users\zz\Downloads\500.zip
dst_dir ="C:\Users\zz\OneDrive\桌面\1\output"
def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            if pathlib.Path(file).suffix == '.zip':
                print(os.path.join(dst_dir, file), os.path.join(dst_dir, pathlib.Path(file).parent))
                unzip_file(os.path.join(dst_dir, file), os.path.join(dst_dir, pathlib.Path(file).parent))
            fz.extract(file, dst_dir)
    else:
        print('This is not zip')
 
 
# unzip_file("D:\test.zip", "D:\temp")