#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: josh
# GNU Radio version: 4.0.0.0-preview0

from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
#from gnuradio.filter import firdes
#from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
#from gnuradio.eng_arg import eng_float, intx
#from gnuradio import eng_notation
from gnuradio import grcon22
from gnuradio import streamops
from matplotlib import pyplot as plt



def snipfcn_snippet_0(fg, rt=None):
    plt.plot(fg.snk.data())
    plt.show()


def snippets_main_after_stop(fg, rt=None):
    snipfcn_snippet_0(fg, rt)


class multDivSub_example(gr.flowgraph):

    def __init__(self):
        gr.flowgraph.__init__(self, "Not titled yet")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.streamops_head_0 = streamops.head( 1000,0, impl=streamops.head.cpu)
        self.snk = blocks.vector_sink_f( 1,1024, impl=blocks.vector_sink_f.cpu)
        self.grcon22_multDivSelect_0 = grcon22.multDivSelect_ff( True, impl=grcon22.multDivSelect_ff.cuda)
        self.analog_sig_source_0_0 = analog.sig_source_f( samp_rate,analog.waveform_t.CONSTANT,1000,17.0,0,0, impl=analog.sig_source_f.cpu)
        self.analog_sig_source_0 = analog.sig_source_f( samp_rate,analog.waveform_t.SIN,1000,1.0,0,0, impl=analog.sig_source_f.cpu)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.streamops_head_0, 0), (self.snk, 0))
        self.connect((self.analog_sig_source_0, 0), (self.grcon22_multDivSelect_0, 0)).set_custom_buffer(gr.buffer_cuda_properties.make(gr.buffer_cuda_type.H2D))
        self.connect((self.analog_sig_source_0_0, 0), (self.grcon22_multDivSelect_0, 1)).set_custom_buffer(gr.buffer_cuda_properties.make(gr.buffer_cuda_type.H2D))
        self.connect((self.grcon22_multDivSelect_0, 0), (self.streamops_head_0, 0)).set_custom_buffer(gr.buffer_cuda_properties.make(gr.buffer_cuda_type.D2H))


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate




def main(flowgraph_cls=multDivSub_example, options=None):
    fg = flowgraph_cls()
    rt = gr.runtime()


    rt.initialize(fg)

    rt.start()

    try:
        rt.wait()
    except KeyboardInterrupt:
        rt.stop()
        rt.wait()
    snippets_main_after_stop(fg, rt)

if __name__ == '__main__':
    main()
