import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='gpt_traceback',
    author='Franz Krekeler',
    author_email='filmfranz@findmeontwitter.com',
    description='Debug your exceptions with GPT',
    keywords='gpt, jupyter, colab, traceback, debugging',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/franz101/gpt-exception',
    project_urls={
        'Documentation': 'https://github.com/franz101/gpt-exception',
        'Bug Reports':
        'https://github.com/franz101/gpt-exception/issues',
        'Source Code': 'https://github.com/franz101/gpt-exception',
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=['requests','rich'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=examplepy:main',
    # You can execute `run` in bash to run `main()` in src/examplepy/__init__.py
    #     ],
    # },
)
