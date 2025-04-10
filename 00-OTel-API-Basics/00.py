import requests
#from opentelemetry import trace
#from opentelemetry.trace import SpanKind
#from opentelemetry.trace import get_tracer_provider, set_tracer_provider
#from opentelemetry.sdk.trace import TracerProvider

# Setup a basic tracer provider (to enable in-process span creation)
# Note: No exporter is configured, so spans won't be sent anywhere yet
tracer_provider = TracerProvider()
set_tracer_provider(tracer_provider)

tracer = trace.get_tracer(__name__)

def call_slow_api():
    with tracer.start_as_current_span("call_httpbin_delay", kind=SpanKind.CLIENT) as span:
        url = "http://httpbin.org/delay/2"
        response = requests.get(url)
        span.set_attribute("http.url", url)
        span.set_attribute("http.status_code", response.status_code)
        return response.text

def main():
    print("Calling slow API...")
    result = call_slow_api()
    print("Done! Response length:", len(result))

if __name__ == "__main__":
    main()
