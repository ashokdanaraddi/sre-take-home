# SRE Take-Home

Welcome! The goal of this exercise is to highlight your skills as an SRE.

## Required Tools
- Docker
- Minikube
- Git

## Scenario

An engineering team you are working with has developed a new service called `user_hasher`. They've taken a first stab at containerizing their application and are off to a good start. It builds, runs, and serves traffic like anyone would expect. They've even built a convenient helper script for local development called `build_and_run.sh`. In the team standup you are presented with all of this and asked "What do we need to do to ship user_hasher?".

## Kubernetes

- The service will run on a standard Kubernetes cluster in the `user_hasher` namespace.
- This service needs to support zero-downtime deployments.

## Plan

Identify and prioritize tasks that would be required to get this running in Kubernetes. Explain how you'd approach breaking down this project and include key requirements.

**Deliverable #1: Create /PLAN.md and commit it locally**

## Manifest

Create a Kubernetes manifest for deploying this service to the cluster. The service will function without any salt provided, but we'd need to provide it in production. Create a test secret in the namespace called `user_salt` with the value "TESTSALT". Mount the secret as the environment variable `USER_SALT`.

Verification: When providing `user_id` of "TESTUSERID" and a `USER_SALT` of "TESTSALT", the `/user_hash` endpoint should return:
```
> curl 'localhost:8000/user_hash?user_id=TESTUSERID'
"9f1021612c2a810d26472a66e4064f6608d52fd3"
```
**Deliverable #2: create /user_hasher.yaml and commit it locally**

## Metrics

Build out a `/metrics` endpoint using the [aioprometheus](https://aioprometheus.readthedocs.io/en/latest/user/index.html) module that exposes the following pieces of information to the [Prometheus server](https://prometheus.io/docs/concepts/metric_types/):
- Request duration
- Response status codes (2xx, 3xx, 4xx, 5xx)
- User hashes generated (cumulative)

Make sure to label the metrics with:
- Application version
- Pod IP
- Node IP

**Deliverable #3: Modify main.py and commit it locally**

## Submitting

Once you have committed all of your work to your local clone of this repo, archive your work and submit it via link in an email (attachments have been known to cause issues).

Assuming you were performing work on the `main` branch, the command to archive the branch as a zip is as follows:

```
tar -czvf sre-take-home.tar.gz sre-take-home
```
