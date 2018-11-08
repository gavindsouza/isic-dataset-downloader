ISIC Dataset Downloader
==================================================
*"Just a micro tool to download, extract and segregate the ISIC dataset!"*

Had made this for my project, if this helps you, then that's great!


Table of Contents
~~~~~~~~~~~~~~~~~

-  `Installation`_
-  `Usage`_
-  `Dependencies`_
-  `License`_

Installation
~~~~~~~~~~~~

Clone the git repository:

.. code:: console

   $ git clone https://github.com/gavindsouza/isic-dataset-downloader.git
   $ cd isic-dataset-downloader

Install necessary dependencies

.. code:: console

   $ pip install -r requirements.txt

Go ahead and install as follows:

.. code:: console

   $ python setup.py install

Usage
~~~~~
If package is installed, go ahead and type the following in the console else just change to module directory

.. code:: console

   $ python -m isic_dataset_downloader


The dataset will be acquired from |ISIC_link|'s Task 3.

`The International Skin Imaging Collaboration: Melanoma Project`
is an academia and industry partnership designed to facilitate
the application of digital skin imaging to help reduce melanoma mortality.

ISIC holds a competition for melanoma detection and classification every year.

`The goal of this recurring challenge is to help participants develop image analysis tools to enable the automated
diagnosis of melanoma from dermoscopic images.`

*Links for individual sets:*

- |train_link|

- |test_link|

- |val_link|

.. |ISIC_link| raw:: html

   <a href="https://challenge2018.isic-archive.com/task3/" target="_blank">ISIC</a>

.. |train_link| raw:: html

   <a href="https://challenge2018.isic-archive.com/task3/train/" target="_blank">Train Data</a>

.. |test_link| raw:: html

   <a href="https://challenge2018.isic-archive.com/task3/test/" target="_blank">Test Data</a>

.. |val_link| raw:: html

   <a href="https://challenge2018.isic-archive.com/task3/validation/" target="_blank">Validation Data</a>


Dependencies
~~~~~~~~~~~~~

- requests

.. _Dependencies: requirements.txt

License
~~~~~~~

This code has been released under the `MIT License`_.

.. _MIT License: LICENSE
