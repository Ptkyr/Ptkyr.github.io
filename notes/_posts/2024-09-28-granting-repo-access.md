---
layout: post
title: "Granting private repository access"
categories: school
author: ptkyr
---

This is a quick reference for anyone (me) wanting to share a private git repository with an employer/friend/whoever. Also, if you are a prospective employer (perhaps sent here from my [resume](/resume.pdf)) who wants to view one of my private projects, please send me an email and I will set up an access token for you.

## GitLab
Under `Project -> Settings -> Access tokens`, create an access token with the **Developer** role and **read_repository** only. Copy and save it somewhere because it will disappear. Anyone can now clone the project using:
```
git clone https://gitlab-ci-token:TOKEN@git.uwaterloo.ca/user/project.git
```

## GitHub
Under `Settings -> Developer settings -> Personal access tokens`, create a new fine-grained token making sure to only grant access to a specific repository and with read-only `Content` and `Metadata` permissions. Anyone can now clone the project using:
```
git clone https://fakename:TOKEN@github.com/user/project
```
The `fakename` field above doesn't matter and doesn't need to be changed, it just has to be non-empty.
