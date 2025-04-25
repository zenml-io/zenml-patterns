We use `uv` package manager, to install see instructions in https://docs.astral.sh/uv/getting-started/installation/

We can run the pipeline

```sh
uv sync --dev # needed once
uv run zenml init # needed once
uv run zenml login # needed once
# uv run zenml integration install -y gcp neptune # for our remote stack
uv run training-pipeline
```

When we run with `default` stack it works but when run remotely we get a message

```
File "/app/code/src/demo/steps/training_step.py", line 14, in <module>
from demo.training import train_model
ModuleNotFoundError: No module named 'demo'
```

We would ideally want to be able to be able to import packages inside our `src` folder or/and
the equivalent of installing the current folder as a package (even when working
with code repository feature)

```sh
uv pip install -e .
```

