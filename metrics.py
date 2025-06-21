from prometheus_client import Counter, Histogram, generate_latest
from fastapi import Response

# Define metrics
REQUEST_COUNT = Counter(
    'app_requests_total', 'Total number of requests received', ['endpoint', 'method']
)
ERROR_COUNT = Counter(
    'app_errors_total', 'Total number of errors', ['endpoint']
)
PROCESSING_TIME = Histogram(
    'app_processing_seconds', 'Time spent processing requests', ['endpoint']
)

# Expose /metrics endpoint to Prometheus
def metrics_endpoint():
    return Response(generate_latest(), media_type="text/plain")
