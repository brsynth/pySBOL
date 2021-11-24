from setuptools import setup
from os import path, chdir
from sys import maxsize, version, version_info
# To use a consistent encoding
from codecs import open
# Determine if Windows or Mac
import platform

here = path.abspath(path.dirname(__file__))


## INFOS ##
package     = 'pysbol'
descr       = 'A module for reading, writing, and constructing genetic designs according to the standardized specifications of the Synthetic Biology Open Language (SBOL).'
url         = 'https://github.com/brsynth/pySBOL'
authors     = 'Joan Hérisson'
corr_author = 'joan.herisson@univ-evry.fr'

## LONG DESCRIPTION
# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

def get_version():
    with open(
        path.join(
            here,
            'CHANGELOG.md'
        ),
        'r'
    ) as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith('##'):
            from re import search
            m = search("\[(.+)\]", line)
            if m:
                return m.group(1)

def get_config():
    if maxsize == 2147483647:
        python_interpreter_architecture = 32
    elif maxsize == 9223372036854775807:
        # May not detect Windows x64 (maxsize = 2147483647)!
        python_interpreter_architecture = 64
    else:
        python_interpreter_architecture = 0
    if version_info[0] == 2:
        python_version = 2
    elif version_info[0] == 3:
        python_version = 3
    else:
        python_version = 0
    if platform.system() == 'Darwin':
        platform_system = 'macOS'
    elif platform.system() == 'Windows':
        platform_system = 'Windows'
    else:
	    platform_system = 'Linux'
    return (platform_system, python_interpreter_architecture, python_version)

config = get_config()

# Reconstruct path to binaries based on the system and Python interpreter architecture
package_dir = "%s_%d_%d" %(config[0], config[1], config[2])

src_dir = package
if platform.system() == 'Windows':
    chdir(path.join(here, src_dir, 'lib', 'Windows'))
    package_data={
        src_dir: ['_libsbol.pyd', 'libsbol.py'],
        # 'sbol.test': ['*.*', 'SBOL2/*.*', 'SBOL2_bp/*.*', 'SBOL2_ic/*.*', 'SBOL2_nc/*.*']
    }
elif platform.system() == 'Darwin':
    chdir(path.join(here, src_dir, 'lib', 'macOS'))
    package_data={
        src_dir: ['_libsbol.so', 'libsbol.py'],
        # 'sbol.test': ['*.*', 'SBOL2/*.*', 'SBOL2_bp/*.*', 'SBOL2_ic/*.*', 'SBOL2_nc/*.*']
    }
elif platform.system() == 'Linux':
    chdir(path.join(here, src_dir, 'lib', 'Linux'))
    package_data={
        src_dir: ['_libsbol.so', 'libsbol.py'],
        # 'sbol.test': ['*.*', 'SBOL2/*.*', 'SBOL2_bp/*.*', 'SBOL2_ic/*.*', 'SBOL2_nc/*.*']
    }

chdir(here)

setup(
    name                          = package,
    version                       = get_version(),
    author                        = authors,
    author_email                  = corr_author,
    description                   = descr,
    long_description              = long_description,
    long_description_content_type = 'text/markdown',
    url                           = url,
    # packages                      = [package],
    packages                      = [src_dir],
    package_data                  = package_data,
    # package_dir                   = {package: 'sbol'},
    # include_package_data          = True,
    package_dir                   = {package: package},
    include_package_data          = True,
    test_suite                    = 'pytest',
    license                       = 'Apache 2.0',
    classifiers                   = [
        'Programming Language :: Python :: 3',
        'License :: Apache 2.0',
        'Operating System :: OS Independent',
    ],
    python_requires               = '>=3.7, <3.8',
)
