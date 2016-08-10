# Image name : itmol/rdkit:2016a
# This image is for Cheminformatics with rdkit.
# Build test is excuted in 07/08/2016.
# This is alpha version(shows 2016"a"), some software are installed through internet.

# Requirement: 
# You must copy following some files to "add" folder(same level as Dockerfile).
# + INCHI-1-API.ZIP
# + RDKit_2016_03_1.tgz

# centos:7 have already installed python 2.7.5.
FROM centos:7

# This file is created by Tetsuya Yamamoto.
MAINTAINER yamamoto@itmol.com

# Add files from Host
ADD add/ /tmp/add/

# Packages Install (from yum and pip)
RUN set -x \
    && mkdir /tmp/ext \
    && yum install -y python-devel python-pillow gcc-c++ boost-devel make cmake unzip \
    && curl -kL https://bootstrap.pypa.io/get-pip.py | python \ 
    && pip install numpy

# RDKit Install (Preparation)
RUN tar zxvf /tmp/add/RDKit_2016_03_1.tgz -C /usr/local/ \
    && mv /usr/local/rdkit-Release_2016_03_1 /usr/local/RDKit_2016_03_1 \
    && mkdir /usr/local/RDKit_2016_03_1/External/INCHI-API/src \
    && unzip /tmp/add/INCHI-1-API.ZIP -d /tmp/ext/ \
    && cp /tmp/ext/INCHI-1-API/INCHI_API/inchi_dll/* /usr/local/RDKit_2016_03_1/External/INCHI-API/src \
    && rm -r /tmp/ext/INCHI-1-API
ENV RDBASE /usr/local/RDKit_2016_03_1
ENV LD_LIBRARY_PATH /lib:$RDBASE/lib
ENV PYTHONPATH $RDBASE

# RDKit Install (Practice)
RUN mkdir $RDBASE/build \
    && cd $RDBASE/build \
    && cmake -DRDK_BUILD_INCHI_SUPPORT=ON -DBOOST_ROOT=/usr/lib64 -D PYTHON_EXECUTABLE=/usr/bin/python .. \
    && make \
    && make install

# Remove all Add folder and files (This command is excuting finaly)
RUN rm -r /tmp/add \
    && rm -r /tmp/ext

# Usage:
# build test(image name is itmol/rdkit:2016, log file name is log.txt)
#     docker build -t itmol/rdkit:2016a . > build_log.txt
# run test(container name is rdkit-container)
#     docker run -it --rm --name rdkit-container itmol/rdkit:2016a /bin/bash
