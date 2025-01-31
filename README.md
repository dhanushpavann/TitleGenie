# TitleGenie.ai 🌟  
**Your AI-Powered YouTube Title Optimization Suite**

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Active-success)](https://titlegenie.live)  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-yellow.svg)](https://python.org)  
[![Django 4.2](https://img.shields.io/badge/Django-4.2-0C4B33)](https://www.djangoproject.com)  
[![OpenAI GPT](https://img.shields.io/badge/OpenAI-GPT_3.5/4-412991)](https://openai.com)

<div align="center">
  <img src="assets/demo-screenshot.png" alt="TitleGenie Interface" width="800">
  <p><em>Generate high-performing YouTube titles in seconds</em></p>
</div>

## Table of Contents 📚
- [Features](#-features)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Architecture](#-architecture)
- [API Documentation](#-api-documentation)
- [Contributing](#-contributing)
- [Roadmap](#-roadmap)
- [FAQ](#-faq)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)

## 🚀 Features

### Core Features
- **AI-Powered Title Generation**  
  GPT-4 powered analysis of video content and context-aware suggestions
- **CTR Optimization Engine**  
  Built-in click-through rate prediction using historical YouTube data patterns
- **Multi-Variant Output**  
  Get 10+ title variations with emoji support and power words
- **Smart Clipboard Integration**  
  One-click copy with success feedback animation

### Technical Features
- **Django Backend**  
  Robust and scalable web framework
- **Responsive Design**  
  Mobile-first approach with CSS Grid/Flexbox
- **Dark/Light Themes**  
  Auto-saved user preference with CSS variables
- **Performance Optimized**  
  Async API calls with loading indicators

## 💻 Installation

### Prerequisites
- Python 3.10+
- OpenAI API key
- PostgreSQL (recommended)

### Setup Guide

```bash
# Clone repository
git clone https://github.com/dhanushpavann/TitleGenie.ai.git
cd TitleGenie.ai

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your credentials