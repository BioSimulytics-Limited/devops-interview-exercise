> [!IMPORTANT]  
> This is a DevOps interview exercise for BioSimulytics Limited. Please do not share your solution publicly.

# DevOps Interview Exercise
Our [weather prediction microservice](https://github.com/orgs/BioSimulytics-Limited/packages/container/package/dummy-weather-api) **keeps crashing in production** and killing its container. We're seeing it in the logs, but we don't know why! Documentation for the service can be found in [WEATHER_API_DOCS.md](WEATHER_API_DOCS.md).

## Running the Service
**Requirements:** Docker, Docker Compose v2, Python 3.10+

We've provided the production `docker-compose.yml` file that will run the service locally and a python script `test_endpoint.py` that will hit the service with a load of requests.

## Deliverables
Your job is to build an observability/monitoring service that can help us understand why our microservice is crashing. The service should capture and display the following performance metrics:
- memory usage
- CPU usage
- network I/O
- restart rate
- logs

Using this data, figure out the root cause of the crash and explain your findings in a brief paragraph.

> [!NOTE]
> You can use any tech stack you want, but the simpler the better.
> You may use AI to assist you, but you must disclose use of AI in your solution and how it was used.