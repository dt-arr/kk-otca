#### cd to cd 01-OTel-API-Traces/


#### Run the file that contains python 00-01-OTel-API.py

 `> python 00-01-OTel-API.py`

 Output:

`Calling slow API...
Done! Response length: 358`

Notice that it works successfully but that spans although generated are never seen or exported anywhere.

## To see the span, we need to more than the API, we would use the SDK to 

Add the following:

`from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter`

Then, add the processor that processes the spans immediately and passes on to the exporter
The exporter then sends the span to the console

# Configure the processor to print spans to the console
span_processor = SimpleSpanProcessor(ConsoleSpanExporter())
trace.get_tracer_provider().add_span_processor(span_processor)


### Run `python 00-02.py` that has Span processors and exporters which are part of the SDK:

Note the new spans:


`
python .\00-02.py
Calling slow API...
{
    "name": "call_httpbin_delay",
    "context": {
        "trace_id": "0xcf092b60818fe5496540ae5d5ec1da84",
        "span_id": "0xd632174e9bd31a35",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": "0x91eda442d7e66f8a",
    "start_time": "2025-04-10T12:44:44.290685Z",
    "end_time": "2025-04-10T12:44:47.061045Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {},
    "events": [],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.31.1",
            "service.name": "unknown_service"
        },
        "schema_url": ""
    }
}
Done! Response length: 358
{
    "name": "main_function_span",
    "context": {
        "trace_id": "0xcf092b60818fe5496540ae5d5ec1da84",
        "span_id": "0x91eda442d7e66f8a",
        "trace_state": "[]"
    },
    "kind": "SpanKind.INTERNAL",
    "parent_id": null,
    "start_time": "2025-04-10T12:44:44.290444Z",
    "end_time": "2025-04-10T12:44:47.062921Z",
    "status": {
        "status_code": "UNSET"
    },
    "attributes": {},
    "events": [],
    "links": [],
    "resource": {
        "attributes": {
            "telemetry.sdk.language": "python",
            "telemetry.sdk.name": "opentelemetry",
            "telemetry.sdk.version": "1.31.1",
            "service.name": "unknown_service"
        },
        "schema_url": ""
    }
}


`






## old notes:

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


### requests is not a built in module, therefore you will have to install it.

Traceback (most recent call last):
  File "C:\Data\OTel\kk-otca\00-OTel-API-Basics\00-no-instrumentation.py", line 1, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'..


### To export Spans you need the SDK:

from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

Traceback (most recent call last):
  File "C:\Data\OTel\kk-otca\00-OTel-API-Basics\00-02.py", line 4, in <module>
    from opentelemetry.sdk.trace import TracerProvider
ModuleNotFoundError: No module named 'opentelemetry.sdk'



PS C:\Data\OTel\kk-otca\00-OTel-API-Basics> pip install opentelemetry.sdk
Defaulting to user installation because normal site-packages is not writeable
Collecting opentelemetry.sdk
  Downloading opentelemetry_sdk-1.31.1-py3-none-any.whl.metadata (1.6 kB)
Requirement already satisfied: opentelemetry-api==1.31.1 in c:\users\amrit\appdata\local\packages\pythonsoftwarefoundation.python.3.13_qbz5n2kfra8p0\localcache\local-packages\python313\site-packages (from opentelemetry.sdk) (1.31.1)
Collecting opentelemetry-semantic-conventions==0.52b1 (from opentelemetry.sdk)
  Downloading opentelemetry_semantic_conventions-0.52b1-py3-none-any.whl.metadata (2.5 kB)
Collecting typing-extensions>=3.7.4 (from opentelemetry.sdk)
  Downloading typing_extensions-4.13.1-py3-none-any.whl.metadata (3.0 kB)
Requirement already satisfied: deprecated>=1.2.6 in c:\users\amrit\appdata\local\packages\pythonsoftwarefoundation.python.3.13_qbz5n2kfra8p0\localcache\local-packages\python313\site-packages (from opentelemetry-api==1.31.1->opentelemetry.sdk) (1.2.18)
Requirement already satisfied: importlib-metadata<8.7.0,>=6.0 in c:\users\amrit\appdata\local\packages\pythonsoftwarefoundation.python.3.13_qbz5n2kfra8p0\localcache\local-packages\python313\site-packages (from opentelemetry-api==1.31.1->opentelemetry.sdk) (8.6.1)
Requirement already satisfied: wrapt<2,>=1.10 in c:\users\amrit\appdata\local\packages\pythonsoftwarefoundation.python.3.13_qbz5n2kfra8p0\localcache\local-packages\python313\site-packages (from deprecated>=1.2.6->opentelemetry-api==1.31.1->opentelemetry.sdk) (1.17.2)
Requirement already satisfied: zipp>=3.20 in c:\users\amrit\appdata\local\packages\pythonsoftwarefoundation.python.3.13_qbz5n2kfra8p0\localcache\local-packages\python313\site-packages (from importlib-metadata<8.7.0,>=6.0->opentelemetry-api==1.31.1->opentelemetry.sdk) (3.21.0)
Downloading opentelemetry_sdk-1.31.1-py3-none-any.whl (118 kB)
Downloading opentelemetry_semantic_conventions-0.52b1-py3-none-any.whl (183 kB)
Downloading typing_extensions-4.13.1-py3-none-any.whl (45 kB)
Installing collected packages: typing-extensions, opentelemetry-semantic-conventions, opentelemetry.sdk
Successfully installed opentelemetry-semantic-conventions-0.52b1 opentelemetry.sdk-1.31.1 typing-extensions-4.13.1

[notice] A new release of pip is available: 24.3.1 -> 25.0.1
[notice] To update, run: C:\Users\amrit\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip
PS C:\Data\OTel\kk-otca\00-OTel-API-Basics> 


