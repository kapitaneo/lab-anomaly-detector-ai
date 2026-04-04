def check_threshold(value, threshold):
    return value > threshold


def detect_borderline(value, threshold):
    return abs(value - threshold) < 0.2


def detect_outliers(values):
    avg = sum(values) / len(values)
    return [v for v in values if abs(v - avg) > 1.5]


TOOL_REGISTRY = {
    "check_threshold": check_threshold,
    "detect_borderline": detect_borderline,
    "detect_outliers": detect_outliers,
}