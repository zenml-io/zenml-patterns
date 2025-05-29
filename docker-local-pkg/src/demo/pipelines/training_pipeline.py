__all__ = ['training_pipeline', 'main']

from zenml import pipeline
from zenml.config import DockerSettings
from demo.steps.training_step import train  # in order for this import to work you need the DockerSettings defined below


@pipeline(
    enable_cache=False,
    settings = {"docker": 
            DockerSettings(
                python_package_installer="uv",
                local_project_install_command="uv pip install -e . --no-deps",
                allow_including_files_in_images=True,
            )
        }
)
def training_pipeline() -> None:
    train() 

def main():
    training_pipeline()
