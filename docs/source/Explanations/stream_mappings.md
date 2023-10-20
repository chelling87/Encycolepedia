# Stream Mappings

At times it seems that the stream mappings are all over the place. There are
certainly differences between the three big setup types: hybrid burn-in, modules, 
and petals/staves. Here I will explain that while they may seem arbitrary, there
is, if not a logic, a **reason** why the streams need to be what they are.

## Hybrid Burn-In

For the Hybrid Burn-in testing, our stream mappings are tied to how the panels are wired.

**Some stuff here**

## Modules

For Module testing, our stream mappings are tied to how the frames are wired.
To understand the stream mapping, it's best to look at the frame design to see
where the communication lines run. The drawings below are from
[EDMS](https://edms.cern.ch/ui/#!master/navigator/project?P:1108698003:100145447:subDocs). 
Click on the tab above the images to see the test frame for a particular 
module type.

```{eval-rst}
.. note::

  The Barrel frame is the same for both the LS and SS module types.

```

```{eval-rst}

.. tabs::

  .. tab:: R0

    .. image:: FramePics/R0_testframe.png
      :height: 600
  .. tab:: R1

    .. image:: FramePics/R1_testframe.png
      :height: 600

  .. tab:: R2

    .. image:: FramePics/R2_testframe.png
      :height: 600
   
  .. tab:: R3

    .. image:: FramePics/R3_testframe.png
      :height: 600
  
  .. tab:: R4

    .. image:: FramePics/R4_testframe.png
      :height: 600

  .. tab:: R5

    .. image:: FramePics/R5_testframe.png
      :height: 600
  
  .. tab:: Barrel
    
    .. image:: FramePics/Barrel_testframe.png
      :height: 600

```

*The images will likely be updated with some highlighted portions, and perhaps
I will include zoomed-in and annotated portions below the full image to make
things clear.  Then I will explain here about which stream connects to which
data line and that's how we ended up with some reversals in numbers. It's not
about what makes sense from a programming point of view, it's about where the
physical lines go such that they have as few crossings as possible (usually)
within the constraints of where things need to end up.*

```{eval-rst}

.. note::
  This might be a good place to make a table.

```

## Petals/Staves

For Petal/Stave testing, our stream mappings are tied to how the **whatdoyoucallit?** are wired.

*I don't yet have all of the information for this, but I'm looking into it.*

```{eval-rst}

.. warning::

  My knowledge here is severely limited. 

```
