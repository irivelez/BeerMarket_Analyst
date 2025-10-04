from crewai import Crew, Process
from agents import (
    create_market_intelligence_researcher,
    create_competitive_analysis_specialist,
    create_financial_analyst,
    create_regional_market_specialist,
    create_opportunity_synthesis_manager
)
from tasks import (
    create_market_research_task,
    create_competitive_analysis_task,
    create_financial_analysis_task,
    create_regional_analysis_task,
    create_synthesis_task
)


def create_latam_beer_market_crew():
    """
    Creates and configures the LATAM Beer Market Research Crew

    Process: Sequential (tasks executed in order)
    Agents: 5 specialized agents
    Tasks: 5 tasks with dependencies
    """

    # Initialize agents
    market_researcher = create_market_intelligence_researcher()
    competitive_analyst = create_competitive_analysis_specialist()
    financial_analyst = create_financial_analyst()
    regional_specialist = create_regional_market_specialist()
    synthesis_manager = create_opportunity_synthesis_manager()

    # Create tasks with context dependencies
    task1_market_research = create_market_research_task(market_researcher)

    task2_competitive_analysis = create_competitive_analysis_task(
        competitive_analyst,
        context=[task1_market_research]
    )

    task3_financial_analysis = create_financial_analysis_task(
        financial_analyst,
        context=[task2_competitive_analysis]
    )

    task4_regional_analysis = create_regional_analysis_task(
        regional_specialist,
        context=[task1_market_research]  # Reduced context - only market data
    )

    task5_synthesis = create_synthesis_task(
        synthesis_manager,
        context=[
            task2_competitive_analysis,  # Reduced context - only most critical tasks
            task3_financial_analysis,
            task4_regional_analysis
        ]
    )

    # Create the crew
    crew = Crew(
        agents=[
            market_researcher,
            competitive_analyst,
            financial_analyst,
            regional_specialist,
            synthesis_manager
        ],
        tasks=[
            task1_market_research,
            task2_competitive_analysis,
            task3_financial_analysis,
            task4_regional_analysis,
            task5_synthesis
        ],
        process=Process.sequential,  # Tasks executed in sequence
        verbose=True
    )

    return crew


def run_market_research():
    """
    Executes the LATAM Beer Market Research crew

    Returns:
        str: Final synthesis report with expansion opportunities
    """
    crew = create_latam_beer_market_crew()

    print("\n" + "="*80)
    print("🍺 LATAM BEER MARKET RESEARCH - MULTI-AGENT ANALYSIS")
    print("="*80)
    print("\nStarting comprehensive market research across 6 LATAM countries...")
    print("Target markets: Brazil, Mexico, Argentina, Colombia, Chile, Peru")
    print("\nThis may take 10-30 minutes depending on API response times.\n")
    print("="*80 + "\n")

    # Execute the crew
    result = crew.kickoff()

    print("\n" + "="*80)
    print("✅ RESEARCH COMPLETED")
    print("="*80 + "\n")

    return result
