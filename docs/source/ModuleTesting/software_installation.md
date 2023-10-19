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
```
```shell
git clone https://gitlab.cern.ch/atlas-itk/sw/db/production_database_scripts.git
```

We don't need to worry about the production database scripts at the moment, as
they are python based and nothing special needs to be done. For ITSDAQ, we will
need to perform a few extra steps.

## Configure and Install ITSDAQ

The first thing you must do after downloading the repository is to configure. Enter
into the ITSDAQ repository with `cd itsdaq-sw` and configure.

```shell
python waf configure
```

```{eval-rst}
.. tip::

  Run with ``--enable-visa`` if you need to use VISA, but it must be installed first.
```

Once you have configured, you can perform the build:

```shell
python waf build
```

And finally, install:

```shell
python waf install
```

If you need to update the repository:

```shell
git pull
```

```{eval-rst}
.. important::

  If you perform a git pull, you need to re-build!
```
