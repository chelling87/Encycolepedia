==========
Line Maker
==========

.. code:: ipython3

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
    display(HTML('<style>.red_label { color:red }</style>'))
    
    moduletype_label = widgets.Label(value = 'Module Type')
    moduletype_label.add_class("red_label")
    
    FMCchannel_label = widgets.Label(value = 'FMC Channel')
    FMCchannel_label.add_class('red_label')
    
    # Create button
    button = widgets.Button(description = 'Update!')
    # To store st_lines
    output = widgets.Output(value = 'Waiting')
    
    # Structure of output boxes
    vb = widgets.VBox([widgets.HBox([moduletype_label, module_dropdown]),
                       widgets.HBox([FMCchannel_label, FMC_dropdown]),
                       xHCC_checkbox,
                       button, 
                       output])
    
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
            lines.append(f'Module 0  0   {streams[2]} JaneDoe0 {module_type}H2')
            lines.append(f'Module 1  0   {streams[3]} JaneDoe1 {module_type}H3')
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
                if (xHCC_checkbox.value):
                    line = f'{line}_xHCC'
                print(line)
        
    
    button.on_click(update)
    
    display(vb)
    
    
    
    
    
    
    




.. raw:: html

    <style>.red_label { color:red }</style>



.. parsed-literal::

    VBox(children=(HBox(children=(Label(value='Module Type', _dom_classes=('red_label',)), Dropdown(options=('LS',…


