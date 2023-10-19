Test
====

This is just a playground for me to test some of the code features in Sphinx.
Most of these are some kind of python, and some of it are from Jupyter NBs!

Running Code
------------

Here is an example where I execute code from a file called ``test_code.py``.
The code itself will show, but I've supressed it with ``:hide_code:``.

.. exec_code::
  :filename: test_code.py
  :hide_code:


This is an example where I've just written some python code to be executed. It
is not hidden, but it could be if desired.

.. exec_code::

  for i in range(0, 4):
    print(f'Cole -> {i}')


A Widget
--------

These widget whatchamacallits seem pretty neat, so I want to see what I can
accomplish with this. I can hide the code here as well, but for now, I like to
see it. I've included the line numbers, but this isn't required.

.. jupyter-execute::
  :linenos:

  import ipywidgets as w
  from IPython.display import display, HTML
  from ipywidgets import HBox, Label
  
  a = w.Dropdown(
      options     = ['LS', 'SS', 'R0', 'R1', 'R2', 'R3', 'R4', 'R5'],
      value       = 'LS',
      disabled    = False
  )
  
  # Fancy work just to change this text
  display(HTML("<style>.white_label { color:white }</style>"))
  label = Label(value = "Module Type")
  label.add_class("white_label")

  HBox([label, a])

Some LaTeX
----------

We can even use the jupyter-execute for Latex!

.. jupyter-execute::

  from IPython.display import Latex
  Latex('\int_{-\infty}^\infty e^{-x²}dx = \sqrt{\pi}')

