from opentelemetry import trace
import uuid

# Function to simulate span context and printing manually
def simulate_tracing_api():
    # Manually generate trace ID (to simulate context)
    trace_id = str(uuid.uuid4())
    
    # Simulate starting a root span
    root_span_name = "root-span"
    root_span_attributes = {"example.attribute": "root-span-attribute"}
    root_span_events = ["root-span-started"]
    
    print(f"Root Span ID: {trace_id}")
    print(f"Root Span Name: {root_span_name}")
    print(f"Root Span Attributes: {root_span_attributes}")
    print(f"Root Span Events: {root_span_events}")
    
    # Simulate starting a child span
    child_span_name = "child-span"
    child_span_attributes = {"example.attribute": "child-span-attribute"}
    child_span_events = ["child-span-started"]
    
    print(f"Child Span ID: {trace_id}")  # Using same trace_id to simulate child span
    print(f"Child Span Name: {child_span_name}")
    print(f"Child Span Attributes: {child_span_attributes}")
    print(f"Child Span Events: {child_span_events}")
    
    # Simulate events in the child span
    for i in range(3):
        print(f"Child Span Event: child-span-event-{i}")

# Run the demonstration
if __name__ == "__main__":
    print("Demonstrating OpenTelemetry API (no SDK):")
    simulate_tracing_api()
    print("Trace recorded via API!")
