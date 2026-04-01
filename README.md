# Lab Anomaly Detector AI

AI-powered agent for analyzing laboratory data (PCR/ELISA-like workflows).

## Overview

This project demonstrates a hybrid AI system combining deterministic validation logic with LLM-based reasoning.

The agent:
- Processes structured lab data
- Applies validation tools (thresholds, borderline detection, outliers)
- Uses LLM reasoning to interpret anomalies
- Generates human-readable explanations

## Architecture

User Input → Agent (LLM) → Tool Calling → Validation → Reasoning → Output

## Features

- Tool-based validation layer
- LLM agent with multi-step reasoning
- Hybrid system (rules + AI)
- Anomaly detection:
  - Threshold violations
  - Borderline cases
  - Outliers

## Tech Stack

- Python
- OpenAI API (Responses API)
- Function Calling (Tool Calling)

## Setup

```bash
git clone <repo>
cd lab-anomaly-detector-ai
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate (Windows)
pip install -r requirements.txt