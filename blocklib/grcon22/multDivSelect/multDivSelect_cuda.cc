/* -*- c++ -*- */
/*
 * Copyright 2022 Block Author
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */

#include "multDivSelect_cuda.h"
#include "multDivSelect_cuda_gen.h"

namespace gr {
namespace grcon22 {

template <class T>
multDivSelect_cuda<T>::multDivSelect_cuda(
    const typename multDivSelect<T>::block_args& args)
    : INHERITED_CONSTRUCTORS(T)
{
    p_multkernel = std::make_unique<cusp::multiply<T>>(2);
    p_divkernel = std::make_unique<cusp::divide<T>>(2);

    cudaStreamCreate(&d_stream);
    p_multkernel->set_stream(d_stream);
    p_divkernel->set_stream(d_stream);
}

template <class T>
work_return_t multDivSelect_cuda<T>::work(work_io& wio)
{
    auto in0 = wio.inputs()[0].items<T>(); // can also do ["in0"]
    auto in1 = wio.inputs()[1].items<T>();
    auto out = wio.outputs()[0].items<T>();

    auto noutput_items = wio.outputs()[0].n_items;

    auto sel = pmtf::get_as<bool>(*this->param_select);


    if (sel) {
        p_multkernel->launch_default_occupancy(
            {
                { in0, in1 },
            },
            { out },
            noutput_items);
    } else {
        p_divkernel->launch_default_occupancy(
            {
                { in0, in1 },
            },
            { out },
            noutput_items);
    }

    cudaStreamSynchronize(d_stream);

    wio.produce_each(noutput_items);
    return work_return_t::OK;
}

} /* namespace grcon22 */
} /* namespace gr */
