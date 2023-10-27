# Hardware Setup

**Here we will discuss what needs to be connected to what. I think the only
hardware that we need to discuss are the FMC-DP and FMC-IB with the Nexys
right? I'll look into that.**

**See what you can steal from the
[Twiki](https://twiki.cern.ch/twiki/bin/view/Atlas/ABCStarHybridModuleTestsV2)**

## Hardware

For testing modules, we will assume you are using the Digilent 410-316 Nexys
Video FPGA, or
[Nexys](https://www.digikey.ca/en/products/detail/digilent-inc/410-316/5456481)
for short. This will be connected to your testing PC via Ethernet. To install
the firmware on the Nexys, you'll need to have a USB cable connecting the PC to
the micro-USB port labelled `prog` on the Nexys board. You can use an SD card
for this, but it will not be covered here.

For the FPGA's Mezzanine Card
([FMC](https://twiki.cern.ch/twiki/bin/viewauth/Atlas/ITSFMCs)), it will be
assumed you are using either the FMC-IB (with SLVS and module-adapter boards)
or the FMC-0514-DP (FMC-DP). This will be installed on the Nexys' FMC Header.
For this tutorial, the FMC-DP will be used.

```{eval-rst}
.. note::
    
  The FMC-IB is not the preferred device, but it is acceptable. Some of the 
  calibrations shown in the tutorial will not apply. Configurations will be
  treated identically as if you were using the FMC-DP on M0.
``` 

The module will be connected with a pair of mini DisplayPort cables. Always pay
close attention to which port on the FMC is connected to on the module testing
frame. Failure to connect them properly and it's game over (Don't you dare
bring up the R3).

Lastly, you will need a test box. Either your single-module testing station or
your coldbox is acceptable. This choice may necessitate a change in the default
`Ophase` value, which will be discussed further on. _link when exists_


```{eval-rst}

.. tabs::

  .. tab:: Single Module Test FMC-IB

    .. image:: Images/single_module_test_setup.png
      :height: 500


  .. tab:: Muti-Module Test FMC-DP

    .. image:: Images/multi_module_test_setup.png
      :height: 500

```

These are merely examples of what your respective test setups may look like. 


## Tips

```{eval-rst}
.. tip::
  
  If you are experiencing unexplanable problems talking to the ASICs, consider giving
  the cables a light jiggle. It can help.
``` 
