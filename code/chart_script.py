import plotly.graph_objects as go
import pandas as pd

# Data for the Bangladesh SDG Research Dashboard project
phases_data = [
    {
        "phase": "Foundation",
        "duration": "Week 1-2", 
        "deliverables": 4,
        "budget_percent": 25,
        "team_involvement": "Full team",
        "key_milestone": "Clickable prototype"
    },
    {
        "phase": "Core Features",
        "duration": "Week 3-5",
        "deliverables": 4, 
        "budget_percent": 35,
        "team_involvement": "Full team",
        "key_milestone": "All data accessible"
    },
    {
        "phase": "Advanced",
        "duration": "Week 6-8",
        "deliverables": 4,
        "budget_percent": 30,
        "team_involvement": "Full team", 
        "key_milestone": "Professional quality"
    },
    {
        "phase": "Launch/Train",
        "duration": "Week 9-10",
        "deliverables": 4,
        "budget_percent": 10,
        "team_involvement": "Reduced team",
        "key_milestone": "Live dashboard"
    }
]

# Create timeline positions
timeline_data = []
colors = ['#1FB8CD', '#5D878F', '#2E8B57', '#13343B']  # Blue/teal color scheme

for i, phase in enumerate(phases_data):
    # Extract week numbers from duration
    if "1-2" in phase["duration"]:
        start_week = 1
        duration = 2
    elif "3-5" in phase["duration"]:
        start_week = 3
        duration = 3
    elif "6-8" in phase["duration"]:
        start_week = 6
        duration = 3
    elif "9-10" in phase["duration"]:
        start_week = 9
        duration = 2
    
    timeline_data.append({
        'phase_name': phase["phase"],
        'start': start_week,
        'duration': duration,
        'budget_pct': phase["budget_percent"],
        'deliverables': phase["deliverables"],
        'milestone': phase["key_milestone"][:15],  # 15 char limit
        'color': colors[i]
    })

# Create the timeline chart using Gantt-style horizontal bars
fig = go.Figure()

for i, data in enumerate(timeline_data):
    fig.add_trace(go.Bar(
        name=data['phase_name'],
        x=[data['duration']],
        y=[data['phase_name']],
        orientation='h',
        marker_color=data['color'],
        text=f"{data['budget_pct']}%",
        textposition='inside',
        textfont=dict(color='white', size=12),
        hovertemplate=f"""
        <b>{data['phase_name']}</b><br>
        Weeks: {data['start']}-{data['start']+data['duration']-1}<br>
        Budget: {data['budget_pct']}%<br>
        Deliverables: {data['deliverables']}<br>
        Milestone: {data['milestone']}<br>
        <extra></extra>
        """,
        base=data['start'] - 1
    ))

# Update layout
fig.update_layout(
    title="SDG Dashboard Project Timeline",
    xaxis_title="Week",
    yaxis_title="Phase",
    showlegend=True,
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5)
)

# Update x-axis to show weeks clearly
fig.update_xaxes(
    range=[0, 11],
    tickvals=list(range(1, 11)),
    ticktext=[f"W{i}" for i in range(1, 11)]
)

# Update traces to not clip on axis
fig.update_traces(cliponaxis=False)

# Save the chart
fig.write_image("sdg_dashboard_timeline.png")