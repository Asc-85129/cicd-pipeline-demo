# CI/CD Pipeline Demo (GitHub Actions + Kubernetes, no Docker)

A small Flask service with a GitHub Actions pipeline:

1. **CI** - flake8 lint, pytest unit tests, package a release artifact.
2. **CD** - start a k3s Kubernetes cluster (containerd runtime) on the runner, publish the
   app code as a ConfigMap, deploy to a 2-replica Deployment on the stock `python:3.11-slim`
   image, wait for rollout and smoke-test the NodePort service.

No Docker or Docker Hub is used: k3s runs containers via containerd, and the application
code is delivered through a ConfigMap instead of a custom image.

Run locally:

```
pip install -r app/requirements.txt pytest
pytest -v tests
python app/app.py
```
