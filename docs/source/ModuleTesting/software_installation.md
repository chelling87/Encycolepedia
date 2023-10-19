# Installation

We will rely on two software repositories for what follows:

We want a few things to all live in the same place. So, for this tutorial, we will create
a directory called `module_testing`, which will be used for all of the material that follows
(might want to movethis to some home page if possible).


So, first, create your directory and get in there.

```shell
mkdir module_testing && cd module_testing
```

We will need two different repositories:
[itsdaq-sw](https://gitlab.cern.ch/atlas-itk-strips-daq/itsdaq-sw) (ITSDAQ!)
and the
[production database scripts](https://gitlab.cern.ch/atlas-itk/sw/db/production_database_scripts).
These two directories will need to be siblings, meaning they are both at the
same level within whatever directory they are in (in this case,
`module_testing`). Clone the two repositories linked above (using https in this example):

```shell
git clone https://gitlab.cern.ch/atlas-itk-strips-daq/itsdaq-sw.git
git clone https://gitlab.cern.ch/atlas-itk/sw/db/production_database_scripts.git
```

We don't need to worry about the production database scripts at the moment, as
they are python based and nothing special needs to be done. For ITSDAQ, we will
need to perform a few extra steps.

## Configure and Install ITSDAQ

The first thing you must do after downloading the repository is to ...

```shell
python waf configure
```
Which will produce something that looks like this (results may vary):

```
Setting top to                           : /home/daq2/module_testing/itsdaq-sw 
Setting out to                           : /home/daq2/module_testing/itsdaq-sw/build 
Checking for 'g++' (C++ compiler)        : /usr/bin/g++ 
Found compiler                           : gcc 4_8_5 
Use architecture                         : native 
Found OS                                 : linux 
Found CPU                                : x86_64 
Found git repository                     : ok 
Checking for program 'git'               : /usr/bin/git 
Checking for program 'root'              : /usr/bin/root 
Using system root                        : /usr 
Checking for program 'root'              : /usr/bin/root 
Checking ROOTSYS                         : /usr 
Read root-config                         : yes 
Checking ROOT                            : yes 
Checking for root-guibuilder             : yes 
Checking ROOT version                    : 6.24/08 
Checking for header json.hpp             : yes 
Checking for header thread               : yes 
Checking for program 'python'            : /usr/bin/python 
Checking for python version              : 2.7.5 
python-config                            : /usr/bin/python-config 
Asking python-config for pyembed '--cflags --libs --ldflags' flags : yes 
Testing pyembed configuration                                      : yes 
Asking python-config for pyext '--cflags --libs --ldflags' flags   : yes 
Testing pyext configuration                                        : yes 
Look for stdint.h (with Python path)     : Use python config for stdint.h 
Using system boost                       : /usr 
Checking BOOST version                   : 1_53 
Checking for BOOST system                : boost_system-mt 
Checking for BOOST program options       : boost_program_options-mt boost_system-mt 
Checking for BOOST unit test             : boost_unit_test_framework-mt boost_system-mt 
Checking for header lmcurve_tyd.h        : not found 
Checking for program 'pkg-config'        : /usr/bin/pkg-config 
Checking for 'libusb-1.0'                : yes 
Checking for header nivxi.h              : not found 
Checking for header pcap.h               : yes 

Configuration successful: Reviewing configuration

Using HSIO                               : yes 
Using VISA                               : no 
Building DLLS                            : stdll, KwikFit, dcsdll, tdummy, khvdll, ttidll, tilockdll, tti_dcload, iseghvdll, tvgendll, tsemiprobe, tnucleus, tvelox, tweiss, tarcus 
Dirs to link in stdll                    : stlib, worker, hsio_lib 
Building python extension (optional)     : yes 
Build tests                              : no 
Build (some) macros                      : no 
'configure' finished successfully (5.024s)
```
