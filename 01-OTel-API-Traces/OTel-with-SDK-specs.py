from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider, SpanProcessor
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.trace import Status, StatusCode
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
    # Simulate starting a root span
    with tracer.start_as_current_span("root-span") as root_span:
        # Set attributes for the root span
        root_span.set_attribute("service.version", "1.0")
        root_span.set_attribute("request.method", "GET")
        
        # Add events to the root span
        root_span.add_event("root-span-started", {"detail": "Starting processing"})
        
        # Simulate work done in root span
        time.sleep(1)  # Simulating 1 second of work
        
        # Set status for the root span
        root_span.set_status(Status(StatusCode.OK, "Root span completed successfully"))

        # Simulate a child span
        with tracer.start_as_current_span("child-span", links=[root_span]) as child_span:
            # Set attributes for the child span
            child_span.set_attribute("component", "HTTP Client")
            child_span.set_attribute("request.url", "https://api.example.com")
            
            # Add events to the child span
            child_span.add_event("child-span-started", {"detail": "Sending request to API"})
            
            # Simulate work done in child span
            time.sleep(0.5)  # Simulating 0.5 seconds of work

            # Set status for the child span
            child_span.set_status(Status(StatusCode.ERROR, "Failed to connect"))

            # Simulate events in the child span
            for i in range(3):
                child_span.add_event(f"child-span-event-{i}", {"info": f"Event #{i}"})

            # Simulate a link between spans
            child_span.add_link(root_span.context, {"info": "Linking to root-span"})

        # End of root span
        print(f"Root Span ID: {root_span.context.trace_id}")
        print(f"Child Span ID: {child_span.context.trace_id}")
        print(f"Root Span Attributes: {root_span.attributes}")
        print(f"Child Span Attributes: {child_span.attributes}")
        print(f"Root Span Status: {root_span.status}")
        print(f"Child Span Status: {child_span.status}")
        print(f"Root Span Events: {root_span.events}")
        print(f"Child Span Events: {child_span.events}")
        print(f"Child Span Links: {child_span.links}")

# Run the demonstration
if __name__ == "__main__":
    print("Demonstrating OpenTelemetry SDK (with full specifications):")
    simulate_tracing_api()
    print("Trace recorded and exported via SDK!")
