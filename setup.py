# !/usr/bin/env python3
# coding:utf-8

from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python',

]

setup(
    name='process-me',
    version='0.3',
    description='Simple Platform Independent Python package',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read()+'\n\nRead more at https://github.com/singhsidhukuldeep/process-me',
    long_description_content_type="text/markdown",
    url='',
    author='',
    author_email='',
    classifiers=classifiers,
    keywords='stay awake',
    packages=find_packages(),
    install_requires=['pyautogui', 'tqdm'],
    zip_safe=False,
)