import requests

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

# Set up the tracer provider and console exporter
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Configure the processor to print spans to the console
span_processor = SimpleSpanProcessor(ConsoleSpanExporter())
trace.get_tracer_provider().add_span_processor(span_processor)

def call_slow_api():
    with tracer.start_as_current_span("call_httpbin_delay"):
        url = "http://httpbin.org/delay/2"
        response = requests.get(url)
        return response.text

def main():
    with tracer.start_as_current_span("main_function_span") as span:
        print("Calling slow API...")
        result = call_slow_api()
        print("Done! Response length:", len(result))

if __name__ == "__main__":
    main()
