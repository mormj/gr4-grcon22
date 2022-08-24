from gnuradio import grcon22
from gnuradio import gr

class multDivSelect_ff(grcon22.multDivSelect_ff):
    def __init__(self, *args, **kwargs):
        grcon22.multDivSelect_ff.__init__(self, *args, **kwargs, 
            impl=grcon22.multDivSelect_ff.available_impl.pyshell)
        self.set_pyblock_detail(gr.pyblock_detail(self))
    
    def work(self, wio):
        out = wio.outputs()[0]
        noutput_items = out.n_items

        inbuf1 = gr.get_input_array(self, wio, 0)
        inbuf2 = gr.get_input_array(self, wio, 1)
        outbuf1 = gr.get_output_array(self, wio, 0)

        # Get the current value of our parameter
        sel = self.get_parameter("select")
        if sel():  # the __call__ operator gets the native value of the pmt
            outbuf1[:] = inbuf1 * inbuf2
        else:
            outbuf1[:] = inbuf1 / inbuf2

        out.produce(noutput_items)
        return gr.work_return_t.OK 