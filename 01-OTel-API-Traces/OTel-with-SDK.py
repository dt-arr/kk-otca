from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider, SpanProcessor
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.resources import Resource
import time
import uuid

# Set up OpenTelemetry resources and TracerProvider
resource = Resource.create({"service.name": "sample-app"})
trace_provider = TracerProvider(resource=resource)
trace.set_tracer_provider(trace_provider)

# Create a console exporter and add to the span processor
console_exporter = ConsoleSpanExporter()
span_processor = SimpleSpanProcessor(console_exporter)
trace_provider.add_span_processor(span_processor)

# Create a tracer
tracer = trace.get_tracer("otel-sdk-demo")

# Function to simulate span context and calculate duration
def simulate_tracing_api():
    # Start time for root span
    root_span_start_time = time.time()

    # Simulate starting a root span
    with tracer.start_as_current_span("root-span") as root_span:
        root_span.set_attribute("example.attribute", "root-span-attribute")
        root_span.add_event("root-span-started")
        
        # Simulate work done in root span
        time.sleep(1)  # Simulating 1 second of work
        
        # End time for root span and calculate duration
        root_span_end_time = time.time()
        root_span_duration = root_span_end_time - root_span_start_time

        print(f"Root Span ID: {root_span.context.trace_id}")
        print(f"Root Span Name: {root_span.name}")
        print(f"Root Span Attributes: {root_span.attributes}")
        print(f"Root Span Events: {root_span.events}")
        print(f"Root Span Duration: {root_span_duration:.4f} seconds")
        
        # Simulate starting a child span
        child_span_start_time = time.time()
        with tracer.start_as_current_span("child-span") as child_span:
            child_span.set_attribute("example.attribute", "child-span-attribute")
            child_span.add_event("child-span-started")
            
            # Simulate work done in child span
            time.sleep(0.5)  # Simulating 0.5 seconds of work

            # End time for child span and calculate duration
            child_span_end_time = time.time()
            child_span_duration = child_span_end_time - child_span_start_time

            print(f"Child Span ID: {child_span.context.trace_id}")  # Same trace_id as root
            print(f"Child Span Name: {child_span.name}")
            print(f"Child Span Attributes: {child_span.attributes}")
            print(f"Child Span Events: {child_span.events}")
            print(f"Child Span Duration: {child_span_duration:.4f} seconds")
            
            # Simulate events in the child span
            for i in range(3):
                child_span.add_event(f"child-span-event-{i}")

# Run the demonstration
if __name__ == "__main__":
    print("Demonstrating OpenTelemetry SDK (with span duration recording):")
    simulate_tracing_api()
    print("Trace recorded and exported via SDK!")
