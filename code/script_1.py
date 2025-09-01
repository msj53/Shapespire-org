# Let's create structured data extracts from the key tables mentioned in the documents

import json
import pandas as pd

# Extract Table 2: Socioeconomic Profile - Monthly Income Distribution
income_distribution_data = [
    {
        "stakeholder_group": "Boat Owners",
        "low_income_percent": 28.57,
        "moderate_income_percent": 40.47, 
        "high_income_percent": 30.96,
        "analysis": "Higher economic stress despite asset ownership"
    },
    {
        "stakeholder_group": "Laborers", 
        "low_income_percent": 14.81,
        "moderate_income_percent": 39.81,
        "high_income_percent": 45.38,
        "analysis": "Higher concentration in high income bracket"
    }
]

# Extract Table 4: Fish Production and Processing Analysis
fish_processing_data = [
    {
        "fish_species": "Loitta",
        "processing_percentage": 90.00,
        "market_value_category": "High-value premium", 
        "market_value_bdt_per_kg": "280-320",
        "sustainability_risk": "High (overexploitation)"
    },
    {
        "fish_species": "Churi", 
        "processing_percentage": 88.66,
        "market_value_category": "Popular commercial",
        "market_value_bdt_per_kg": "250-290", 
        "sustainability_risk": "High (demand pressure)"
    },
    {
        "fish_species": "Faissa",
        "processing_percentage": 42.67,
        "market_value_category": "Moderate market",
        "market_value_bdt_per_kg": "180-220",
        "sustainability_risk": "Medium"
    },
    {
        "fish_species": "Rupchada",
        "processing_percentage": 23.33, 
        "market_value_category": "Specialized market",
        "market_value_bdt_per_kg": "350-400",
        "sustainability_risk": "Critical (supply shortage)"
    },
    {
        "fish_species": "Others",
        "processing_percentage": 18.66,
        "market_value_category": "Diverse species mix", 
        "market_value_bdt_per_kg": "120-180",
        "sustainability_risk": "Variable"
    },
    {
        "fish_species": "Powa",
        "processing_percentage": 16.00,
        "market_value_category": "Niche market",
        "market_value_bdt_per_kg": "160-200", 
        "sustainability_risk": "Low"
    }
]

# Extract Table 7: Natural Disaster Vulnerability Profile  
disaster_vulnerability_data = [
    {
        "disaster_type": "Cyclone",
        "exposure_percentage": 77.33,
        "frequency_per_decade": "8-12 events",
        "risk_severity": "Extreme vulnerability",
        "impact_on_operations": "Season disruption",
        "economic_impact_bdt": "150,000-300,000"
    },
    {
        "disaster_type": "Tidal Surge", 
        "exposure_percentage": 40.66,
        "frequency_per_decade": "15-20 events",
        "risk_severity": "High coastal risk",
        "impact_on_operations": "Infrastructure damage",
        "economic_impact_bdt": "50,000-100,000"
    },
    {
        "disaster_type": "Flooding",
        "exposure_percentage": 20.00,
        "frequency_per_decade": "5-8 events", 
        "risk_severity": "Moderate impact",
        "impact_on_operations": "Temporary displacement",
        "economic_impact_bdt": "75,000-150,000"
    },
    {
        "disaster_type": "River Bank Erosion",
        "exposure_percentage": 12.66,
        "frequency_per_decade": "3-5 events",
        "risk_severity": "Gradual threat", 
        "impact_on_operations": "Long-term land loss",
        "economic_impact_bdt": "100,000-200,000"
    },
    {
        "disaster_type": "Others",
        "exposure_percentage": 2.00,
        "frequency_per_decade": "Variable",
        "risk_severity": "Minor disasters",
        "impact_on_operations": "Various small impacts", 
        "economic_impact_bdt": "Variable"
    }
]

# Extract Tourism Development Priorities
tourism_priorities_data = [
    {
        "enhancement_need": "Transportation improvement",
        "percentage_ranking": 36.00,
        "priority_level": "Critical infrastructure",
        "investment_requirement": "High capital investment"
    },
    {
        "enhancement_need": "Communication systems", 
        "percentage_ranking": 34.00,
        "priority_level": "Essential connectivity",
        "investment_requirement": "Medium-high investment"
    },
    {
        "enhancement_need": "Publicity and marketing",
        "percentage_ranking": 27.33,
        "priority_level": "Market development",
        "investment_requirement": "Medium investment"
    },
    {
        "enhancement_need": "Security measures",
        "percentage_ranking": 20.00,
        "priority_level": "Safety concerns", 
        "investment_requirement": "Government coordination"
    },
    {
        "enhancement_need": "Government help",
        "percentage_ranking": 18.00,
        "priority_level": "Policy support",
        "investment_requirement": "Institutional engagement"
    },
    {
        "enhancement_need": "Medical facility",
        "percentage_ranking": 3.33,
        "priority_level": "Healthcare needs",
        "investment_requirement": "Infrastructure development"
    }
]

# Create DataFrames and save as CSV
df_income = pd.DataFrame(income_distribution_data)
df_fish = pd.DataFrame(fish_processing_data)
df_disaster = pd.DataFrame(disaster_vulnerability_data)
df_tourism = pd.DataFrame(tourism_priorities_data)

print("DATA EXTRACTION COMPLETE")
print("="*50)
print(f"Income Distribution Data: {len(df_income)} records")
print(f"Fish Processing Data: {len(df_fish)} records") 
print(f"Disaster Vulnerability Data: {len(df_disaster)} records")
print(f"Tourism Priorities Data: {len(df_tourism)} records")
print()

# Display sample data
print("SAMPLE: Income Distribution by Worker Category")
print(df_income.to_string(index=False))
print()

print("SAMPLE: Fish Processing by Species (Top 3)")
print(df_fish.head(3)[['fish_species', 'processing_percentage', 'market_value_category']].to_string(index=False))
print()

print("SAMPLE: Disaster Vulnerability (Top 3 Risks)")  
print(df_disaster.head(3)[['disaster_type', 'exposure_percentage', 'risk_severity']].to_string(index=False))