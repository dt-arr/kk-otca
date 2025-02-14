#### cd to cd 01-OTel-API-Traces/

#### Run `python OTEL-API-No-Op-defaults.py `
Traceback (most recent call last):
  File "/workspaces/kk-otca/01-OTel-API-Traces/OTEL-API-No-Op-defaults.py", line 1, in <module>
    from opentelemetry import trace
ModuleNotFoundError: No module named 'opentelemetry'

Notice the error.

To fix this, you would need the opentelemetry package.

Get the OpenTelemetry package by running the following command

`pip install opentelemetry-api`

Run the app again:

`python OTEL-API-No-Op-defaults.py`