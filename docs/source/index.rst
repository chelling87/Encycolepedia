Welcome to the Encycolepedia!
====================================

Hi, I'm Cole Helling. Here, I elucidate the various topics for the ITk
Strips to the best of my abilities.

In the tutorials, I try to always point to the official documentation whenever
possible. I may copy the instructions from those documents here to avoid having
the user flip back and forth, however, please consult the links in the event of
an issue. It's possible that something has changed.
   
.. note::

  This project is under active development. None of this is to be considered
  official, and I wouldn't hold my breath on it all being correct. I make
  mistakes in my understandings and my explanations. I've also included 4
  errors on purpose, but I will not tell you which. If you find something
  wrong, please let me know. Better yet, make a merge request.


.. exec_code::
  :filename: test_code.py
  :hide_code:

.. exec_code::

  for i in range(0, 4):
    print(f'Cole -> {i}')

Contents
--------

.. toctree::

  test
  thing1/thing2

Code
----

.. toctree::

  generated/test_script
  usage
  api


Experimental
------------

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

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   example
