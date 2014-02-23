===============================
egg
===============================

.. image:: https://badge.fury.io/py/egg.png
    :target: http://badge.fury.io/py/egg
    
.. image:: https://travis-ci.org/rgbkrk/egg.png?branch=master
        :target: https://travis-ci.org/rgbkrk/egg

.. image:: https://pypip.in/d/egg/badge.png
        :target: https://pypi.python.org/pypi/egg


This package isn't meant to be installed, but is instead meant to be friendly name squatting against pip typos (especially misconfigured installs of packages from git). Upon installing this package, you should see the warning message:

.. code-block:: bash

  $ pip install egg
  Downloading/unpacking egg
    Downloading egg-0.1.0.tar.gz
    Running setup.py (path:/tmp/egg/setup.py) egg_info for package egg
      ****************************************
      You probably installed this package on accident.
      Perhaps your pip syntax is incorrect
      ****************************************
  
  Installing collected packages: egg
    Running setup.py install for egg
      ****************************************
      You probably installed this package on accident.
      Perhaps your pip syntax is incorrect
      ****************************************
  
  Successfully installed egg
  Cleaning up...


Features
--------

* None whatsoever.
