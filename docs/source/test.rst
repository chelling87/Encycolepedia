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

Some LaTeX
----------

We can even use the jupyter-execute for Latex!

.. jupyter-execute::

  from IPython.display import Latex
  Latex('\int_{-\infty}^\infty e^{-x²}dx = \sqrt{\pi}')


A Widget
--------

These widget whatchamacallits seem pretty neat, so I want to see what I can
accomplish with this. I can hide the code here as well, but for now, I like to
see it. I've included the line numbers, but this isn't required.

.. jupyter-execute::
  
  import ipywidgets as widgets
  from IPython.display import display

  w = widgets.Textarea(
    value = "my value",
    placeholder = "placeholder",
    description = "Type",
    disabled = False
  )  

  display(w)

.. jupyter-execute::

  import ipywidgets as widgets
  from IPython.display import display, HTML

  a = widgets.IntSlider(description='a')
  b = widgets.IntSlider(description='b')
  c = widgets.IntSlider(description='c')
  def f(a, b, c):
      print('{}*{}*{}={}'.format(a, b, c, a*b*c))

  out = widgets.interactive_output(f, {'a': a, 'b': b, 'c': c})
  
  widgets.HBox([widgets.VBox([a, b, c]), out])

Unfortunately, the interactive output isn't ... well, interactive at all.
   
.. jupyter-execute::

  import ipywidgets as widgets
  from IPython.display import display, HTML
  
  module_dropdown = widgets.Dropdown(
      options     = ['LS', 'SS', 'R0', 'R1', 'R2', 'R3', 'R4', 'R5'],
      value       = 'LS',
      disabled    = False
  )
  
  FMC_dropdown = widgets.Dropdown(
      options     = [0, 1, 2, 3, 4, 5],
      value       = 0,
      disabled    = False
  )
  
  xHCC_checkbox = widgets.Checkbox(
      value       = True,
      description = "Crossed HCC Bonds?",
      disabled    = False,
      indent      = False
  )
  
  # Fancy work just to change this text
  display(HTML('<style>.white_label { color:white }</style>'))
  
  moduletype_label = widgets.Label(value = 'Module Type')
  moduletype_label.add_class("white_label")
  
  
  FMCchannel_label = widgets.Label(value = 'FMC Channel')
  FMCchannel_label.add_class('white_label')

  dummy_label = widgets.Label(value = "Unfortunately, this won't update properly")
  dummy_label.add_class('white_label')

  # Create button
  button = widgets.Button(description = 'Update!')
  # To store st_lines
  output = widgets.Output(value = 'Waiting', layout = {'border': '1px solid black'})
  
  # Some functions
  def return_streams(channel):
      ''' return array of streams for given FMC channel '''
      all_streams = [[0, 2, 4, 6],
                     [8, 10, 12, 14],
                     [16, 18, 20, 22],
                     [24, 26, 28, 30],
                     [32, 34, 36, 38],
                     [40, 42, 44, 46]]
  
      return all_streams[channel]
  
  def create_st_lines(module_type, channel):
  
      streams = return_streams(channel)
      lines = []
      print(f'module_type: {module_type}')
      print(f'FMC channel: {channel}')
      if (module_type == 'LS'):
          lines.append(f'Module 0  0   {streams[0]} JaneDoe0 Barrel')
      elif (module_type == 'SS'):
          lines.append(f'Module 0  0   {streams[1]} JaneDoe0 Barrel')
          lines.append(f'Module 1  0   {streams[0]} JaneDoe1 Barrel')
      elif (module_type == 'R0' or module_type == 'R1'):
          lines.append(f'Module 0  0   {streams[1]} JaneDoe0 {module_type}H0')
          lines.append(f'Module 1  0   {streams[0]} JaneDoe1 {module_type}H1')
      elif (module_type == 'R2' or module_type == 'R4' or module_type == 'R5'):
          lines.append(f'Module 0  0   {streams[0]} JaneDoe0 {module_type}H0')
          lines.append(f'Module 1  0   {streams[1]} JaneDoe1 {module_type}H1')
      elif (module_type == 'R3'):
          lines.append(f'Module 0  0   {streams[0]} JaneDoe0 {module_type}H0')
          lines.append(f'Module 1  0   {streams[1]} JaneDoe1 {module_type}H1')
          lines.append(f'Module 2  0   {streams[2]} JaneDoe0 {module_type}H2')
          lines.append(f'Module 3  0   {streams[3]} JaneDoe1 {module_type}H3')
      else:
          lines.append('Working on it, give me a break.')
  
      return lines
  
  def update(b):
      ''' Update the output based on module type and FMC channel '''
      output.clear_output()
      module_type = module_dropdown.value
      FMC_channel = FMC_dropdown.value
      st_lines    = create_st_lines(module_type, FMC_channel)
      with output:
          for line in st_lines:
              dummy_label.value = line
              if (xHCC_checkbox.value):
                  line = f'{line}_xHCC'
              print(line)
  
  # Structure of output boxes
  vb = widgets.VBox([widgets.HBox([moduletype_label, module_dropdown]),
                     widgets.HBox([FMCchannel_label, FMC_dropdown]),
                     xHCC_checkbox,
                     button,
                     dummy_label,
                     output])
  
   
  button.on_click(update)
  display(vb)


