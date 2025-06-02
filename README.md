# Customer Journey Analytics Dashboard

An interactive data analytics project that analyzes and visualizes customer behavior throughout their e-commerce journey — from product views to purchases.

## Project Overview

This dashboard provides:
- Funnel stage analysis (View → Cart → Purchase)
- Conversion rates and drop-off insights
- Key session metrics
- Interactive visualization using Streamlit & Plotly

## Dataset

- Source: [E-Commerce Behavior Dataset (Kaggle)](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)
- Size: 9GB of raw logs including `event_type`, `user_id`, `user_session`, and timestamps

## Tech Stack

| Area                 | Technology                            |
|----------------------|----------------------------------------|
| Data Processing      | Python, Pandas                         |
| Feature Engineering  | Session-level funnel tagging           |
| Visualization        | Streamlit, Plotly                      |
| Dataset              | CSV files (Kaggle e-commerce logs)     |
| Version Control      | Git, GitHub                            |

## Key Features

- Session-level funnel segmentation: **Viewed Only → Carted → Purchased**
- Conversion rate KPIs and session metrics
- Interactive funnel charts for behavior exploration
- Clean modular code with notebooks and scripts

## How to Run

1. Clone the repo
2. Install dependencies:
