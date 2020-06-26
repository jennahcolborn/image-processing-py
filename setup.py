#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup, find_packages
setup(
    name="PixPro",
    version="0.1",
    packages=find_packages(),
    scripts=["pixpro.py"],
    # metadata to display on PyPI
    author="Aanica Gonzales-Rogers, Jennah Colborn",
    author_email="asgonzal@caltech.edu, jcolborn@caltech.edu",
    description="This is a package designed to provide statistics related to the pixel color values of a jpeg image.",
    keywords="rbg bw histogram photo image",
    project_urls={
        "Documentation": "https://docs.google.com/PixPro/",
        "Source Code": "https://github.com/jennahcolborn/image-processing-py.git",
    },
    classifiers=[
        "License :: OSI Approved :: Python Software Foundation License"
    ]
    # could also include long_description, download_url, etc.
)

