
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    description='contacts-scrapy',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Wilson Pedrosa',
    url='https://github.com/Wilson08/contacts-scrapy',
    download_url='https://github.com/Wilson08/contacts-scrapy',
    version='1.0.1',
    license='MIT',
    keywords='scrapy contact',
    install_requires=[
        'scrapy'
    ],
    packages=find_packages(),
    scripts=[],
    name='contacts-scrapy',
    include_package_data=True
)
