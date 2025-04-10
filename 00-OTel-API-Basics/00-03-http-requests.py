import requests

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

from opentelemetry.instrumentation.requests import RequestsInstrumentor

# SDK setup (needed to see spans)
trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)

# Auto-instrument requests module
RequestsInstrumentor().instrument()

def call_slow_api():
    url = "http://httpbin.org/delay/2"
    response = requests.get(url)  # Automatically traced!
    return response.text

def main():
    print("Calling slow API...")
    result = call_slow_api()
    print("Done! Response length:", len(result))

if __name__ == "__main__":
    main()
