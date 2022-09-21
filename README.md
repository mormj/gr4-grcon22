# gr4-grcon22

Out of Tree Module for GRCon22 GR 4.0 Workshop

## Prerequisites

### Installing GNU Radio 4.0

https://wiki.gnuradio.org/index.php?title=GNU_Radio_4.0

### Creating the OOT Module

For more info: 

https://wiki.gnuradio.org/index.php?title=Creating_OOT_Module_in_GR_4.0

```
cd $GR_PREFIX && source setup_env.sh
cd $GR_PREFIX/src
python3 $GR_PREFIX/src/gnuradio/utils/modtool/create_mod.py grcon22
```
### Creating the Block

```
cd gr4-grcon22
python3 $GR_PREFIX/src/gnuradio/utils/modtool/create_block.py --templated multDivSelect
```

## Running from Docker image
Using the image provided from https://github.com/mormj/gr4-docker

```
docker pull mormj/gr4-runtime-docker:ubuntu-22.04
xhost +
docker run -it --privileged -v ~/.Xauthority:/root/.Xauthority \
    -v /tmp/.X11-unix/:/tmp/.X11-unix:rw -e DISPLAY=$DISPLAY \
    -e QT_X11_NO_MITSHM=1 mormj/gr4-runtime-docker:ubuntu-22.04
```
Now, inside the container (we don't need to specify a prefix or libdir):
```
git clone https://github.com/mormj/gr4-grcon22
cd gr4-grcon22
meson setup build
cd build
ninja
ninja test
ninja install
ldconfig
gnuradio-companion
```

Now, the example inside the examples/ directory can be run
