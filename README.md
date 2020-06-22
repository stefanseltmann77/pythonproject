# TODO on Setup
- First read this README to the end
- Rename the my_project_module to your desired project name
- Delete folders and files from the my_project_module you don't need
    - setup.py is needed, if you want to pass all on as an installable package (wheel).
- If you need the setup.py adjust:
    - name, description
    - author, author_email 
    - packages (module names)
- Delete the contents for this README file and replace with project readme. 

# Config-Files
## Location
- conf folder within module/package
- contains default config, that may be overwritten in run-scripts
## Technology
- Config-Parser ist still used
- Python files instead of .ini, .json or .yaml:
- no additional installation
- no additional formats
- easy import on different environments
- easy to update

## Special files
### pylintrc.cfg
Standard config for pylint, should be adjusted for project requirements.
DEPRECATED: The file is still included in order to give an overview of possible configs.
Please use the new more modern setup.cfg for pylint configs.
Run like ``pylint my_project_module --rcfile ./setup.cfg``.

### environment.yml
Definition of a requirements file for a conda environment. 
This file is just an example and can be used for creation 
of a individual conda environment for the project. 

### setup.cfg
As a replacement for separate config files, the combining setup.cfg should be used.
There are blocks in it for Pylint and Mypy as an example.

### setup.py
Config file for building wheel files.
Run like ``python setup.py bdist_wheel``.

# Test-Folder
## Location
The Test-Folder is part of the module/package and should be deployed with it.
## Technology
- use pytest whenever possible instead of unittest
- use the same folder structure as the project for your tests

# Runnable Scripts
## Location
- run folder *outside* the module
- executables *only* in run
- personal run script, like scratches, belong outside the project, not even in run.
  use a personal folder, that can be added to the .gitignore
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
Use git.

### gitignore
Never use the ignore functionality within the JetBrains tool. Always use the .gitignore file in the root directory.
Exclusion of files from git is so critical that it must work independent of a IDE.

# Linting
## Technology
We use Pylint as the linting tool. Every project has it's own pylintrc.cfg in the config folder.

DON'T rely on a option pylint integration in PyCharm because ...
- the exact settings may be project specific and therefore should be derived from a config file within the project.
- the linting functionality should by available independent of the IDE (similar with gitignore).

# Type Checker
## mypy
Mypy is the preferred type checker. It is included as a dependency in the environment.yml.
The configs will be pulled per default fallback from the setup.cfg.
Run from root like ``mypy my_project_module``.
 
 

# Scratches
Scratches are little scripts of code to get things done, but that aren't part of the project per se.
## Location
Put them in a separate folder that is ignored by git. 
I propose a folder called desktop for stuff that isn't properly sorted away. 
There is already an entry in the .gitingore ignoring a folder with that name.
