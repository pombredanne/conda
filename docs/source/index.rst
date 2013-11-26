.. conda documentation master file, created by
   sphinx-quickstart on Sat Nov  3 16:08:12 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=====
Conda
=====


The `conda` command is the primary interface for managing `Anaconda <http://docs.continuum.io/anaconda/index.html>`_ installations. It can query and search the Anaconda package index and current Anaconda installation, create new Anaconda environments, and install and update packages into existing Anaconda environments.


Installation
-----------
conda is a part of the Anaconda distribution which can be downloaded `here <https://store.continuum.io/cshop/anaconda/>`_.


Getting Started
---------------

To demonstrate the ease of a typical conda workflow, we will create an Anaconda environment
with a version of `NumPy <http://www.numpy.org>`_ different from the default version.

First, we will check our system NumPy version

.. code-block:: bash

    $ python
    Python 2.7.5 |Anaconda 1.6.1 (x86_64)| (default, Jun 28 2013, 22:20:13)
    [GCC 4.0.1 (Apple Inc. build 5493)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import numpy
    >>> numpy.__version__
    '1.7.1'

Next we will create an Anaconda environment using a different version of NumPy

.. code-block:: bash

    $ conda create -p ~/anaconda/envs/test numpy=1.6 anaconda

    Package plan for creating environment at /Users/maggie/anaconda/envs/test:

    The following packages will be downloaded:

    [      COMPLETE      ] |#################################################| 100%

Now we adjust our **PATH** variable to point to the new environment

.. code-block:: bash

    $ export PATH=~/anaconda/envs/test/bin/:$PATH

Finally, we check the version again

.. code-block:: bash

    $ python
    Python 2.7.5 |Anaconda 1.6.1 (x86_64)| (unknown, Jan 10 2013, 12:19:03)
    [GCC 4.0.1 (Apple Inc. build 5493)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import numpy
    >>> numpy.__version__
    '1.6.2'


User Guide
----------
.. toctree::
   :maxdepth: 1

   intro
   examples
   build


Reference Guide
---------------

.. toctree::
   :maxdepth: 2

   commands

Presentations & Blog Posts  
--------------------------

`Packaging and Deployment with conda - Travis Oliphant <https://speakerdeck.com/teoliphant/packaging-and-deployment-with-conda>`_

 
`Python 3 support in Anaconda - Ilan Schnell <http://continuum.io/blog/anaconda-python-3>`_  

`New Advances in conda - Ilan Schnell <http://continuum.io/blog/new-advances-in-conda>`_

`Python Packages and Environments with conda - Bryan Van de Ven <http://continuum.io/blog/conda>`_


Requirements
------------

* python 2.7 or 3.3
* pycosat
* pyyaml



License Agreement
-----------------

conda is distributed under the `OpenBSD license <http://opensource.org/licenses/bsd-license.php>`_.


Indices and tables
------------------

* :ref:`genindex`
* :ref:`search`
