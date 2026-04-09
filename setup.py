from setuptools import setup, find_packages

setup(
    name='sanskrit_cleaner',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'psycopg2-binary',  # For PostgreSQL connection
        'pandas',           # For data processing
    ],
    author='Your Name',
    description='A Sandhi-aware Sanskrit pre-processor for LLMs',
    python_requires='>=3.8',
)

