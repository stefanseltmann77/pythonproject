# Config-Files
## Location
- conf folder within module
- contains default config, that may be overwritten
## Technology
- Config-Parser ist still used
- Python files instead of .ini,.json or .yaml:
- no additional installation
- no additional formats
- easy import on different environments
- easy to update

## Special files
### pylintrc.cfg
Standard config for pylint, adjusted for ACODS-project requirements.

### environment.yml
Definition of a requirements file for a conda environment. This file is just an example and can be used for creation 
of a individual conda environment for the project. 

# Test-Folder
## Location
The Test-Folder is part of the Module and should be deployed with it.
## Technology
- use pytest whenever possible instead of unittest
- use the same folder structure as the project for your tests

# Runnable Scripts
## Location
- run folder *outside* the module
- executables *only* in run
- personal run script as scratches or outside the project, not even in run
- use shebang line instead of source activate for switching enviroments

# Logging
## Location
- logfiles should be placed somewhere *outside* of the project scope
- if logfiles are generated inside the project scope, please use the .gitignore 
in order to avoid cluttering the repo with logs
## Technology
We use the default logging module of python.
### Logging config
Use a global configuration based on the logging_conf.py. This is the most flexible
way for logging configs, that also allows filtering.

# VCS
## Technology
We use git.

### gitignore
Never use the ignore functionality within the Jetbrains tool. Always use the .gitignore file in the root directory.
Exclusion of files from git is so critical that it must work independend of a IDE.

# Linting
## Techology
We use Pylint as the linting tool. Every project has it's own pylintrc.cfg in the config folder.

DON'T rely on a option pylint integration in PyCharm because ...
- the exact settings may be project specific and therefore should be derived from a config file within the project.
- the linting functionality should by available independ of the IDE (similar with gitignore).
