import os
from pathlib import Path
import logging

# logging string

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'Kidney_disease_classification'

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/utils/common.py',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'requirements.txt',
    'setup.py',
    '.gitignore',
    'README.md',
    'LICENSE',
    'research/trials.ipynb',
    'templates/index.html',

]

for file in list_of_files:
    file = Path(file)
    filedir, filename = os.path.split(file)

    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Created {filedir} directory for the file: {filename}')

    if (not os.path.exists(file)) or (os.path.getsize(file) == 0):
        with open(file, 'w') as f:
            pass
            logging.info(f'Created empty file: {filename}')
    else:
        logging.info(f'File {filename} already exists')
