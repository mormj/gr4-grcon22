from gnuradio import grcon22
from gnuradio import gr

class multDivSelect_ff():
    def __init__(self, blk, **kwargs):
        self._blk = blk
    
    def work(self, wio):
        out = wio.outputs()[0]
        noutput_items = out.n_items

        inbuf1 = gr.get_input_array(self._blk, wio, 0)
        inbuf2 = gr.get_input_array(self._blk, wio, 1)
        outbuf1 = gr.get_output_array(self._blk, wio, 0)

        # Get the current value of our parameter
        sel = self._blk.get_parameter("select")
        if sel():  # the __call__ operator gets the native value of the pmt
            outbuf1[:] = inbuf1 * inbuf2
        else:
            outbuf1[:] = inbuf1 / inbuf2

        out.produce(noutput_items)
        return gr.work_return_t.OK 