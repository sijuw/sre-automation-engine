# 🚨 SRE Automation Engine

An event-driven Incident Automation Platform built with **Python** and **FastAPI** that automates the early stages of incident response.

The engine receives alerts from Grafana, stores them, sends interactive Slack notifications for approval, creates Jira incidents on demand, and keeps Slack and Jira synchronized throughout the incident lifecycle.

---

# Project Overview

In many organizations, SREs manually perform the same repetitive tasks whenever an alert fires:

- Review the monitoring alert
- Create a Jira Incident
- Notify engineers
- Open dashboards
- Start investigations
- Update stakeholders

This project automates those repetitive workflows while keeping a human approval step before creating incidents.

---

# Architecture

```text
                   Grafana Alert
                         │
                         ▼
                 FastAPI Webhook
                         │
                         ▼
                    SQLite Database
                         │
                         ▼
              Interactive Slack Message
                         │
         ┌───────────────┼───────────────┐
         ▼               ▼               ▼
   Create Jira    Create Jira + Meet    Ignore
         │               │               │
         ▼               ▼               ▼
      Jira API      (Upcoming)       Update Status
         │
         ▼
   Update Slack Message
```

---

# Features

## ✅ Alert Ingestion

- Receives Grafana alerts via Webhooks
- Validates payloads using Pydantic
- Structured logging
- Error handling

---

## ✅ Alert Persistence

Alerts are stored using SQLAlchemy.

Stored information includes:

- Alert Title
- Status
- Message
- Dashboard URL
- Jira Ticket
- Incident Status
- Acknowledged By
- Timestamp

---

## ✅ Slack Integration

Interactive Slack notifications are automatically sent whenever an alert is received.

Example:

```
🚨 Production Alert

Title:
Payment API Down

Status:
Critical

Buttons

[Create Jira]

[Create Jira + Meet]

[Ignore]
```

---

## ✅ Jira Integration

When an engineer approves the alert:

- Creates a Jira Incident
- Stores the Jira Ticket Number
- Updates the database
- Updates the Slack message

---

## ✅ Incident State Tracking

The engine tracks the incident lifecycle.

```
NEW

↓

SLACK_SENT

↓

JIRA_CREATED

↓

IGNORED

↓

RESOLVED
```

---

## ✅ Repository Pattern

Business logic is separated into:

```
API

↓

Services

↓

Repositories

↓

Clients

↓

Database
```

Making the application modular and easy to extend.

---

# Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| FastAPI | REST API |
| SQLAlchemy | ORM |
| SQLite | Database |
| Slack API | Notifications |
| Jira REST API | Incident Management |
| Grafana | Alert Source |
| HTTPX | API Client |
| Pydantic | Validation |

---

# Project Structure

```
app/
│
├── api/
│
├── clients/
│   ├── jira_client.py
│   └── slack_client.py
│
├── services/
│
├── repositories/
│
├── database/
│
├── schemas/
│
└── core/
```

---

# Current Workflow

```
Grafana Alert

↓

Webhook

↓

Save Alert

↓

Send Slack Message

↓

Engineer Clicks Button

↓

Create Jira

↓

Update Database

↓

Update Slack
```

---

# Planned Features

- Kubernetes Diagnostics
- Prometheus Metrics Collection
- Splunk Log Analysis
- Google Meet Integration
- Automatic Jira Comments
- Incident Timeline
- AI-generated Incident Summary
- AI-generated Root Cause Analysis
- Automated Runbook Suggestions
- Slack Thread Updates
- ServiceNow Integration
- Microsoft Teams Integration

---

# Running the Project

## Clone

```bash
git clone https://github.com/YOUR_USERNAME/sre-automation-engine.git
```

## Install

```bash
pip install -r requirements.txt
```

## Configure

Create a `.env`

```
JIRA_URL=

JIRA_EMAIL=

JIRA_API_TOKEN=

JIRA_PROJECT_KEY=

SLACK_BOT_TOKEN=

SLACK_CHANNEL_ID=
```

## Run

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

---

# Example Incident Flow

```
Grafana detects high latency

↓

Webhook received

↓

Alert stored in SQLite

↓

Slack notification sent

↓

Engineer clicks Create Jira

↓

Jira Incident created

↓

Slack message updated

↓

Incident investigation begins
```

---

# Future Vision

The goal is to evolve this project into a complete SRE Automation Platform capable of:

- Automated Diagnostics
- Intelligent Incident Correlation
- Automatic Root Cause Analysis
- Self-healing Actions
- AI-assisted Incident Response

---

# Why I Built This

As a Senior Application Support Engineer, I wanted to reduce the repetitive operational tasks performed during incident response.

This project demonstrates practical backend engineering, workflow automation, REST API integrations, observability tooling, and modern SRE practices.

---

# Author

**Saheed Yusuf**
Senior Application Support Engineer

