Usage
=====

.. _installation:

Installation
------------

To use test_script, first install it using pip:

.. code-block:: console

   (.venv) $ pip install test_script

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``test_script.get_random_ingredients()`` function:

.. autofunction:: test_script.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`test_script.get_random_ingredients`
will raise an exception.

.. autoexception:: test_script.InvalidKindError

For example:

>>> import test_script
>>> test_script.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']
