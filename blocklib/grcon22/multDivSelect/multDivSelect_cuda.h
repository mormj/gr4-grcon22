/* -*- c++ -*- */
/*
 * Copyright 2022 Block Author
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */

#pragma once

#include <gnuradio/grcon22/multDivSelect.h>


#include <cusp/multiply.cuh>
#include <cusp/divide.cuh>

namespace gr {
namespace grcon22 {

template <class T>
class multDivSelect_cuda : public multDivSelect<T>
{
public:
    multDivSelect_cuda(const typename multDivSelect<T>::block_args& args);

    work_return_t work(work_io&) override;

private:
    cudaStream_t d_stream;
    std::unique_ptr<cusp::multiply<T>> p_multkernel;
    std::unique_ptr<cusp::divide<T>> p_divkernel;
};


} // namespace grcon22
} // namespace gr
