import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='code4th-datasource-air4thai',
    version='0.2',
    description='A datasource package for retrieving data from http://air4thai.pcd.go.th',
    author='Pattarawat Chormai',
    author_email='pat.chormai@gmail.com',
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
