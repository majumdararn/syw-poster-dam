<!-- omit in toc -->
# Guide for reproducibility

Authors: [Arnab Majumdar](https://github.com/majumdararn) and [Sebastian Busch](https://github.com/thamnos)

<!-- omit in toc -->
<!-- ## Introduction -->

This repository demonstrates the reproducibility of a scientific publication using [showyourwork](https://github.com/showyourwork/showyourwork) within the context of [DAPHNE4NFDI](https://www.daphne4nfdi.de/). The project generates a [poster](https://events.hifis.net/event/3368/contributions/22895/) that was presented at the [DAPHNE4NFDI Annual Meeting 2026](https://events.hifis.net/event/3368/overview).

This guide is designed to support reproducibility of the poster by providing step-by-step instructions for different types of users, including independent investigators. The [table of contents](#table-of-contents) outlines the various user roles. Please select the role that best matches your situation and follow the corresponding instructions.  

> If you like this project or find the poster interesting but do not have time to fully explore its reproducibility, that’s absolutely fine. You can still support the project in the following ways:
> - Star the project.
> - Refer this project in your project's readme.
> - Mention the project at local meetups and tell your friends/colleagues.



<!-- omit in toc -->
## Table of contents

- [Collaborators](#collaborators)
- [Independendent investogators](#independent-investogators)
  - [Reproduce locally and remotely](#reproduce-locally-and-remotely)
  - [Reproduce locally](#reproduce-locally)

## Collaborators

<!-- omit in toc -->
### Are you a collaborator?

You are a collaborator if you are a co-author of this poster. The collaborators can also reproduce as an independent investigator.

To reproduce the poster, make changes, and make changed poster publicly available as a collaborator; follow the following steps: 

1. Create access to Zenodo and overleaf,
2. Reproduce locally,
3. Edit and produce new poster remotely.

<!-- omit in toc -->
### Create access to Zenodo and overleaf

Showyourwork reproduces articles accessing the zenodo datasets and overleaf project (if applicable). So, local machine need to have access to zenodo (preferably also zenodo sandbox) and overleaf.
    
To access Zenodo (or Zenodo sandbox):
- Create a profile (or not already exists) in [Zenodo](https://zenodo.org/) (and preferably in [Zenodo sandbox](https://sandbox.zenodo.org/)) and log in.
- Create a [Zenodo token](https://zenodo.org/account/settings/applications/tokens/new/) (or [Zenodo sandbox token](https://sandbox.zenodo.org/account/settings/applications/tokens/new/))
- Use the following settings:
    - Name: ``ZENODO_TOKEN`` (or ``SANDBOX_TOKEN``).
    - Click on ``deposit:actions`` and ``deposit:write``.
    - Click on create
- Copy the code and keep it somewhere. This code can not to accessed later. In this guide, let's call this value ``$ZENODO_TOKEN`` (or ``$SANDBOX_TOKEN``).
- Add the code as a environment variable named ``ZENODO_TOKEN`` (and ``SANDBOX_TOKEN``) in your local computer
    - For Linux (ubuntu) system: add ``export ZENODO_TOKEN=$ZENODO_TOKEN`` (and ``export SANDBOX_TOKEN=$SANDBOX_TOKEN``) in your ``.bashrc`` script.

To access overleaf (if applicable):
- Ask project administrator for overleaf project access
- Create a profile in [overleaf](https://www.overleaf.com) and log in.
- Go to settings, scroll down to Git integration and click on ``add another token``.
- Copy the generated code and keep it. There is no way to get this code late
- The value of this code will be called ``$OVERLEAF_TOKEN``.
- Add the code as an environment variable named `OVERLEAF_TOKEN`.
    - For Linux (ubuntu) system: add ``export OVERLEAF_TOKEN=$OVERLEAF_TOKEN`` in your ``.bashrc`` script.

<!-- omit in toc -->
### Repoduce locally as collaborator

- It is recommended to install showyourwork inside a conda environment using ``pip install git+https://github.com/showyourwork/showyourwork`` command.
- Make a local clone of the repository using ``git clone``.
- Ensure `ZENODO_TOKEN`, `SANDBOX_TOKEN`, and `OVERLEAF_TOKEN` are added as environment variable in your local machine. In Linux (ubuntu) machine, one can check using ``echo`` command, e.g. ``echo ZENODO_TOKEN`` for zenodo token. In case they are not added, please refer [previous step](#create-access-to-zenodo-and-overleaf).
- Reproduce the poster using ``showyourwork build`` command inside the top directory in the cloned repository.

<!-- omit in toc -->
### Edit and produce changed poster remotely as collaborator

- To edit the poster, please make changes locally  and commit them using ``git add`` and ``git commit -m "your commit message"``. 
- To produce the edited poster locally, run ``showyourwork build`` with commited changes. If overleaf is integrated, the build command will check for changes in tex and bib files and automatically make a commit named `overleaf sync`.
- To the edited poster remotely, push the changes using ``git push``. This will trigger a wrokflow automated by CI/CD and create edited article remotely.

## Independendent investogators

<!-- omit in toc -->
### Are you an independent investigator?

You are an independent investigator if you are not a co-author of this poster.

  <!-- - [Reproduce locally and remotely](#reproduce-locally-and-remotely)
  - [Reproduce locally](#reproduce-locally) -->

### Reproduce locally and remotely

If you want to reproduce the poster, make changes, and make changed poster publicly available but you are not a collaborator, follow the following steps: 

1. Create access to Zenodo and overleaf,
2. Reproduce locally,
3. Edit and produce new poster remotely.

To create access to Zendo and overleaf, follow the same [steps](#create-access-to-zenodo-and-overleaf) as the collaborators.

To reproduce locally, fork the project in GitHub and clone the forked project locally. All other [steps](#repoduce-locally-as-collaborator) are same as the collaborators.

To edit and produce a new poster remotely, follow the same [steps](#edit-and-produce-changed-poster-remotely-as-collaborator) as the collaborators. The new poster will be built in the forked repository.

### Reproduce locally

If you simply want to check the reproducibility of this poster and have a feeling how showyourwork works; follow the following steps:

1. Create access to Zenodo and overleaf,
2. Reproduce locally,
3. Edit and produce new poster locally.

To create access to Zendo and overleaf, follow the same [steps](#create-access-to-zenodo-and-overleaf) as the collaborators.

To reproduce locally, clone the project locally. All other [steps](#repoduce-locally-as-collaborator) are same as the collaborators.

To edit and produce a new poster locally, follow the same [steps](#edit-and-produce-changed-poster-remotely-as-collaborator) as the collaborators. the new poster can not be uploaded remotely. If you want to make your changes publicly available, refer [instructions for reproducing locally and remotely](reproduce-locally-and-remotely). 