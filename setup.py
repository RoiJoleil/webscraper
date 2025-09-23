from setuptools import setup, find_packages

setup(
    name='webscraper',
    version='0.2.1',
    author='Joel Gyhra',
    description='A helper to scraping the web and beyond.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/RoiJoleil/webscraper.git',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    install_requires=[
        "spacy",
        "https://github.com/explosion/spacy-models/releases/download/de_core_news_sm-3.6.0/de_core_news_sm-3.6.0-py3-none-any.whl"
    ]
)