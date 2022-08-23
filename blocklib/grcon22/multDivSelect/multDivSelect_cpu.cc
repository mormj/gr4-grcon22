/* -*- c++ -*- */
/*
 * Copyright 2022 Block Author
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */

#include "multDivSelect_cpu.h"
#include "multDivSelect_cpu_gen.h"

namespace gr {
namespace grcon22 {

template <class T>
multDivSelect_cpu<T>::multDivSelect_cpu(const typename multDivSelect<T>::block_args& args)
    : INHERITED_CONSTRUCTORS(T)
{
}

template <class T>
work_return_t multDivSelect_cpu<T>::work(work_io& wio)
{
    auto in0 = wio.inputs()[0].items<T>(); // can also do ["in0"]
    auto in1 = wio.inputs()[1].items<T>();
    auto out = wio.outputs()[0].items<T>();

    auto noutput_items = wio.outputs()[0].n_items;

    auto sel = pmtf::get_as<bool>(*this->param_select);

    for (size_t index = 0; index < noutput_items; index++) {
        if (sel) { out[index] = in0[index] * in1[index]; }
        else{ out[index] = in0[index] / in1[index]; }
    }

    wio.produce_each(noutput_items); 
    return work_return_t::OK;
}

} /* namespace grcon22 */
} /* namespace gr */
