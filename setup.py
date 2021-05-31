import setuptools 

with open('README.txt', 'r') as fh:
  long_description = fh.read()

setuptools.setup(
  name="macromrit",
  version="1.0.0",
  author="C.Amrit Subramanian",
  author_email="amritsubramanian.c@gmail.com",
  description="A tiny but compact file writting library",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/macromrit/python_package_amrit",
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
)
 
