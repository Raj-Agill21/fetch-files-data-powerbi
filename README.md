# Autodesk API to Power BI Integration using Python & Microsoft Fabric

A complete workflow to fetch data from Autodesk Construction Cloud (ACC) using Autodesk Platform Services (APS), load it into Microsoft Fabric Lakehouse, and build Power BI dashboards.

## 📁 Folder Structure
C:\APS\Review-files\

├── auth.py ← for OAuth and token storage

├── token_store.json ← generated after login

---

## ✅ Features

- OAuth2 flow with Autodesk API
- ACC review data extraction
- Upload tokens to Fabric Lakehouse
- Scheduled daily refresh via Data Pipeline
- Power BI report based on live Autodesk data

---

## 🛠️ Prerequisites

- Python 3.8+
- Microsoft Fabric Workspace
- Autodesk Developer App
- Power BI Access

Install dependencies:

```bash
pip install requests flask pandas
