# 🚀 Assignment 3 — Hybrid Auto-Scaling: Local VM → Google Cloud Platform

## 📌 Project Overview

This project demonstrates a **hybrid cloud auto-scaling architecture** where a **local virtual machine (VirtualBox)** continuously monitors system resource usage and automatically provisions infrastructure on **Google Cloud Platform (GCP)** when utilization exceeds a defined threshold.

The implementation simulates a real-world **cloud bursting** scenario commonly used in enterprise systems to extend local capacity dynamically into public cloud infrastructure.

---

## 🎯 Objective

Build a system that:

✔ Creates and runs a Local VM
✔ Monitors CPU and Memory usage continuously
✔ Detects resource usage above **75%**
✔ Automatically triggers provisioning of a Cloud VM on GCP
✔ Deploys a sample application for demonstration

---

## 🧱 High-Level Architecture

```
┌─────────────────────────────┐
│      Local Virtual Machine  │
│  (VirtualBox – Ubuntu)      │
│                             │
│  • Sample Application       │
│  • Monitoring Script        │
└──────────────┬──────────────┘
               │
               │ CPU / RAM > 75%
               ▼
┌─────────────────────────────┐
│   Auto-Scaling Trigger      │
│   (Bash + gcloud CLI)       │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Google Cloud Platform (GCP) │
│ Compute Engine              │
│ • Auto-created VM Instance  │
└─────────────────────────────┘
```

---

## 🧠 Architecture Concept

This implementation follows the **Cloud Bursting Model**:

* Local infrastructure handles normal workloads.
* When utilization crosses threshold, workloads are extended to cloud resources.
* Scaling logic is automated using scripting and cloud APIs.

This approach reflects modern hybrid infrastructure used in production environments.

---

## 🛠️ Technology Stack

| Layer          | Technology            |
| -------------- | --------------------- |
| Virtualization | Oracle VirtualBox     |
| OS             | Ubuntu 24.04 LTS      |
| Monitoring     | Python + psutil       |
| Automation     | Bash scripting        |
| Cloud Provider | Google Cloud Platform |
| Cloud Service  | Compute Engine        |
| CLI Tool       | gcloud SDK            |

---

## 📂 Repository Structure

```
Assignment3-AutoScaling/
│
├── monitoring/
│   └── monitor.py            # Resource monitoring logic
│
├── cloud/
│   └── scale_to_cloud.sh     # GCP VM provisioning script
│
├── app/
│   └── service.py            # Sample application
│
├── architecture/
│   └── architecture_diagram.png
│
├── docs/
│   └── report.pdf
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Implementation Steps

### 1️⃣ Local VM Setup

Create Ubuntu VM using VirtualBox.

Login as username - ubuntu password - ubuntu

<img width="1637" height="977" alt="image" src="https://github.com/user-attachments/assets/4dee6853-96bf-498d-a276-6bfef052d970" />



Install dependencies:

```bash
sudo apt update
sudo apt install python3 python3-psutil stress -y
```

---

### 2️⃣ Google Cloud Authentication

Authenticate using Service Account:

```bash
gcloud auth activate-service-account --key-file=autoscale-key.json
gcloud config set project Assignment2g25ai1052
```

---

### 3️⃣ Start Monitoring

```bash
cd monitoring
python3 monitor.py
```

The script continuously checks:

* CPU Utilization
* Memory Utilization

Threshold:

```
75%
```

---

### 4️⃣ Simulate High Load

Open another terminal:

```bash
stress --cpu 4 --timeout 60
```

---

### 5️⃣ Auto-Scaling Trigger

When threshold exceeds:

```
Threshold exceeded — scaling to cloud...
```

Script executes:

```
cloud/scale_to_cloud.sh
```

---

### 6️⃣ Cloud VM Provisioning

GCP instance is created automatically using:

```bash
gcloud compute instances create autoscale-vm \
  --zone=asia-south1-c \
  --machine-type=e2-medium \
  --image-family=ubuntu-2204-lts \
  --image-project=ubuntu-os-cloud
```

---

## 🧪 Expected Output

### Local VM Console

```
CPU: 78% | RAM: 30%
Threshold exceeded — scaling to cloud...
```

### GCP Console

```
autoscale-vm   → RUNNING
```

---

## 📊 Key Engineering Concepts Demonstrated

* Hybrid Cloud Architecture
* Automated Infrastructure Provisioning (IaC-style)
* Resource Monitoring & Threshold-based Scaling
* Cloud API Automation
* Infrastructure Resilience Strategy

---

## 🎥 Demo Video

Video walkthrough showing:

* Local VM monitoring
* CPU stress generation
* Auto scaling trigger
* Cloud VM creation

```
<PASTE VIDEO LINK HERE>
```

---

## 📄 Plagiarism Declaration

This implementation, scripts, architecture, and documentation are original work developed specifically for academic submission. External technologies are used strictly for implementation purposes.

---

## 👨‍💻 Author

Ved Prakash
Cloud & Automation Implementation — Assignment 3

---
