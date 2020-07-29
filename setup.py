import setuptools


def readme():
    with open('README.md') as f:
        return f.read()


setuptools.setup(
    name='oopsgenie',
    version='0.1.0',
    description='Functions to run analysis on an exported OpsGenie alert CSV',
    long_description=readme(),
    url='https://github.com/tlugger/oopsgenie',
    author='tlugger, dianaabishop',
    author_email='notnottyler@gmail.com',
    keywords=['opsgenie'],
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
    packages=setuptools.find_packages("oopsgenie"),
    install_requires=[
        'fuzzywuzzy',
    ],
    entry_points={
        'console_scripts': [
            'oopsgenie = oopsgenie.oopsgenie:main'
        ]
    }
)