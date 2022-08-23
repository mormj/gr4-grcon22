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

namespace gr {
namespace grcon22 {

template <class T>
class multDivSelect_cpu : public multDivSelect<T>
{
public:
    multDivSelect_cpu(const typename multDivSelect<T>::block_args& args);

    work_return_t work(work_io&) override;

private:
    // Declare private variables here
};


} // namespace grcon22
} // namespace gr
