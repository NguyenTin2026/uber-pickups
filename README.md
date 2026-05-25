# Uber Pickups Streamlit App

This repository contains a small Streamlit learning project based on the official Uber pickups demo dataset.

## What It Includes

- A Streamlit app that loads Uber pickup data from September 2014.
- A raw data preview.
- A pickup count chart by hour.
- A map visualization of pickup locations.
- A simple multi-page Streamlit navigation example.

## Files

- `uber_pickups.py` - Main Uber pickups demo app.
- `streamlit-docs.py` - Streamlit tutorial examples and navigation setup.
- `main_page.py`, `page_2.py`, `page_3.py` - Example pages for Streamlit navigation.
- `.gitignore` - Excludes local secrets and generated Python files.

## Run Locally

Install the required packages:

```bash
pip install streamlit pandas numpy
```

Run the Uber pickups app:

```bash
streamlit run uber_pickups.py
```

Or run the tutorial/navigation app:

```bash
streamlit run streamlit-docs.py
```

## Notes

The `secrets.toml` file is intentionally ignored and should not be committed to GitHub.
