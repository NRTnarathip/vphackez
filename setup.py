import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vphackez",
    version='0.1',
    script=['vphackez'],
    author='Viper Hacker',
    author_email='viperhackerth@gmail.com',
    description='A Tools Viper Hacker @onehack',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/NRTnarathip/vphackez.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programing Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
