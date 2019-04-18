#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  setuptools import setup, find_packages


setup(
    name='tbbsm',
    version='0.6',
    description='Blog System base on Django',
    author='tbbsm',
    author_email='msqming@163.com',
    license='MIT',
    packages=find_packages('tbbsm'),
    package_dir={'': 'tbbsm'},
    include_package_data=True,  # 方法二 配合 MANIFEST.in文件
    install_requires=[
        'django==2.1',
        'pymysql=='
        'pandas=='
        'numpy=='
        'xlrd=='
        'gunicorn==19.8.1',
        'supervisor==4.0.0dev0',
        #'xadmin==2.0.1',
        #'mysqlclient==1.3.12',
        # 'django-ckeditor==5.4.0',
        # 'django-rest-framework==0.1.0',
        # 'django-redis==4.8.0',
        # 'django-autocomplete-light==3.2.10',
        # 'mistune==0.8.3',
        # 'Pillow==4.3.0',
        # 'coreapi==2.3.3',
        # django-redis==4.8.0',
        # 'hiredis==0.2.0',
        # debug
        # 'django-debug-toolbar==1.9.1',
        # 'django-silk==2.0.0',
    ],
    scripts=[
        'tbbsm/manage.py',
        'tbbsm/tbbsm/wsgi.py',
    ],
    entry_points={
        'console_scripts': [
            'tbbsm_manage = manage:main',
        ]
    },
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Blog :: Django Blog',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',
    ],

)

