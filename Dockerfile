FROM zenmldocker/zenml:py3.11

RUN mkdir -p /app/code

WORKDIR /app/code

# create empty src/demo directory and add __init__.py
RUN mkdir -p src/demo

# Copy the README.md file
COPY README.md .

# Copy only the pyproject.toml first to leverage Docker layer caching
COPY pyproject.toml .

# Install the package in development mode without dependencies
RUN pip install uv
RUN uv pip install -e . --no-deps  

# Remove the pyproject.toml and README.md after installation
RUN rm pyproject.toml README.md     

# Remove /app/code directory
RUN rm -rf /app/code

# reset the working directory
WORKDIR /app
