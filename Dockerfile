# Use an appropriate base image
FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y \
    pandoc \
    python3.11 \
    texlive-xetex

# Install pypandoc
# command sasd change testasdasdasdasdasd
RUN python3.11 -m pip install --upgrade pip && \
    pip install pypandoc \