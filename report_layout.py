import shutil
from datetime import datetime

def divider(title=''):
    width = shutil.get_terminal_size().columns
    
    if title:
        print(title.center(width, '-'))
    else:
        print('-' * width)
    
def report_header(file_name):
    divider('Email Analysis Report')
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f'File: {file_name}')
    divider()
    

