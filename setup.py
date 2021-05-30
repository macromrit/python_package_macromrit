import setuptools 

with open('README.txt', 'r') as fh:
  long_description = fh.read()

setuptools.setup(
  name="amrit",
  cersion="0.0.1",
  author="C.Amrit Subramanian",\
  author_email="amritsubramanian.c@gmail.com",
  description="A tiny but compact file writting library",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="",
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3 "
  ],
  python_requires='>=3.6',
)
 
