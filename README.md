# 🚀 Naukri Auto Profile Updater

Automatically updates your Naukri profile every day at 9 AM IST using GitHub Actions — completely free, no server needed.

-----

## 📁 Files in This Repo

```
├── naukri_update.py                     # Main Python script
├── requirements.txt                     # Python dependencies
├── .github/
│   └── workflows/
│       └── naukri_update.yml            # GitHub Actions schedule
└── README.md
```

-----

## ⚙️ Setup (One Time — Takes ~10 Minutes)

### Step 1: Create this repo on GitHub

- Go to github.com → New Repository
- Name it: `naukri-auto-update`
- Set to **Private** (keeps your credentials safe)
- Upload all files from this folder

### Step 2: Add your credentials as Secrets

- Go to your repo → **Settings** → **Secrets and variables** → **Actions**
- Click **New repository secret** and add:

|Secret Name      |Value               |
|-----------------|--------------------|
|`NAUKRI_EMAIL`   |your_email@gmail.com|
|`NAUKRI_PASSWORD`|your_naukri_password|

### Step 3: Enable GitHub Actions

- Go to the **Actions** tab in your repo
- Click **“I understand my workflows, go ahead and enable them”**

### Step 4: Test it manually

- Go to **Actions** → **Naukri Daily Profile Update** → **Run workflow**
- Watch it run live — check logs for success ✅

-----

## ⏰ Schedule

Runs automatically every day at **9:00 AM IST**.
To change the time, edit `cron: "30 3 * * *"` in the workflow file.

Common times (UTC):

|IST Time|Cron (UTC)  |
|--------|------------|
|8:00 AM |`30 2 * * *`|
|9:00 AM |`30 3 * * *`|
|10:00 AM|`30 4 * * *`|

-----

## 🔒 Security

- Credentials are stored as **encrypted GitHub Secrets** — never in plain text
- Repo should be set to **Private**

-----

## ❓ Troubleshooting

- **Login failed**: Double-check email/password in Secrets
- **Workflow not running**: Make sure Actions are enabled in repo settings
- **Chrome error**: The workflow auto-installs Chrome — no action needed
