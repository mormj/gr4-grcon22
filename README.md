# gr4-grcon22

Out of Tree Module for GRCon22 GR 4.0 Workshop

## Installing GNU Radio 4.0

https://wiki.gnuradio.org/index.php?title=GNU_Radio_4.0#Creating_a_Prefix

## Creating the OOT Module

For more info: 

https://wiki.gnuradio.org/index.php?title=Creating_OOT_Module_in_GR_4.0

```
cd $GR_PREFIX && source setup_env.sh
cd $GR_PREFIX/src
python3 $GR_PREFIX/src/gnuradio/utils/modtool/create_mod.py grcon22
```
## Creating the Block

```
cd gr4-grcon22
python3 $GR_PREFIX/src/gnuradio/utils/modtool/create_block.py --templated multDivSelect
```