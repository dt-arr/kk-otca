from opentelemetry import trace

# Acquire a tracer from the API
tracer = trace.get_tracer("otel-api-demo")

# Function to demonstrate spans with the API
def simulate_tracing_api():
    # Start a root span
    with tracer.start_as_current_span("root-span") as root_span:
        root_span.set_attribute("example.attribute", "root-span-attribute")
        root_span.add_event("root-span-started")
        
        # Start a child span
        with tracer.start_as_current_span("child-span") as child_span:
            child_span.set_attribute("example.attribute", "child-span-attribute")
            child_span.add_event("child-span-started")
            
            # Simulate some work in the child span
            for i in range(3):
                child_span.add_event(f"child-span-event-{i}")
        
        # End child span and log root span ending
        root_span.add_event("root-span-ending")

# Run the demonstration
if __name__ == "__main__":
    print("Demonstrating OpenTelemetry API (no SDK):")
    simulate_tracing_api()
    print("Trace recorded via API!")
