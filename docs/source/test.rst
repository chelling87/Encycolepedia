TEST
====

.. exec_code::
  :filename: test_code.py
  :hide_code:

.. exec_code::

  for i in range(0, 4):
    print(f'Cole -> {i}')

Experimental
------------

This is just some stuff I'm playing around with

A Widget
--------

.. jupyter-execute::
  :linenos:

  import ipywidgets as w
  from IPython.display import display

  a = w.Dropdown(
      options=['LS', 'SS', 'R0'],
      value='LS',
      description='Number:',
      disabled=False,
  )

  display(a)

Some LaTeX
----------
.. jupyter-execute::

  from IPython.display import Latex
  Latex('\int_{-\infty}^\infty e^{-x²}dx = \sqrt{\pi}')

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   example
