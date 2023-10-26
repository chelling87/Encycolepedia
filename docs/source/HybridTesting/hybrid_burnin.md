# Hybrid Burn-in

These notes come from Ben Bruers, and I'm working on making them more robust,
this should do for now however.

In this example, they are building two R1H0 hybrids. Hybrids
[20USEH20000051](https://itkpd-test.unicorncollege.cz/componentView?code=4277d938247b0d7a5f06446ca8b98583)
and
[20USEH20000052](https://itkpd-test.unicorncollege.cz/componentView?code=f1705755e9eb0bab4359455acad5a6a3)
were first registered in the database, where they were registered to the
[20USET10000016](https://itkpd-test.unicorncollege.cz/componentView?code=1093ea2608d63fab82b5ff292a6dc6e7)
R1 hybrid panel.

## Setup ITSDAQ



```bash
git clone https://gitlab.cern.ch/atlas-itk-strips-daq/itsdaq-sw.git
cd itsdaq-sw
python waf configure
python waf build
python waf install
```

### Create var folder

```bash
mkdir -p var/ps
mkdir -p var/data
mkdir -p var/results
mkdir -p var/config
```

### Create `setup.sh`

The content in our case is:

```bash
source /home/atlas/root/bin/thisroot.sh
export ROOTSYS=/home/atlas/root
export SCTDAQ_ROOT=/home/atlas/burnIn/itsdaq-sw/
export SCTDAQ_VAR=/home/atlas/burnIn/itsdaq-sw/var/
export ITSDAQ_LOCATION="DESY-Z_HU"
export SCTDB_USER="dzhu"
```


## InfluxDB Environmental Variables

```
export INFLUX_URL=localhost:8086/api/v2  # The server URL (defaults to localhost:8086)
export INFLUX_ORGANISATION=ITSDAQ  # Organisation in which to find the bucket (defaults to none)
export INFLUX_BUCKET=ITSDAQ  # Bucket/database in which to store data (defaults to ITSDAQ)
export INFLUX_TOKEN=never-you-mind-;)
```

### Copy/edit templates for AutoConfig

```bash
cp config/* var/config # have templates
``` 

Remove `power_supplies.json`:

```bash
mv var/config/power_supplies.json var/config/.power_supplies.json
```

Because we have crossed HCC bonds, we do following:

```bash
cd var/config
cp default_R1H0.det default_R1H0_xHCC.det
```

Then edit `default_R1H0_xHCC.det` and replace `0x02900000 0xaaaaaaa0 0x00000aaa
0x00ff3b05` by `0x02940023 0x88888888 0x00000888 0x00ff3b05`.

In our case the `st_system_config.dat` looks like this:

```
DAQ udp 192.168.222.16 60000,60001
DAQ udp 192.168.222.16 60002,60002

   DETECTOR COM  DAQ   Module
       id CCR  str   Filename    Type
Module  0 102  0x20  JaneDoe_2_0 R1H0_xHCC
Module  2 102  0x24  JaneDoe_2_2 R1H0_xHCC
```

## Run ITSDAQ

```bash
source setup.sh
./RUNITSDAQ.sh
```

This also runs `AutoConfig` and all chips should be found.

## Run `AutoConfig`

Note the extra changes we did above to run `AutoConfig` without issues.
To download the best configs according to chip testing and what is stored
in the database, we execute in the ITSDAQ terminal:

```bash
AutoConfig(false, false, false)
```

This queries for our prod. DB credentials.

## Auto assemble hybrids

The two R1H0s are registered in the database, but have no chips associated.
To change that, we first ask ITSDAQ to output the chips we have on the
hybrid in a nice concise way:


```bash
FuseData fuse_data;
readABCFuseIDs(fuse_data);
readHCCFuseIDs(fuse_data);
database_build_assembly(fuse_data);
```

This returns:

```
Saving assembly information to assembly_script_panel_2.json.
```

Hence the output information is now in `assembly_script_panel_2.json`.
It indeed contains a list of HCC and ABC "alternative identifiers".

## Upload auto-assemble

### Check-out the production-database-scripts

```bash
git clone https://gitlab.cern.ch/atlas-itk/sw/db/production_database_scripts.git
cd production_database_scripts
```

### Apply manual corrections

Removed entries with `ABC000000` in the json file `assembly_script_panel_2.json` and changed order from 0 to 9 instead of 1 to 10.

Currently addressing these bugs in ITSDAQ, so this really is intermediate for now.

### Run `assemble_component`

```bash
python3 assemble_component.py --json ../itsdaq-sw/assembly_script_panel_2.json --reference 20USET10000016
```

where:

- `--json` gives the path to the JSON file just created
- `--reference` gives the database SN of the hybrid panel to which the hybrids are associated
