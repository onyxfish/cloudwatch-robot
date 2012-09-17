#!/usr/bin/env python

from setuptools import setup

setup(
    name='cloudwatch-robot',
    version='0.0.1',
    description='A script to monitor metrics using Amazon AWS\'s CloudWatch service.',
    #long_description=open('README').read(),
    author='Christopher Groskopf',
    author_email='staringmonkey@gmail.com',
    #url='http://blog.apps.chicagotribune.com/',
    license='MIT',
    scripts=[
        'cloudwatch-robot'
    ],
    install_requires = [
        'boto==2.5.2',
        'psutil==0.6.1'
    ]
)
