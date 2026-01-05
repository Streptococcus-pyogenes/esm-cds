# Contributing to ESM-CDS

Thank you for your interest in contributing to ESM-CDS! This project is structured as a research repository and aims to prioritize reproducibility and clarity over rapid iteration.

## Guidelines

- **Reproducibility first:** All experiments and changes should be driven by configuration files. Please do not make silent modifications to training scripts or default parameters.
- **No silent experimental changes:** Whenever you update training settings, hyperparameters, or data filtering criteria, document these changes in the appropriate config or experimental docs.
- **Config-driven experiments:** Use the `experiments/configs/` directory to store YAML/JSON config files for each run. The code should read settings exclusively from these configs.
- **Documentation:** Update the `docs/` files and README as needed when you add new features, methods, or findings. Clear documentation ensures others can understand and reproduce your work.
- **Pull requests:** Include the results (plots, tables, logs) of your experiments in the pull request description. Also describe the motivation and expected impact of the change.

We welcome feedback, bug reports, and feature requests via GitHub issues. Please use the provided templates to ensure we have all the necessary information to assist you.
