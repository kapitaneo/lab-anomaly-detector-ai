# Lab Anomaly Detector AI

AI-powered agent for analyzing laboratory data (PCR / ELISA-like workflows).

---

## Overview

This project demonstrates a hybrid AI system that combines deterministic validation logic with LLM-based reasoning to analyze structured laboratory data and detect non-trivial anomalies.

The goal is to show how modern AI systems can be integrated into real-world, domain-specific workflows where pure rule-based logic is insufficient.

---

## Problem

Laboratory systems typically rely on strict validation rules:

* Threshold checks
* Basic data validation
* Predefined assay logic

However, real-world data often contains edge cases that are difficult to capture with deterministic rules alone:

* Borderline values near thresholds
* Inconsistent results across samples
* Outliers within a batch
* Irregular signal patterns

---

## Solution

This project implements a **hybrid validation system**:

```
Structured Data → Validation Tools → LLM Agent → Interpretation
```

### Key Idea

* **Tools (deterministic layer)** ensure correctness
* **LLM (reasoning layer)** handles ambiguity and interpretation

---

## Features

* Agent-based architecture with tool calling
* Multi-step reasoning workflow
* Hybrid system (rules + AI)
* Structured output (JSON)

### Supported anomaly detection:

* Borderline results
* Replicate inconsistencies
* Outliers
* Suspicious patterns

---

## Architecture

```
User Input
   ↓
LLM Agent
   ↓
Tool Selection (Function Calling)
   ↓
Validation Tools
   ↓
LLM Reasoning
   ↓
Structured Output
```

---

## Example Output

```json
{
  "anomalies": [
    {
      "id": "A3",
      "issue": "Outlier detected",
      "value": 3.9
    }
  ],
  "summary": "Sample A3 shows abnormal deviation compared to other values.",
  "confidence": 0.92
}
```

---

## Tech Stack

* Python
* OpenAI Responses API
* Tool Calling / Function Calling
* JSON-based structured outputs

---

## Setup

```bash
git clone https://github.com/your-username/lab-anomaly-detector-ai.git
cd lab-anomaly-detector-ai

python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows
# or
source .venv/bin/activate     # macOS/Linux

pip install -r requirements.txt
```

---

## Environment

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## Run

```bash
python main.py
```

---

## Why Hybrid Approach?

Pure LLM-based systems are:

* non-deterministic
* hard to validate
* unreliable for strict domains

Pure rule-based systems:

* lack flexibility
* fail on edge cases

This project demonstrates a **hybrid approach**, combining:

* deterministic validation tools (accuracy)
* LLM reasoning (flexibility and interpretation)

---

## What This Project Demonstrates

* Designing agent-based systems
* Integrating LLMs into domain-specific workflows
* Combining structured data with reasoning models
* Building reliable AI systems beyond simple prompting

---

## Future Improvements

* Confidence calibration based on validation results
* Support for time-series analysis
* Integration with real data sources
* Multimodal inputs (e.g. signal curves, images)

---

## Notes

This is a proof-of-concept project designed to simulate how AI could be integrated into laboratory workflows without exposing proprietary systems or data.
