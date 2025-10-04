from crewai import Agent, LLM
from crewai_tools import SerperDevTool, WebsiteSearchTool, ScrapeWebsiteTool

# Initialize tools
serper_tool = SerperDevTool()
website_search_tool = WebsiteSearchTool()
scrape_tool = ScrapeWebsiteTool()

# Configure LLM with token limits to prevent rate limit errors
llm = LLM(
    model="gpt-4o-mini",
    temperature=0.7,
    max_tokens=1500  # Limit output tokens per request
)


def create_market_intelligence_researcher():
    """
    Market Intelligence Researcher
    Primary market data collector and pricing analyst for LATAM beer market
    """
    return Agent(
        role="Market Intelligence Researcher",
        goal="Gather LATAM beer market data: size, growth, pricing",
        backstory="""Market analyst specializing in LATAM beverage industry. Expert in market trends and pricing.""",
        tools=[serper_tool, website_search_tool, scrape_tool],
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_competitive_analysis_specialist():
    """
    Competitive Analysis Specialist
    Maps competitor landscape, market share, and value propositions
    """
    return Agent(
        role="Competitive Analysis Specialist",
        goal="Map LATAM beer competitors: key players, market share, positioning",
        backstory="""Competitive intelligence analyst. Expert in competitor strategies and market share analysis.""",
        tools=[serper_tool, website_search_tool, scrape_tool],
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_financial_analyst():
    """
    Financial Analyst
    Extracts and analyzes financial indicators from public sources
    """
    return Agent(
        role="Financial Analyst",
        goal="Extract financial metrics: EBITDA, revenue, margins for beer companies",
        backstory="""Financial analyst. Expert in EBITDA analysis and financial data from public sources.""",
        tools=[serper_tool, scrape_tool],
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_regional_market_specialist():
    """
    Regional Market Specialist
    Provides market-specific insights for different LATAM countries
    """
    return Agent(
        role="Regional Market Specialist",
        goal="Analyze country-specific insights: regulations, distribution, entry barriers",
        backstory="""Regional expert for LATAM markets. Specialist in regulations and market entry.""",
        tools=[serper_tool, website_search_tool, scrape_tool],
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


def create_opportunity_synthesis_manager():
    """
    Opportunity Synthesis Manager
    Synthesizes all findings into actionable expansion opportunities
    """
    return Agent(
        role="Opportunity Synthesis Manager",
        goal="Synthesize research into ranked expansion recommendations",
        backstory="""Strategic consultant. Expert in market entry strategies and opportunity synthesis.""",
        tools=[],  # No external tools, synthesizes from other agents' outputs
        verbose=True,
        allow_delegation=False,
        llm=llm
    )
