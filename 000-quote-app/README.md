# Background:

✅ Proposed App: “Quote Service”
💡 What It Does:
A simple Quote Service API that:

Stores motivational quotes in a SQLite (or Postgres) database

Provides an endpoint to retrieve a random quote

Supports adding a new quote (POST request)

🔗 App Architecture (2 services):
lua
Copy
Edit
+-------------+      HTTP       +-------------+      DB Query      +-----------+
| Python App  |  <--------->   | Java App    |  <------------->   |  Database |
| (Frontend)  |                | (Backend)   |                    |  (SQLite) |
+-------------+                +-------------+                    +-----------+
Python App (Flask): Acts as the frontend API. It calls the Java service to get/store quotes.

Java App (Spring Boot): Acts as the backend, connects to a SQLite/Postgres DB.

Database: Stores quotes in a single quotes table.

🔍 Why this app is perfect for OpenTelemetry Certified Associate (OTCA):
Topic	Where You’ll Teach It
Manual instrumentation	Start with basic span creation in both apps
Auto-instrumentation	Use Java Agent, opentelemetry-instrument
API vs SDK	Separate API call and SDK behavior in Python
Context propagation	Trace across Python → Java → DB
Metrics	Add request count, DB query latency
Logs	Add structured logs with correlation IDs
Collector Export	Export via OTLP to Jaeger or Prometheus
Semantic conventions	Label spans with HTTP/db conventions
🔨 Features You Can Incrementally Add:
Phase 1: Basic HTTP spans

Manual spans around HTTP calls in Python

Auto-instrumentation for Java

Phase 2: Context propagation (traceId)

Pass trace context across services

Phase 3: DB instrumentation

Use JDBC or ORM tracing in Java

Phase 4: Metrics + Logs

Add basic metrics (request count, DB latency)

Add logs with trace/span context

Phase 5: Export + Collector

Export all data to an OpenTelemetry Collector

Visualize in Jaeger, Prometheus/Grafana, or console

🧪 Tech Stack (simple, lightweight)
Python (Flask)

Java (Spring Boot) or even plain Java + Javalin

SQLite (or PostgreSQL) — simple, file-based or easily containerized

Docker Compose (optional for scaling demo)





# Basics

## Get Flask

PS C:\Data\OTel\kk-otca\000-quote-app> python .\00-python-app.py
Traceback (most recent call last):
  File "C:\Data\OTel\kk-otca\000-quote-app\00-python-app.py", line 3, in <module>
    from flask import Flask, jsonify, request
ModuleNotFoundError: No module named 'flask'


PS C:\Data\OTel\kk-otca\000-quote-app> pip install flask
Defaulting to user installation because normal site-packages is not writeable
Collecting flask
  Downloading flask-3.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting Werkzeug>=3.1 (from flask)
  Downloading werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting Jinja2>=3.1.2 (from flask)
  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting itsdangerous>=2.2 (from flask)
  Downloading itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting click>=8.1.3 (from flask)
  Downloading click-8.1.8-py3-none-any.whl.metadata (2.3 kB)
Collecting blinker>=1.9 (from flask)
  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting colorama (from click>=8.1.3->flask)
  Downloading colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting MarkupSafe>=2.0 (from Jinja2>=3.1.2->flask)
  Downloading MarkupSafe-3.0.2-cp313-cp313-win_amd64.whl.metadata (4.1 kB)
Downloading flask-3.1.0-py3-none-any.whl (102 kB)
Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Downloading click-8.1.8-py3-none-any.whl (98 kB)
Downloading itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading werkzeug-3.1.3-py3-none-any.whl (224 kB)
Downloading MarkupSafe-3.0.2-cp313-cp313-win_amd64.whl (15 kB)
Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Installing collected packages: MarkupSafe, itsdangerous, colorama, blinker, Werkzeug, Jinja2, click, flask
  WARNING: The script flask.exe is installed in 'C:\Users\amrit\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed Jinja2-3.1.6 MarkupSafe-3.0.2 Werkzeug-3.1.3 blinker-1.9.0 click-8.1.8 colorama-0.4.6 flask-3.1.0 itsdangerous-2.2.0

[notice] A new release of pip is available: 24.3.1 -> 25.0.1
[notice] To update, run: C:\Users\amrit\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip
PS C:\Data\OTel\kk-otca\000-quote-app> 



# JAVA

## Install OpenJDK

## Install Maven



## Run maven commands

mvn exec:java

## POST the Quote into the Application


curl.exe -X POST http://localhost:8080/quote -H "Content-Type: application/json" -d '{\"quote\": \"The only way out is through.\"}'



## GET the quote from the application


curl http://localhost:8080/quote



 mvn -f .\pom.xml clean package