Usage
=====

.. _installation:

Installation
------------

To use test_script, first install it using pip:

.. code-block:: console

   (.venv) $ pip install test_script

Creating modules
----------------

To retrieve a list of random modules,
you can use the ``test_script.get_random_modules()`` function:

.. autofunction:: test_script.get_random_modules

The ``kind`` parameter should be a module type (i.e. ``"R0"`` or ``"SS"``).

.. autoexception:: test_script.InvalidKindError

For example:

>>> import test_script
>>> test_script.get_random_modules()
['R0', 'SS', 'R3']
