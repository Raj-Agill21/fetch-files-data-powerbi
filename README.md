# Autodesk API to Power BI Integration using Python & Microsoft Fabric
<img width="3840" height="2280" alt="Screenshot 2025-08-01 103700" src="https://github.com/user-attachments/assets/4a4c9c5e-202d-4590-8827-68c51d596528" />


A complete workflow to fetch data from Autodesk Construction Cloud (ACC) using Autodesk Platform Services (APS), load it into Microsoft Fabric Lakehouse, and build Power BI dashboards.

## 📁 Folder Structure

```
your-project-folder/
├── auth.py              # Handles OAuth authentication
├── token_store.json     # Token file generated after login
```

## ✅ Features

- OAuth2 flow with Autodesk API
- ACC review data extraction
- Upload tokens to Fabric Lakehouse
- Scheduled daily refresh via Data Pipeline
- Power BI report based on live Autodesk data

## 🛠️ Prerequisites

- Python 3.8+
- Microsoft Fabric Workspace
- Autodesk Developer App
- Power BI Access

Install dependencies:

```bash
pip install requests flask pandas
```

## 🔐 1. Set Up Autodesk API App

- Go to: https://aps.autodesk.com/
- Create an app and note:
  - `client_id`
  - `client_secret`
- Set Redirect URI: `http://localhost:3000/callback`
- Required Scopes:  
  `data:read`, `data:write`, `bucket:read`, `viewables:read`

## 🔌2. Custom Integration in ACC

1. Go to **ACC → ACC Admin → Custom Integrations**
2. Register your APS App using the `client_id`

## 🔑 3. Authentication Script

Create `auth.py` and insert the following:

```python
# auth.py
# [Insert full authentication code here]
```

Run it:

```bash
python auth.py
```

- Browser opens → Login → Token saved in `token_store.json`

## 📤 4. Upload Token to Fabric

- Go to Fabric Workspace → Lakehouse
- Create folder: `Files/auth/`
- Upload `token_store.json` there

## 📓 5. Create Fabric Notebook

- In Fabric, create a Notebook
- Paste the Python code to:
  - Refresh token
  - Run
  - It Save as `acc_reviews_daily` table

## ⏱ 6. Automate with Data Pipeline

- Go to workspace → `+ New > Data Pipeline`
- Drag your notebook
- Add Trigger → Schedule → Daily
- Save & Publish

## 📈 7. Build Power BI Report

- Go to workspace → `+ New > Power BI Report`
- Choose Lakehouse as source
- Select `acc_reviews_daily` table
- Build and save your dashboard

## 📚 Resources

- [Autodesk Platform Services](https://aps.autodesk.com/)

## 👨‍💻 Author

- Name: `Raj Agill P K`

---

