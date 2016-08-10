# Image name : itmol/rdkit:2016a
# This image is for Cheminformatics with rdkit.
# Build test is excuted in 07/08/2016.
# This is alpha version(shows 2016"a"), some software are installed through internet.

# centos:7 have already installed python 2.7.5.
FROM itmol/rdkit:2016a

# This file is created by Tetsuya Yamamoto.
MAINTAINER yamamoto@itmol.com

# Packages Install (from yum and pip)
RUN set -x


# Usage:
# build test(image name is itmol/rdkit-postgres:2016, log file name is build_log.txt)
#     docker build -t itmol/rdkit-postgres:2016a . > build_log.txt
# run test(container name is rdkit-postgres-container)
#     docker run -it --rm --name rdkit-postgres-container itmol/rdkit-postgres:2016a /bin/bash
