from setuptools import setup, find_packages

setup(
    name='inspiring_quotes',
    version='1.5.1',
    description='A simple Python package for retrieving random inspirational quotes.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='cyberdeeb',
    author_email='abrahamdeeb@gmail.com',
    url='https://github.com/cyberdeeb/inspiring-quotes',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'inspiring_quotes': ['quotes_list.json'],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='quotes inspirational motivational wisdom positivity self-improvement',
    python_requires='>=3.6',
)
