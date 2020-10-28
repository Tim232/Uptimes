from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(


    name='uptimes',

    version='1.0.0',

    description='A small python3 package for uptimes.',
    license="MIT",
    author='Tim232',

    author_email='endbot4023@gmail.com',
    url='https://github.com/Tim232/Uptimes',

    download_url='https://github.com/Tim232/Uptimes',

    long_description=long_description,
    long_description_content_type='text/markdown',

    install_requires=[],

    packages=find_packages(),

    keywords=['easy''uptime','uptimes'],

    python_requires='>=3',



    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        #'Development Status :: 3 - Alpha',
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
    ],
)
