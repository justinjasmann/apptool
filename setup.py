import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="apptool",
    version="1.0",
    author="Justin Jasmann",
    author_email="justin.jasmann@gmail.com",
    description="A simple Android app tool",
    long_description=long_description,
    long_description_content_type="text/plain",
    url="https://github.com/justinjasmann/apptool",
    packages=setuptools.find_packages(),
    classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
    ],
)