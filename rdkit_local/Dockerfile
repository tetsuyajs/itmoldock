# Image name : itmol/rdkit
# This image is for Cheminformatics with rdkit.
# Build test is excuted in 07/08/2016.

# centos:7 have already installed python 2.7.5.
FROM centos:7

# This file is created by Tetsuya Yamamoto.
MAINTAINER yamamoto@itmol.com

# Packages Install (from yum and pip)
RUN set -x \
    && yum install -y python-devel python-pillow gcc-c++ boost-devel make cmake unzip git \
    && curl -kL https://bootstrap.pypa.io/get-pip.py | python \ 
    && pip install numpy

RUN cd usr/local/ \
    && git clone -b master --single-branch https://github.com/rdkit/rdkit.git
ENV RDBASE /usr/local/rdkit
ENV LD_LIBRARY_PATH /lib:$RDBASE/lib
ENV PYTHONPATH $RDBASE

# RDKit Install (Practice)
RUN mkdir $RDBASE/build \
    && cd $RDBASE/build \
    && cmake -DRDK_BUILD_INCHI_SUPPORT=ON -DBOOST_ROOT=/usr/lib64 -D PYTHON_EXECUTABLE=/usr/bin/python .. \
    && make \
    && make install

# Usage:
# build test(image name is itmol/rdkit, log file name is build_log.txt)
#     docker build -t itmol/rdkit . > build_log.txt
# run test(container name is rdkit-container)
#     docker run -it --rm --name rdkit-container itmol/rdkit /bin/bash
