import json
import pandas as pd
from collections import defaultdict
import re

# First, let's analyze the uploaded documents to extract all the tables and charts mentioned
# Based on the documents, I can see there are 42 tables and 20 charts mentioned

# Create a comprehensive analysis of the research data
research_summary = {
    "study_focus": "Transforming Bangladesh's Coastal Belt: An Integrated 17-SDG Framework for Sustainable Development in Dublar Char and the Sundarbans",
    "key_location": "Dublar Char - seasonal fishing settlement in Sundarbans UNESCO World Heritage Site",
    "research_scope": "Mixed-methods research with 300 Focus Group Discussion participants",
    "main_objective": "Achieve all 17 United Nations Sustainable Development Goals through single integrated coastal development intervention"
}

# Extract key data points from the research
key_findings = {
    "population_impact": "35,000+ seasonal workers, 43 million coastal belt residents",
    "economic_impact": "80% of Bangladesh's dried fish production, Tk 600-800 million annual value",
    "climate_vulnerability": "77.33% cyclone exposure, 40.66% tidal surge exposure", 
    "poverty_statistics": "80% debt dependency among workers, 28.57% boat owners in low income category",
    "gender_exclusion": "0% women participation during fishing season",
    "environmental_pressure": "1,500 trawlers seasonal operation, mangrove degradation from illegal cutting"
}

print("RESEARCH DOCUMENT ANALYSIS")
print("="*50)
print(f"Study Focus: {research_summary['study_focus']}")
print(f"Location: {research_summary['key_location']}")
print(f"Methodology: {research_summary['research_scope']}")
print(f"Objective: {research_summary['main_objective']}")
print()
print("KEY FINDINGS:")
for key, value in key_findings.items():
    print(f"• {key.replace('_', ' ').title()}: {value}")

# Now let's create a structured inventory of all the tables mentioned in the documents
tables_inventory = []

# Based on document analysis, here are the major tables I can identify:
table_data = [
    {
        "id": "table_01",
        "title": "Dublar Char Seasonal Settlement Characteristics", 
        "description": "Overview of population, economic output, infrastructure, and transformation needs",
        "category": "Infrastructure Assessment",
        "data_type": "Mixed",
        "source": "Primary field research and government documentation"
    },
    {
        "id": "table_02", 
        "title": "Socioeconomic Profile - Monthly Income Distribution",
        "description": "Income distribution by worker category (boat owners vs laborers)",
        "category": "Socioeconomics", 
        "data_type": "Percentage",
        "source": "FGD economic survey data (n=300)"
    },
    {
        "id": "table_03",
        "title": "Labor Force Characteristics and Working Patterns", 
        "description": "Working days, income ranges, and educational levels",
        "category": "Labor Analysis",
        "data_type": "Mixed",
        "source": "FGD participant demographics"
    },
    {
        "id": "table_04",
        "title": "Fish Production and Processing Analysis",
        "description": "Processing percentages and market values by species",
        "category": "Fisheries",
        "data_type": "Percentage/Currency", 
        "source": "Market analysis and production survey"
    },
    {
        "id": "table_07",
        "title": "Natural Disaster Vulnerability Profile",
        "description": "Exposure percentages to cyclone, tidal surge, flood, river erosion",
        "category": "Climate Risk",
        "data_type": "Percentage",
        "source": "Disaster impact assessment and community surveys"
    },
    {
        "id": "table_15",
        "title": "Complete SDG Integration Matrix - All 17 Goals Framework", 
        "description": "Comprehensive integration strategy for all 17 SDGs with specific targets and interventions",
        "category": "SDG Implementation",
        "data_type": "Framework",
        "source": "Integrated development planning framework"
    }
]

print("\nTABLES INVENTORY (Sample of Key Tables)")
print("="*50)
for i, table in enumerate(table_data, 1):
    print(f"{i}. {table['title']}")
    print(f"   Category: {table['category']}")  
    print(f"   Description: {table['description']}")
    print(f"   Data Type: {table['data_type']}")
    print()