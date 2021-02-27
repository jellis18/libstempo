import platform

import numpy
from Cython.Build import cythonize
from setuptools import Extension, setup

TEMPO2 = "/usr/local"

# need rpath links to shared libraries on Linux
if platform.system() == "Linux":
    linkArgs = ["-Wl,-R{}/lib".format(TEMPO2)]
else:
    linkArgs = []

setup(
    name="libstempo",
    version="2.3.5",  # remember to change it in __init__.py.in
    description="A Python wrapper for tempo2",
    author="Michele Vallisneri",
    author_email="vallis@vallis.org",
    url="https://github.com/vallis/libstempo",
    packages=["libstempo"],
    package_dir={"libstempo": "libstempo"},
    package_data={"libstempo": ["data/*", "ecc_vs_nharm.txt"]},
    py_modules=[
        "libstempo.like",
        "libstempo.multinest",
        "libstempo.emcee",
        "libstempo.plot",
        "libstempo.toasim",
        "libstempo.spharmORFbasis",
        "libstempo.eccUtils",
    ],
    install_requires=["Cython>=0.22", "numpy>=1.15.0", "scipy>=1.2.0", "matplotlib>=3.3.2", "ephem>=3.7.7.1"],
    extras_require={"astropy": ["astropy>=4.2"]},
    ext_modules=cythonize(
        Extension(
            "libstempo.libstempo",
            ["libstempo/libstempo.pyx"],
            language="c++",
            include_dirs=[TEMPO2 + "/include", numpy.get_include()],
            libraries=["tempo2", "tempo2pred"],
            library_dirs=[TEMPO2 + "/lib"],
            extra_compile_args=["-Wno-unused-function"],
            extra_link_args=linkArgs,
        )
    ),
)
