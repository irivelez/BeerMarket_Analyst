from crewai import Task


def create_market_research_task(agent):
    """
    Task 1: Market Landscape & Pricing Research
    Comprehensive LATAM beer market overview including pricing
    """
    return Task(
        description="""Research LATAM beer market for Brazil, Mexico, Argentina, Colombia, Chile, Peru:
        1. Market size (USD billions), growth rates (CAGR 2023-2025), segments (premium/mainstream/economy/craft)
        2. Pricing: average prices by segment per country, key pricing strategies
        3. Top 3 trends (consumer preferences, craft beer, premiumization)

        Be concise. Focus on numbers and key insights only.""",
        expected_output="""CONCISE report (max 800 words):
        - Market size table (6 countries x size/growth/segments)
        - Pricing table (segment x country with avg prices)
        - 3 key trends with bullet points

        Keep it brief, data-focused, no verbose explanations.""",
        agent=agent
    )


def create_competitive_analysis_task(agent, context):
    """
    Task 2: Competitor Mapping
    Map competitive landscape and market share
    """
    return Task(
        description="""Identify top 5-7 beer companies in LATAM (AB InBev, Heineken, etc.):
        1. Market share % by country (top 3 players per country)
        2. Key brands and positioning (premium/mainstream/economy)
        3. Main differentiation factors

        Be concise. Extract from prior context where possible.""",
        expected_output="""CONCISE report (max 600 words):
        - Top players table (company, market share by country)
        - Brand positioning matrix (company x segment)
        - 2-3 key competitive gaps

        Brief bullets only. No lengthy descriptions.""",
        agent=agent,
        context=context
    )


def create_financial_analysis_task(agent, context):
    """
    Task 3: Financial Performance Analysis
    Extract key financial metrics from public sources
    """
    return Task(
        description="""Get financials for top 5 companies from prior context (AB InBev, Heineken, etc.):
        1. EBITDA margin %, revenue (latest year)
        2. YoY growth rate
        3. LATAM revenue % if available

        Use Yahoo Finance, company IR sites. Be concise.""",
        expected_output="""CONCISE report (max 500 words):
        - Financial table (company, EBITDA margin, revenue, growth rate)
        - 2-3 key insights on profitability

        Data table format. Minimal text.""",
        agent=agent,
        context=context
    )


def create_regional_analysis_task(agent, context):
    """
    Task 4: Regional Deep Dive
    Country-specific insights for LATAM markets
    """
    return Task(
        description="""Analyze top 3 LATAM countries (pick from: Brazil, Mexico, Argentina, Colombia, Chile, Peru):
        1. Key regulations (alcohol taxes, import restrictions)
        2. Distribution channels (retail/on-premise dominance)
        3. Top 2 entry barriers per country

        Focus on actionable insights only.""",
        expected_output="""CONCISE report (max 600 words):
        - Country comparison table (regulations, distribution, barriers)
        - Market attractiveness ranking (1-3)

        Bullet points only. No lengthy paragraphs.""",
        agent=agent,
        context=context
    )


def create_synthesis_task(agent, context):
    """
    Task 5: Opportunity Synthesis
    Executive report with expansion recommendations
    """
    return Task(
        description="""Synthesize prior research into expansion recommendations:
        1. Rank top 3 countries (score: market size, growth, competition, barriers)
        2. Best segment opportunities (premium/craft/mainstream)
        3. Top 3 strategic recommendations
        4. Expected EBITDA margins

        Use only context from previous tasks. No new research.""",
        expected_output="""EXECUTIVE REPORT (max 800 words):

        1. COUNTRY RANKING (table with scores)
        2. SEGMENT OPPORTUNITIES (top 2-3 segments)
        3. TOP 3 RECOMMENDATIONS (ranked, with rationale)
        4. FINANCIAL OUTLOOK (expected margins)
        5. NEXT STEPS (3-5 action items)

        Concise bullet points. Data-driven. No fluff.""",
        agent=agent,
        context=context
    )
