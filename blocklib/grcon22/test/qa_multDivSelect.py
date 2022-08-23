#!/usr/bin/env python3

from gnuradio import gr_unittest, gr, blocks, grcon22

class test_multdivsel(gr_unittest.TestCase):

    def setUp(self):
        self.fg = gr.flowgraph()

    def tearDown(self):
        self.fg = None

    def test_mult_f(self):
        nsamples = 10000

        indata_1 = list(range(100)) * (nsamples // 100)
        indata_2 = list(range(100)) * (nsamples // 100)

        expected_output = [z[0] * z[1] for z in zip(indata_1, indata_2)]

        src1 = blocks.vector_source_f(indata_1, False)
        src2 = blocks.vector_source_f(indata_2, False)

        blk = grcon22.multDivSelect_ff(True)
        snk = blocks.vector_sink_f()
        

        self.fg.connect(src1, 0, blk, 0)
        self.fg.connect(src2, 0, blk, 1)
        self.fg.connect(blk, 0, snk, 0)

        self.fg.start()
        self.fg.wait()
        
        self.assertSequenceEqual(expected_output, snk.data())

    def test_div_f(self):
        nsamples = 10000

        indata_1 = list(range(100)) * (nsamples // 100)
        indata_2 = list(range(1,101)) * (nsamples // 100)

        expected_output = [z[0] / z[1] for z in zip(indata_1, indata_2)]

        src1 = blocks.vector_source_f(indata_1, False)
        src2 = blocks.vector_source_f(indata_2, False)

        # Set it to true as if we are going to multiply
        blk = grcon22.multDivSelect_ff(True)
        # Use the setter to update the value
        blk.set_select(False)
        self.assertEqual(False, blk.select())
        snk = blocks.vector_sink_f()
        

        self.fg.connect(src1, 0, blk, 0)
        self.fg.connect(src2, 0, blk, 1)
        self.fg.connect(blk, 0, snk, 0)

        self.fg.start()
        self.fg.wait()
        
        self.assertFloatTuplesAlmostEqual(expected_output, snk.data(), places=7)


    def test_mult_c(self):
        nsamples = 10000

        indata_1 = [complex(x,-(x+1)) for x in range(100)] * (nsamples // 100)
        indata_2 = [complex(x,-(x+2)) for x in range(100)] * (nsamples // 100)

        expected_output = [z[0] * z[1] for z in zip(indata_1, indata_2)]

        src1 = blocks.vector_source_c(indata_1, False)
        src2 = blocks.vector_source_c(indata_2, False)

        blk = grcon22.multDivSelect_cc(True)
        snk = blocks.vector_sink_c()
        

        self.fg.connect(src1, 0, blk, 0)
        self.fg.connect(src2, 0, blk, 1)
        self.fg.connect(blk, 0, snk, 0)

        self.fg.start()
        self.fg.wait()
        
        self.assertSequenceEqual(expected_output, snk.data())

    def test_div_c(self):
        nsamples = 10000

        indata_1 = [complex(x,-(x+1)) for x in range(100)] * (nsamples // 100)
        indata_2 = [complex(x,-(x+2)) for x in range(100)] * (nsamples // 100)

        expected_output = [z[0] * z[1] for z in zip(indata_1, indata_2)]

        src1 = blocks.vector_source_c(indata_1, False)
        src2 = blocks.vector_source_c(indata_2, False)

        blk = grcon22.multDivSelect_cc(True)
        snk = blocks.vector_sink_c()
        

        self.fg.connect(src1, 0, blk, 0)
        self.fg.connect(src2, 0, blk, 1)
        self.fg.connect(blk, 0, snk, 0)

        self.fg.start()
        self.fg.wait()
        
        self.assertComplexTuplesAlmostEqual(expected_output, snk.data(), places=7)

if __name__ == "__main__":
    gr_unittest.run(test_multdivsel)