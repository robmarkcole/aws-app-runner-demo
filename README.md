# app-runner-demo
Demo application for AWS App Runner using [starlette](https://www.starlette.io/) following example [hello-app-runner](https://github.com/aws-containers/hello-app-runner). Can be used to host ML models using [fastai2-Starlette](https://github.com/muellerzr/fastai2-Starlette). App Runner is not yet available in London region so apps run in Ireland region.

- https://docs.aws.amazon.com/apprunner/latest/dg/what-is-apprunner.html and https://github.com/aws-containers/hello-app-runner
- two routes to deplolment (a) code (b) docker image on ECR

## Docker
```
docker build -t app-runner-demo .
docker run -p 8000:8000 app-runner-demo:latest
```

## Dev
* `python3 -m venv venv`
* `source venv/bin/activate`
* `pip3 install -r requirements.txt`
* `python3 app.py`

## Deployment
Deploying from github repo using the `apprunner.yaml` file is working OK.

Using deployment approach (b) using ECR, getting error: `Error in assuming access role arn:aws:iam::118655806378:role/service-role/AppRunnerECRAccessRole`