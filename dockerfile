# Use Python base image
FROM python:3.9-slim

# Create and set Tsinghua mirror for apt
RUN echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye main contrib non-free" > /etc/apt/sources.list && \
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-updates main contrib non-free" >> /etc/apt/sources.list && \
    echo "deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-backports main contrib non-free" >> /etc/apt/sources.list

# Install Calibre dependencies
RUN apt-get update && apt-get install -y \
    calibre \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy the script
COPY epub2azw.py .

# Create input and output directories
RUN mkdir -p /app/input /app/output

# Set pip to use Tsinghua mirror
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# Set environment variables
ENV INPUT_DIR=/app/input
ENV OUTPUT_DIR=/app/output

# Command to run the script
ENTRYPOINT ["python", "epub2azw.py"]