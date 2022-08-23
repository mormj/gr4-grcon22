grcon22_sources += []
grcon22_deps += [gnuradio_gr_dep, volk_dep, fmt_dep, pmtf_dep, python3_embed_dep, json_dep]

block_cpp_args = ['-DHAVE_CPU']

# if cuda_dep.found() and get_option('enable_cuda')
#     block_cpp_args += '-DHAVE_CUDA'

#     gnuradio_blocklib_grcon22_cu = library('gnuradio-blocklib-grcon22-cu', 
#         grcon22_cu_sources, 
#         include_directories : incdir, 
#         install : true, 
#         dependencies : [cuda_dep])

#     gnuradio_blocklib_grcon22_cu_dep = declare_dependency(include_directories : incdir,
#                         link_with : gnuradio_blocklib_grcon22_cu,
#                         dependencies : cuda_dep)

#     grcon22_deps += [gnuradio_blocklib_grcon22_cu_dep, cuda_dep]

# endif

incdir = include_directories(['../include/gnuradio/grcon22','../include'])
gnuradio_blocklib_grcon22_lib = library('gnuradio-blocklib-grcon22', 
    grcon22_sources, 
    include_directories : incdir, 
    install : true,
    link_language: 'cpp',
    dependencies : grcon22_deps,
    link_args : ['-lgnuradio-runtime'],
    cpp_args : block_cpp_args)

gnuradio_blocklib_grcon22_dep = declare_dependency(include_directories : incdir,
					   link_with : gnuradio_blocklib_grcon22_lib,
                       dependencies : grcon22_deps)
