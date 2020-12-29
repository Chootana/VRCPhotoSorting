"""
sort_by_month.py

Copyright (c) 2020 chootana

This software is released under the MIT License.
http://opensource.org/licenses/mit-license.php
"""

import os
import glob 
import shutil 

if __name__ == '__main__':
    dir_base_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    vrc_dir_path = '{}\\VRChat'.format(dir_base_path)
    file_base_path = '*.png'

    file_paths = glob.glob('{}\\{}'.format(vrc_dir_path, file_base_path))
    print('# of new pictures: {}'.format(len(file_paths)))  
    if not file_paths:
        print('There are not new photos.')
    
    for file_path in file_paths:
        file_name = file_path.split('\\')[-1]

        if not '_' in file_name:
            print('skip: {}'.format(file_name))
            continue
        
        month = file_name.split('_')[-2]

        month_dir_path = '{}\\{}'.format(vrc_dir_path, month)
        if not os.path.exists(month_dir_path):
            print('make direcotry: {}'.format(month_dir_path))
            os.makedirs(month_dir_path)
        
        dst_file_path = '{}\\{}'.format(month_dir_path, file_name)
        shutil.move(file_path, dst_file_path)


    print('done.')
