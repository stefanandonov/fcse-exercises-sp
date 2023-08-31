# Use an ARM-compatible base image
FROM ubuntu
#FROM thomasweise/texlive

# Install required packages
RUN apt-get update && \
    apt-get install -y pandoc python3.11 python3-pip

RUN apt-get update && apt-get install texlive-xetex -y

#install pypandoc library
RUN    pip3 install pypandoc


# Create a working directory
WORKDIR /app

# Copy the contents of the /src folder and the python script
COPY src /app/src
COPY create_files.py /app/create_files.py

# Create an entrypoint script
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Set the entrypoint to keep the container alive
ENTRYPOINT ["/app/entrypoint.sh"]