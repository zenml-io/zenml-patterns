FROM zenmldocker/zenml:py3.11

RUN mkdir -p /app/code/src/demo
RUN touch /app/code/src/demo/__init__.py

WORKDIR /app/code

# Copy the pyproject.toml
COPY pyproject.toml .

# Copy the README.md file because pyproject.toml references it
COPY README.md .

# Install the package in development mode without dependencies
RUN pip install uv
RUN uv pip install -e . --no-deps  

# Remove the pyproject.toml and README.md after installation
RUN rm pyproject.toml README.md     

# Remove /app/code directory to avoid clashes during code download in the step entrypoint
RUN rm /app/code/src/demo/__init__.py
RUN rm -rf /app/code

# reset the working directory
WORKDIR /app