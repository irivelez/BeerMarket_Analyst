# 🍺 LATAM Beer Market Analyst

Multi-agent AI system powered by CrewAI for comprehensive beer market research across Latin America.

## 🎯 Overview

This system uses 5 specialized AI agents to analyze the beer market in 6 LATAM countries (Brazil, Mexico, Argentina, Colombia, Chile, Peru) to identify expansion opportunities.

### Research Scope
- **Market Intelligence**: Market size, growth trends, pricing strategies
- **Competitive Analysis**: Key players, market share, value propositions
- **Financial Analysis**: EBITDA, margins, profitability metrics
- **Regional Insights**: Country-specific regulatory, distribution, and consumer insights
- **Strategic Recommendations**: Ranked expansion opportunities with action plans

## 🤖 AI Agents

1. **Market Intelligence Researcher** - Market data & pricing analysis
2. **Competitive Analysis Specialist** - Competitor mapping & positioning
3. **Financial Analyst** - Financial metrics from public sources
4. **Regional Market Specialist** - Country-specific insights
5. **Opportunity Synthesis Manager** - Strategic recommendations

## 🛠️ Tools Used

- **SerperDevTool** - Google search via Serper API
- **WebsiteSearchTool** - Website content search
- **ScrapeWebsiteTool** - Web page scraping

## 📋 Prerequisites

- Python 3.8+
- OpenAI API key
- Serper API key

## 🚀 Installation

1. Clone or download this repository

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp .env.example .env
```

Edit `.env` and add your API keys:
```
OPENAI_API_KEY=your_openai_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

## 💻 Usage

Run the market research:
```bash
python main.py
```

The process takes 10-30 minutes depending on API response times.

## 📊 Output

The system generates a comprehensive report (`latam_beer_market_report.txt`) containing:

- Executive summary
- Market size and growth analysis
- Pricing landscape
- Competitive positioning
- Financial benchmarks
- Country-by-country insights
- Top expansion opportunities (ranked)
- Strategic recommendations
- Action plan

## 📁 Project Structure

```
BeerMarket_Analyst/
├── agents.py              # Agent definitions
├── tasks.py               # Task definitions
├── crew.py                # Crew configuration
├── main.py                # Main execution script
├── requirements.txt       # Python dependencies
├── .env.example           # Environment template
├── .env                   # Your API keys (not in git)
└── README.md              # This file
```

## 🔑 API Keys

### OpenAI API
Get your key at: https://platform.openai.com/api-keys

### Serper API
Get your key at: https://serper.dev/api-key

## ⚙️ Configuration

The system uses:
- **Process**: Sequential (tasks run in order)
- **LLM**: OpenAI GPT models (configurable)
- **Tools**: CrewAI built-in tools only

## 🎓 Target Markets

- 🇧🇷 Brazil
- 🇲🇽 Mexico
- 🇦🇷 Argentina
- 🇨🇴 Colombia
- 🇨🇱 Chile
- 🇵🇪 Peru

## 📝 Notes

- All data is sourced from publicly available information
- Financial data prioritizes trusted sources (Yahoo Finance, Bloomberg, company IR sites)
- The system does not use custom tools or PDF parsing
- Results depend on data availability and API quality

## 🔍 Troubleshooting

**Missing API keys**: Ensure `.env` file is properly configured

**API errors**: Check API key validity and credits

**Slow execution**: Normal for comprehensive research (10-30 min)

**No results**: Verify internet connection and API access

## 📄 License

This project is for educational and research purposes.
