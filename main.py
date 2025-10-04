#!/usr/bin/env python3
"""
LATAM Beer Market Research - Multi-Agent System
Powered by CrewAI

This script orchestrates 5 specialized AI agents to conduct comprehensive
market research on the beer industry across 6 Latin American countries.

Required Environment Variables:
- OPENAI_API_KEY: OpenAI API key for LLM
- SERPER_API_KEY: Serper API key for web search
"""

import os
from dotenv import load_dotenv
from crew import run_market_research


def check_environment():
    """Verify required environment variables are set"""
    load_dotenv()

    required_vars = ["OPENAI_API_KEY", "SERPER_API_KEY"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        print("❌ Error: Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nPlease create a .env file with the required API keys.")
        print("You can use .env.example as a template.")
        return False

    return True


def save_report(result, filename="latam_beer_market_report.txt"):
    """Save the final report to a file"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(result))
        print(f"📄 Report saved to: {filename}")
        return True
    except Exception as e:
        print(f"⚠️  Warning: Could not save report to file: {e}")
        return False


def main():
    """Main execution function"""

    # Check environment variables
    if not check_environment():
        return

    try:
        # Run the multi-agent market research
        result = run_market_research()

        # Display result
        print("\n" + "="*80)
        print("📊 FINAL REPORT")
        print("="*80 + "\n")
        print(result)
        print("\n" + "="*80 + "\n")

        # Save report to file
        save_report(result)

        print("✅ Market research completed successfully!")
        print("\nNext steps:")
        print("1. Review the report: latam_beer_market_report.txt")
        print("2. Validate findings with additional sources")
        print("3. Deep dive into top-ranked opportunities")
        print("4. Prepare expansion strategy based on recommendations\n")

    except KeyboardInterrupt:
        print("\n\n⚠️  Research interrupted by user")
        print("Progress may be lost. Consider running again for complete results.\n")

    except Exception as e:
        print(f"\n❌ Error during execution: {e}")
        print("\nTroubleshooting:")
        print("1. Verify API keys are correct in .env file")
        print("2. Check internet connection")
        print("3. Ensure sufficient API credits")
        print("4. Review error message above for details\n")


if __name__ == "__main__":
    main()
