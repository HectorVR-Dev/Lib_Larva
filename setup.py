from setuptools import setup, find_packages

setup(
    name="Larva_Motion",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Dependencias, por ejemplo:
        # "numpy>=1.18.0",
    ],
    author="",
    author_email="hectordaniel1112@gmail.com",
    description="A simple example library",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/tu_usuario/my_library",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
