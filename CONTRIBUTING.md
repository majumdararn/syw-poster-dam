<!-- omit in toc -->
# Guide for reproducibility

Authors: [Arnab Majumdar](https://github.com/majumdararn) and [Sebastian Busch](https://github.com/thamnos)

This repository demonstrates the reproducibility of a scientific publication using [showyourwork](https://github.com/showyourwork/showyourwork) within the context of [DAPHNE4NFDI](https://www.daphne4nfdi.de/). The project generates a [poster](https://events.hifis.net/event/3368/contributions/22895/) that was presented at the [DAPHNE4NFDI Annual Meeting 2026](https://events.hifis.net/event/3368/overview).

This guide is designed to support the reproducibility of the poster by providing step-by-step instructions for different types of users, including independent investigators. The [table of contents](#table-of-contents) outlines the various user roles. Please select the role that best matches your situation and follow the corresponding instructions.  

> If you like this project or find the poster interesting but do not have time to fully explore its reproducibility, that’s absolutely fine. You can still support the project in the following ways:
> - Star the project.
> - Refer to this project in your project's README.
> - Mention the project at local meetups and share it with your friends or colleagues.

<!-- omit in toc -->
## Table of contents

- [Collaborators](#collaborators)
- [Independent investigators](#independent-investigators)
  - [Reproduce locally and remotely](#reproduce-locally-and-remotely)
  - [Reproduce locally](#reproduce-locally)

## Collaborators

<!-- omit in toc -->
### Are you a collaborator?

You are a collaborator if you are a co-author of this poster. Collaborators can also reproduce the project as independent investigators.

To reproduce the poster, make changes, and make the modified poster publicly available as a collaborator, follow these steps: 

1. Create access to Zenodo and Overleaf,
2. Reproduce locally,
3. Edit and produce a new poster remotely.

<!-- omit in toc -->
### Create access to Zenodo and Overleaf

Showyourwork reproduces articles by accessing Zenodo datasets and Overleaf projects (if applicable). Therefore, your local machine needs access to Zenodo (preferably also the Zenodo sandbox) and Overleaf.
    
To access Zenodo (or Zenodo sandbox):
- Create a profile (if it does not already exist) on [Zenodo](https://zenodo.org/) (and preferably also on [Zenodo sandbox](https://sandbox.zenodo.org/)) and log in.
- Create a [Zenodo token](https://zenodo.org/account/settings/applications/tokens/new/) (or a [Zenodo sandbox token](https://sandbox.zenodo.org/account/settings/applications/tokens/new/)).
- Use the following settings:
    - Name: `ZENODO_TOKEN` (or `SANDBOX_TOKEN`)
    - Select `deposit:actions` and `deposit:write`
    - Click on "Create"
- Copy the generated token and store it securely. This token cannot be accessed later. In this guide, we refer to it as `$ZENODO_TOKEN` (or `$SANDBOX_TOKEN`).
- Add the token as an environment variable named `ZENODO_TOKEN` (and `SANDBOX_TOKEN`) on your local computer.
    - For Linux (Ubuntu): add `export ZENODO_TOKEN=$ZENODO_TOKEN` (and `export SANDBOX_TOKEN=$SANDBOX_TOKEN`) to your `.bashrc`.

To access Overleaf (if applicable):
- Ask the project administrator for access to the Overleaf project.
- Create a profile on [Overleaf](https://www.overleaf.com) and log in.
- Go to Settings -> scroll down Git integration -> click on `Add another token`.
- Copy the generated token and store it securely. There is no way to retrieve it later.
- Refer to this value as `$OVERLEAF_TOKEN`.
- Add it as an environment variable named `OVERLEAF_TOKEN`.
    - For Linux (Ubuntu): add `export OVERLEAF_TOKEN=$OVERLEAF_TOKEN` to your `.bashrc`.

<!-- omit in toc -->
### Reproduce locally as a collaborator

- It is recommended to install showyourwork inside a conda environment using `pip install git+https://github.com/showyourwork/showyourwork`.
- Clone the repository locally using `git clone`.
- Ensure `ZENODO_TOKEN`, `SANDBOX_TOKEN`, and `OVERLEAF_TOKEN` are set as environment variables on your machine.  
  On Linux (Ubuntu), you can check using `echo $ZENODO_TOKEN`, etc.  
  If not set, refer to the [previous step](#create-access-to-zenodo-and-overleaf).
- Reproduce the poster using `showyourwork build` in the top-level directory of the cloned repository.

<!-- omit in toc -->
### Edit and produce a modified poster remotely as a collaborator

- To edit the poster, make changes locally and commit them using `git add` and `git commit -m "your commit message"`.
- To build the edited poster locally, run `showyourwork build`. If Overleaf is integrated, this may automatically create a commit named `overleaf sync`. Sometimes, `showyourwork build` is required before building.
- To produce the edited poster remotely, push your changes using `git push`. This will trigger a CI/CD workflow and generate the updated article remotely.

## Independent investigators

<!-- omit in toc -->
### Are you an independent investigator?

You are an independent investigator if you are not a co-author of this poster.

### Reproduce locally and remotely

If you want to reproduce the poster, make changes, and make the modified poster publicly available but are not a collaborator, follow these steps: 

1. Create local access to Zenodo and Overleaf,
2. Reproduce locally,
3. Edit and produce a new poster remotely.

To create access to Zenodo and Overleaf from local machine, follow the same [steps](#create-access-to-zenodo-and-overleaf) as collaborators.

To reproduce locally, fork the project on GitHub. Inside the forked project, go to settings -> secrets -> actions -> actions-> new and create three tokens named `ZENODO_TOKEN`, `SANDBOX_TOKEN`, and `OVERLEAF_TOKEN` and put appropiate values. Thereafter, clone your fork and follow all other [steps](#reproduce-locally-as-a-collaborator), same as the collaborators.

To edit and produce a new poster remotely, follow the same [steps](#edit-and-produce-a-modified-poster-remotely-as-a-collaborator). The new poster will be built in your forked repository.

### Reproduce locally

If you only want to check the reproducibility of this poster and understand how showyourwork works, follow these steps:

1. Create access to Zenodo and Overleaf,
2. Reproduce locally,
3. Edit and produce a new poster locally.

To create access to Zenodo and Overleaf, follow the same [steps](#create-access-to-zenodo-and-overleaf) as collaborators.

To reproduce locally, clone the project. All other [steps](#reproduce-locally-as-a-collaborator) are the same as for collaborators.

To edit and produce a new poster locally, follow the same [steps](#edit-and-produce-a-modified-poster-remotely-as-a-collaborator). The new poster cannot be uploaded remotely. If you want to make your changes publicly available, refer to the [instructions for reproducing locally and remotely](#reproduce-locally-and-remotely).