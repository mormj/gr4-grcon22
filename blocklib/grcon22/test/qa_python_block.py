#!/usr/bin/env python3

from gnuradio import gr_unittest, gr, blocks, grcon22
from gnuradio.grcon22.numpy import multDivSelect_ff
class multDivSelect_ff_scratch(gr.sync_block):
    def __init__(self, select):
        gr.sync_block.__init__(
            self,
            name="multDivSelect")

        self._select = select

        self.add_port_f("in1", gr.INPUT)
        self.add_port_f("in2", gr.INPUT)
        self.add_port_f("out", gr.OUTPUT)

    def work(self, wio):
        noutput_items = wio.outputs()[0].n_items
        
        inbuf1 = self.get_input_array(wio, 0)
        inbuf2 = self.get_input_array(wio, 1)
        outbuf1 = self.get_output_array(wio, 0)

        if self._select:
            outbuf1[:] = inbuf1 * inbuf2
        else:
            outbuf1[:] = inbuf1 / inbuf2

        wio.produce_each(noutput_items)
        return gr.work_return_t.OK

    # Not thread safe??
    def set_select(self, select):
        self._select = select

    def select(self):
        return self._select

class test_multdivsel(gr_unittest.TestCase):

    def setUp(self):
        self.fg = gr.flowgraph()

    def tearDown(self):
        self.fg = None

    def test_mult_f_python(self):
        nsamples = 10000

        indata_1 = list(range(100)) * (nsamples // 100)
        indata_2 = list(range(100)) * (nsamples // 100)

        expected_output = [z[0] * z[1] for z in zip(indata_1, indata_2)]

        src1 = blocks.vector_source_f(indata_1, False)
        src2 = blocks.vector_source_f(indata_2, False)

        blk = multDivSelect_ff_scratch(True)
        snk = blocks.vector_sink_f()
        

        self.fg.connect(src1, 0, blk, 0)
        self.fg.connect(src2, 0, blk, 1)
        self.fg.connect(blk, 0, snk, 0)

        self.fg.start()
        self.fg.wait()
        
        self.assertSequenceEqual(expected_output, snk.data())

    def test_div_f_python(self):
        nsamples = 10000

        indata_1 = list(range(100)) * (nsamples // 100)
        indata_2 = list(range(1,101)) * (nsamples // 100)

        expected_output = [z[0] / z[1] for z in zip(indata_1, indata_2)]

        src1 = blocks.vector_source_f(indata_1, False)
        src2 = blocks.vector_source_f(indata_2, False)

        blk = multDivSelect_ff_scratch(True)
        blk.set_select(False)        
        snk = blocks.vector_sink_f()
        

        self.fg.connect(src1, 0, blk, 0)
        self.fg.connect(src2, 0, blk, 1)
        self.fg.connect(blk, 0, snk, 0)

        self.fg.start()
        self.fg.wait()
        
        self.assertFloatTuplesAlmostEqual(expected_output, snk.data(), places=7)


    def test_mult_f_python_extend(self):
        nsamples = 10000

        indata_1 = list(range(100)) * (nsamples // 100)
        indata_2 = list(range(100)) * (nsamples // 100)

        expected_output = [z[0] * z[1] for z in zip(indata_1, indata_2)]

        src1 = blocks.vector_source_f(indata_1, False)
        src2 = blocks.vector_source_f(indata_2, False)

        blk = multDivSelect_ff(True)
        snk = blocks.vector_sink_f()
        

        self.fg.connect(src1, 0, blk, 0)
        self.fg.connect(src2, 0, blk, 1)
        self.fg.connect(blk, 0, snk, 0)

        self.fg.start()
        self.fg.wait()
        
        self.assertSequenceEqual(expected_output, snk.data())

    def test_div_f_python_extend(self):
        nsamples = 10000

        indata_1 = list(range(100)) * (nsamples // 100)
        indata_2 = list(range(1,101)) * (nsamples // 100)

        expected_output = [z[0] / z[1] for z in zip(indata_1, indata_2)]

        src1 = blocks.vector_source_f(indata_1, False)
        src2 = blocks.vector_source_f(indata_2, False)

        blk = multDivSelect_ff(True)
        blk.set_select(False)        
        snk = blocks.vector_sink_f()
        

        self.fg.connect(src1, 0, blk, 0)
        self.fg.connect(src2, 0, blk, 1)
        self.fg.connect(blk, 0, snk, 0)

        self.fg.start()
        self.fg.wait()
        
        self.assertFloatTuplesAlmostEqual(expected_output, snk.data(), places=7)

if __name__ == "__main__":
    gr_unittest.run(test_multdivsel)