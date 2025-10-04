# 🍺 LATAM Beer Market Analyst

**Multi-agent AI system for strategic beer market research across Latin America**

---

**⏱️ Build time:** ~2 hours
**🤖 Built with:** CrewAI multi-agent framework
**🎯 Purpose:** Market research automation for business expansion analysis

---

## What It Does

This system deploys 5 specialized AI agents to conduct comprehensive market research on the beer industry across 6 Latin American countries. It autonomously gathers data, analyzes competition, extracts financial metrics, and synthesizes strategic recommendations for market entry.

**Key outputs:**
- Market sizing and growth forecasts
- Competitive landscape with market share estimates
- Financial benchmarks (EBITDA, margins, profitability)
- Country-specific entry barriers and opportunities
- Ranked expansion recommendations with action plans

---

## Tech Stack

- **CrewAI 0.201.1** - Multi-agent orchestration framework
- **OpenAI GPT-4o-mini** - Language model (token-optimized)
- **Serper API** - Web search capabilities
- **CrewAI Tools** - SerperDevTool, WebsiteSearchTool, ScrapeWebsiteTool

---

## Quick Start

### Prerequisites

- Python 3.11+
- OpenAI API key ([get one here](https://platform.openai.com/api-keys))
- Serper API key ([get one here](https://serper.dev/api-key))

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/irivelez/BeerMarket_Analyst.git
cd BeerMarket_Analyst
```

2. **Create virtual environment and install dependencies**
```bash
# Using uv (recommended)
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt

# Or using standard venv
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3. **Configure API keys**
```bash
cp .env.example .env
```

Edit `.env` and add your keys:
```
OPENAI_API_KEY=your_openai_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

4. **Run the analysis**
```bash
python main.py
```

Expected runtime: **5-15 minutes**

---

## How It Works

### The Crew

5 specialized AI agents work sequentially to research the market:

1. **Market Intelligence Researcher** - Gathers market size, growth rates, pricing data
2. **Competitive Analysis Specialist** - Maps competitors, market share, brand positioning
3. **Financial Analyst** - Extracts EBITDA, margins, profitability from public sources
4. **Regional Market Specialist** - Analyzes regulations, distribution, entry barriers by country
5. **Opportunity Synthesis Manager** - Synthesizes findings into strategic recommendations

### Research Coverage

**Target Markets:**
- 🇧🇷 Brazil
- 🇲🇽 Mexico
- 🇦🇷 Argentina

**Analysis Areas:**
- Market size and growth trends
- Pricing strategies by segment (premium, mainstream, economy, craft)
- Competitive landscape and market share
- Financial performance of key players
- Regulatory environment and distribution channels
- Strategic expansion opportunities

---

## Output

The system generates `latam_beer_market_report.txt` containing:

1. **Market Overview** - Size, growth, pricing by country
2. **Competitive Analysis** - Top players, market share, positioning
3. **Financial Benchmarks** - EBITDA margins, profitability metrics
4. **Regional Insights** - Country comparison with entry barriers
5. **Strategic Recommendations** - Ranked expansion opportunities
6. **Action Plan** - Next steps for market entry

---

## Why This Exists

Traditional market research is time-consuming and expensive. This project demonstrates how multi-agent AI systems can automate the initial research phase, providing:

- **Speed**: 15 minutes vs weeks of manual research
- **Cost**: Just API Costs
- **Comprehensiveness**: Parallel analysis across multiple dimensions
- **Objectivity**: Data-driven insights from public sources

---

## Features

✅ **Token-optimized** - Designed to work within OpenAI rate limits
✅ **Configurable** - Easy to adjust countries, segments, or focus areas
✅ **Sequential workflow** - Tasks build on each other for coherent analysis
✅ **Public data only** - No proprietary databases required
✅ **Automated synthesis** - Combines multiple data sources into actionable insights

---

## Limitations

- **Data recency** - Limited to publicly available online information
- **Accuracy** - Estimates may vary; should be validated with primary research
- **Scope** - Focuses on top 3 countries (configurable to all 6)
- **API costs** - Requires active OpenAI and Serper subscriptions
- **Language** - Primarily searches English-language sources

> **Note:** This tool is for initial research and opportunity identification. Always validate findings with on-the-ground market research before major investment decisions.

---

⚡️ Built in 2 hours • Part of thexperiment.dev
