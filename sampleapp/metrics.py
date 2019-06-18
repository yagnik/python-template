"""
module to handle app level metrics.

wrapper around prometheus metrics library
"""

from prometheus_client import Counter, Gauge, Summary

METRICS = {
    "request_processing_seconds": Summary(
        "request_processing_seconds", "Time spent processing request"
    ).time,
    "request_in_progress": Gauge(
        "request_in_progress", "In progress requests"
    ).track_inprogress,
    "failed_requests": Counter("failed_requests", "Failed requests").count_exceptions,
}
