# ZenML Patterns

A collection of proven patterns, best practices, and practical solutions for ZenML pipelines. Each pattern demonstrates how to solve common challenges in ML pipeline development, from local development to production deployment.

## Why ZenML Patterns?

When working with ZenML, you might encounter various challenges:
- How to properly containerize local packages
- How to handle custom data types
- How to optimize pipeline performance
- How to manage dependencies across different environments

This repository provides battle-tested solutions to these challenges, helping you build more robust and maintainable ML pipelines.

## Available Patterns

### [Local Package Docker](local-package-docker/)
Learn how to properly include custom local libraries with ZenML pipelines, particularly when running on remote stacks like Sagemaker or GCP Vertex AI or Kubernetes. This pattern solves common issues with:
- Local vs Remote Import Issues
- Python Path Problems
- Package Installation Challenges

## Contributing

We welcome contributions! If you have a pattern that has worked well for you, please consider sharing it. To contribute:

1. Create a new directory for your pattern
2. Include a clear README explaining the problem and solution
3. Provide working example code
4. Submit a pull request