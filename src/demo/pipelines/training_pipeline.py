__all__ = ['training_pipeline', 'main']

from zenml import pipeline
from zenml.config import DockerSettings
from demo.steps.training_step import train

@pipeline(
        enable_cache=False,
        settings = {"docker": DockerSettings(
            dockerfile="Dockerfile", 
            build_context_root=".",
            build_config={"build_options": {"platform": "linux/amd64"}},
            python_package_installer="uv",
            # prevent_build_reuse=True
            )
        }
)
def training_pipeline() -> None:
    train() 

def main():
    training_pipeline()
