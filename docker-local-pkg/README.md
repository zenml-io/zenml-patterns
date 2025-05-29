# Minimal example repo for using custom libraries with ZenML

This repository demonstrates how to properly use and reference custom local libraries with ZenML pipelines, particularly when running on remote stacks like Azure or GCP Vertex AI.

## Motivation

When working with ZenML pipelines that use custom local libraries, you might encounter these common issues:

1. **Local vs Remote Import Issues**: Your code works locally but fails on remote stacks because the local packages aren't properly included in the Docker image
2. **Python Path Problems**: Modules in your `src` directory are importable locally but not found when running on remote stacks
3. **Package Installation Challenges**: Simply adding packages to `requirements.txt` doesn't work because the local package structure isn't preserved

This repo provides a solution that ensures your local packages are properly installed in the Docker image while maintaining the correct package structure.

## How It Works

The solution works by:
1. Installing your local package in editable mode in the Docker image
2. Preserving the package structure while allowing ZenML to load the actual code at runtime
3. Ensuring all imports work correctly both locally and remotely

## Prerequisites

- Your git repository and ZenML root must be at the same level for this to work
- You need to have `uv` installed for package management

## Setup
```sh
uv sync --dev
uv run zenml init
uv run zenml login
uv run zenml project set default
```

## Running Pipelines

### Local Execution
```sh
uv run zenml stack set default
uv run training-pipeline
```

This will run the pipeline defined in `src/demo/pipelines/training_pipeline.py` using your local environment with the demo package installed in editable mode.

### Remote Execution

In this case we will run on GCP but this will also work for other remote orchestrators.

```sh
uv run zenml stack set <...> 
uv run zenml integration install gcp
uv run training-pipeline
```

When running remotely, ZenML will:

1. **Build the Docker Image**:
   - Start with the base ZenML image
   - Mock the local project path at `/app/code`
   - Install the local project in editable mode
   - Clean up mocked files while preserving the folder structure

2. **Deploy the Pipeline**:
   - Push the Docker image to the container registry
   - Optionally push code to the artifact store
   - Launch the run on the orchestrator

3. **Execute the Pipeline**:
   - The orchestrator pulls the Docker image
   - The entrypoint loads your code into the correct location
   - All local package imports work as expected

## Limitations

- Requires git and ZenML root to be at the same level
- May need adjustments for complex package structures
- Consider the size of your local packages when building Docker images
