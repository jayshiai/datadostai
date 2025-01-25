<div align="center">

<h1>DataDost AI</h1>

[![CI | Test Handler](https://github.com/runpod-workers/worker-template/actions/workflows/CI-test_handler.yml/badge.svg)](https://github.com/runpod-workers/worker-template/actions/workflows/CI-test_handler.yml)
&nbsp;
[![CD | Build-Test-Release](https://github.com/runpod-workers/worker-template/actions/workflows/build-test-release.yml/badge.svg)](https://github.com/runpod-workers/worker-template/actions/workflows/build-test-release.yml)

🚀 | A simple worker that can be deployed on Cloud to handle our AI workloads for DataDost.

</div>

## 📖 | Getting Started

1. Clone this repository.
2. Install the dependencies using `pip install -r builder/requirements.txt`.
3. Cache the models using `python builder/cache_models.py`.
4. Start local server using `python src/handler --rp_serve_api`. Refer to this [Link](https://docs.runpod.io/category/development) for more information.

### 🧪 | Testing

To test without running the local server, you can use the following commands:

1. Test the handler using `python src/handler --test_input '{"input": {"text": "John Doe"}}'`.
2. Alternatively create a `text_input.json` and test the handler using `python src/handler'`. This will use the `text_input.json` file as input.

### 🚀 | Deployment

1. Build the docker image using `docker build -t <username>/<repo>:<tag> .`.
2. Push the docker image to the registry using `docker push <username>/<repo>:<tag>`.
3. Run the docker image using `docker run -p 8080:8080 <username>/<repo>:<tag>`.

## 🔗 | Links

🐳 [Docker Container](https://hub.docker.com/r/jayshiai/datadost)
