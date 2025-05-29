import os
import time
from typing import Any, Dict, List, Optional

from zenml import pipeline, step
from zenml.client import Client
from zenml.exceptions import EntityExistsError
from zenml.config import DockerSettings

STACK_NAME = "axj-gcp-stack"
PROJECT_NAME = "default"
BASE_TEMPLATE_NAME = "simple_ml_pipeline_template"
MAIN_TRIGGER_TEMPLATE_NAME = "main_trigger_pipeline"


@step(enable_cache=False)
def trigger_run_templates(template_name: str, configs: List[Optional[Dict[str, Any]]]):
    
    client = Client()
    template = client.get_run_template(template_name)

    for config in configs:
        time.sleep(1)

        # Trigger the pipeline with the updated configuration
        run = Client().trigger_pipeline(
            template_id=template.id,
            run_configuration=config,
        )

        print(f"Run of pipeline triggered with {config['steps']['train_model']['parameters']['n_estimators']} estimators.")


@pipeline(
    settings = {"docker": 
        DockerSettings(
            python_package_installer="uv"
        )
    }
)
def main_trigger_pipeline():

    trigger_run_templates(template_name=BASE_TEMPLATE_NAME)
        

if __name__ == "__main__":

    # Set the active project and stack
    client = Client()
    client.set_active_project(PROJECT_NAME)
    remote_stack = client.get_stack(STACK_NAME)
    os.environ["ZENML_ACTIVE_STACK_ID"] = str(remote_stack.id)
    
    # Create the run template for the base pipeline
    try:
        from pipeline import simple_ml_pipeline

        template = simple_ml_pipeline.create_run_template(name=BASE_TEMPLATE_NAME)
    except EntityExistsError:
        template = client.get_run_template(BASE_TEMPLATE_NAME)

    # Create a batch of configs to use for the base pipeline
    configs: List[Optional[Dict[str, Any]]] = []
    for i in range(10):
        config: Optional[Dict[str, Any]] = template.config_template

        config["steps"]["train_model"]["parameters"]["n_estimators"] = i*10

        configs.append(config)

    # Create the run template for the main trigger pipeline
    params = {
            "trigger_run_templates": {
                "parameters": {
                    "configs": configs,
                    "template_name": BASE_TEMPLATE_NAME
                }
            }
        }
    collective_template = main_trigger_pipeline.with_options(
        step_configurations=params
    )

    collective_template.create_run_template(name=MAIN_TRIGGER_TEMPLATE_NAME)


    





