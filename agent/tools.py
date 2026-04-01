def check_threshold(sample):
    return sample["value"] > sample["threshold"]


def detect_borderline(sample):
    diff = abs(sample["value"] - sample["threshold"])
    return diff < 0.2


def detect_outliers(samples):
    values = [s["value"] for s in samples]
    avg = sum(values) / len(values)

    outliers = []
    for s in samples:
        if abs(s["value"] - avg) > 1.5:
            outliers.append(s["id"])

    return outliers