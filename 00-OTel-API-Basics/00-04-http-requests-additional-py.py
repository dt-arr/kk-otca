import requests

from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry import trace

# Set up tracing
trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)

# Auto-instrument requests
RequestsInstrumentor().instrument()

def call_httpbin_delay():
    url = "http://httpbin.org/delay/2"
    return requests.get(url).text

def call_httpbin_status():
    url = "http://httpbin.org/status/418"
    return requests.get(url).text

def call_httpbin_ip():
    url = "http://httpbin.org/ip"
    return requests.get(url).text

def main():
    print("Calling httpbin delay...")
    print("Response length:", len(call_httpbin_delay()))

    print("\nCalling httpbin status (418)...")
    print("Response length:", len(call_httpbin_status()))

    print("\nCalling httpbin IP...")
    print("Response:", call_httpbin_ip())

if __name__ == "__main__":
    main()
