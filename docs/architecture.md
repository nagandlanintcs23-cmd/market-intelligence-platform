# System Architecture – Market Intelligence Platform

## Overview
The Market Intelligence Platform is a modular system designed to compress large market reports, analyze competitor data, and generate strategic business insights at low computational cost.

The architecture follows a simple layered pipeline:

Input → Processing → Analysis → Insight Generation → Output

---

## Components

### 1. Data Input Layer
Sources:
- Market reports (text files or pasted text)
- Competitor data (manual or JSON input)

Purpose:
Collect raw business data for processing.

---

### 2. Compression Layer (src/compressor.py)
Responsibility:
- Reduces large market reports into short summaries
- Removes redundant information
- Prepares text for analysis

---

### 3. Analysis Layer (src/analyzer.py)
Responsibility:
- Extracts competitor strengths
- Compares multiple competitors
- Generates structured competitive insights

---

### 4. Insight Engine (src/insight_engine.py)
Responsibility:
- Combines compressed market data with competitor analysis
- Produces strategic recommendations

---

### 5. Application Layer (app.py)
Responsibility:
- User interaction
- Orchestrates all modules
- Displays final strategy output

---

## Architecture Diagram (Text)

Market Report
      ↓
Compressor
      ↓
Compressed Summary
      ↓
Analyzer ← Competitor Data
      ↓
Insight Engine
      ↓
Strategic Output
