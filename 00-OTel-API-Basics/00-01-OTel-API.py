import requests
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

def call_slow_api():
    url = "http://httpbin.org/delay/2"
    with tracer.start_as_current_span("call_httpbin_delay") as span:
        response = requests.get(url)
        return response.text

def main():
    with tracer.start_as_current_span("main_function_span") as span:
        print("Calling slow API...")
        result = call_slow_api()
        print("Done! Response length:", len(result))

if __name__ == "__main__":
    main()
