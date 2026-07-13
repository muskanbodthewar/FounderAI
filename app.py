"""
=========================================================
FounderAI
Your AI Startup Co-Founder
AI Powered Startup Business Analyzer
=========================================================
"""

# --------------------------------------------------------
# Imports
# --------------------------------------------------------
import streamlit as st
import re

# --------------------------------------------------------
# Import AI Agents
# --------------------------------------------------------
from agents.idea_validator import validate_idea
from agents.market_research import market_research
from agents.competitor_analysis import competitor_analysis
from agents.business_model import business_model
from agents.financial_planner import financial_planner
from agents.marketing_strategy import marketing_strategy
from agents.investor_pitch import investor_pitch
from agents.roadmap import roadmap
from agents.startup_score import startup_score

# --------------------------------------------------------
# Page Configuration
# --------------------------------------------------------
st.set_page_config(
    page_title="FounderAI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------------
# Session State
# --------------------------------------------------------
if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

# --------------------------------------------------------
# Custom CSS
# --------------------------------------------------------
st.markdown("""
<style>

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

.hero{
    background:linear-gradient(90deg,#2563eb,#7c3aed);
    padding:35px;
    border-radius:18px;
    color:white;
    text-align:center;
    margin-bottom:25px;
}

.hero h1{
    font-size:48px;
    margin-bottom:10px;
}

.hero p{
    font-size:18px;
    color:#F3F4F6;
}

.feature-box{
    background:#F8FAFC;
    padding:18px;
    border-radius:12px;
    border:1px solid #E5E7EB;
    text-align:center;
    font-weight:600;
}

.metric-card{
    background:#ffffff;
    padding:15px;
    border-radius:12px;
    border:1px solid #E5E7EB;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------------
# Hero Section
# --------------------------------------------------------
st.markdown("""
<div class="hero">

<h1>🚀 FounderAI</h1>

<h3>Your AI Startup Co-Founder</h3>

<p>
Turn your startup idea into a complete business strategy with AI-powered insights.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("## ✨ Why Choose FounderAI?")

col1, col2 = st.columns(2)

with col1:
    st.info("""
📊 **Validate your startup idea**

Know whether your idea is worth building.
""")

    st.info("""
📈 **Research your market**

Understand opportunities and trends.
""")

    st.info("""
⚔️ **Analyze competitors**

Identify your competitive advantage.
""")

    st.info("""
🏢 **Build your business model**

Generate a complete business strategy.
""")

with col2:
    st.info("""
💰 **Financial planning**

Estimate costs, revenue and profitability.
""")

    st.info("""
📢 **Marketing strategy**

Create a customer acquisition plan.
""")

    st.info("""
🎤 **Investor pitch**

Generate a funding-ready startup pitch.
""")

    st.info("""
🗓️ **Execution roadmap**

Receive a practical 12-month action plan.
""")

st.divider()
# --------------------------------------------------------
# User Input
# --------------------------------------------------------
st.subheader("💡 Describe Your Startup Idea")

startup_idea = st.text_area(
    "",
    height=220,
    placeholder="""
Example:

An AI platform that helps students prepare for placements by generating
mock interviews, resume reviews, personalized interview questions,
and company-specific preparation plans.
"""
)

analyze = st.button(
    "🚀 Analyze Startup",
    use_container_width=True
)
# --------------------------------------------------------
# Run FounderAI
# --------------------------------------------------------

if analyze:

    if startup_idea.strip() == "":

        st.warning("⚠️ Please enter your startup idea.")

    else:

        with st.spinner("🤖 FounderAI is analyzing your startup..."):

            # -----------------------------
            # Run All AI Agents
            # -----------------------------
            st.session_state.score_report = startup_score(startup_idea)

            st.session_state.idea_report = validate_idea(startup_idea)

            st.session_state.market_report = market_research(startup_idea)

            st.session_state.competitor_report = competitor_analysis(startup_idea)

            st.session_state.business_report = business_model(startup_idea)

            st.session_state.finance_report = financial_planner(startup_idea)

            st.session_state.marketing_report = marketing_strategy(startup_idea)

            st.session_state.investor_report = investor_pitch(startup_idea)

            st.session_state.roadmap_report = roadmap(startup_idea)

            st.session_state.startup_idea = startup_idea

            st.session_state.analysis_done = True

        st.success("🎉 Startup Analysis Completed Successfully!")

# --------------------------------------------------------
# Show Results Only After Analysis
# --------------------------------------------------------

if st.session_state.analysis_done:

    score_report = st.session_state.score_report
    idea_report = st.session_state.idea_report
    market_report = st.session_state.market_report
    competitor_report = st.session_state.competitor_report
    business_report = st.session_state.business_report
    finance_report = st.session_state.finance_report
    marketing_report = st.session_state.marketing_report
    investor_report = st.session_state.investor_report
    roadmap_report = st.session_state.roadmap_report
    startup_idea = st.session_state.startup_idea

    st.divider()

    st.header("📊 FounderAI Analysis Report")
    # --------------------------------------------------------
    # AI Startup Score Dashboard
    # --------------------------------------------------------

    st.subheader("⭐ AI Startup Score")

    overall = re.search(r"Overall Startup Score:\s*(\d+/\d+)", score_report)
    innovation = re.search(r"Innovation:\s*(\d+/\d+)", score_report)
    market = re.search(r"Market Demand:\s*(\d+/\d+)", score_report)
    revenue = re.search(r"Revenue Potential:\s*(\d+/\d+)", score_report)
    scalability = re.search(r"Scalability:\s*(\d+/\d+)", score_report)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(
            "Overall",
            overall.group(1) if overall else "N/A"
        )

    with col2:
        st.metric(
            "Innovation",
            innovation.group(1) if innovation else "N/A"
        )

    with col3:
        st.metric(
            "Market",
            market.group(1) if market else "N/A"
        )

    with col4:
        st.metric(
            "Revenue",
            revenue.group(1) if revenue else "N/A"
        )

    with col5:
        st.metric(
            "Scalability",
            scalability.group(1) if scalability else "N/A"
        )

    st.info(
        "This score is AI-generated based on innovation, feasibility, "
        "market demand, scalability, revenue potential and business model."
    )

    st.divider()

    # --------------------------------------------------------
    # Detailed Startup Score
    # --------------------------------------------------------

    with st.expander("⭐ Detailed Startup Score", expanded=False):
        st.write(score_report)

    # --------------------------------------------------------
    # Idea Validation
    # --------------------------------------------------------

    with st.expander("🧠 Idea Validation", expanded=True):
        st.write(idea_report)

    # --------------------------------------------------------
    # Market Research
    # --------------------------------------------------------

    with st.expander("📊 Market Research"):
        st.write(market_report)

    # --------------------------------------------------------
    # Competitor Analysis
    # --------------------------------------------------------

    with st.expander("⚔️ Competitor Analysis"):
        st.write(competitor_report)

    # --------------------------------------------------------
    # Business Model
    # --------------------------------------------------------

    with st.expander("🏢 Business Model"):
        st.write(business_report)

    # --------------------------------------------------------
    # Financial Planning
    # --------------------------------------------------------

    with st.expander("💰 Financial Planning"):
        st.write(finance_report)

    # --------------------------------------------------------
    # Marketing Strategy
    # --------------------------------------------------------

    with st.expander("📢 Marketing Strategy"):
        st.write(marketing_report)

    # --------------------------------------------------------
    # Investor Pitch
    # --------------------------------------------------------

    with st.expander("🎤 Investor Pitch"):
        st.write(investor_report)

    # --------------------------------------------------------
    # Roadmap
    # --------------------------------------------------------

    with st.expander("🗓️ 12-Month Roadmap"):
        st.write(roadmap_report)
    # --------------------------------------------------------
    # Download Startup Report
    # --------------------------------------------------------

    st.divider()

    final_report = f"""
============================================================
FounderAI - Startup Analysis Report
============================================================

STARTUP IDEA
------------------------------------------------------------

{startup_idea}

============================================================
AI STARTUP SCORE
============================================================

{score_report}

============================================================
IDEA VALIDATION
============================================================

{idea_report}

============================================================
MARKET RESEARCH
============================================================

{market_report}

============================================================
COMPETITOR ANALYSIS
============================================================

{competitor_report}

============================================================
BUSINESS MODEL
============================================================

{business_report}

============================================================
FINANCIAL PLANNING
============================================================

{finance_report}

============================================================
MARKETING STRATEGY
============================================================

{marketing_report}

============================================================
INVESTOR PITCH
============================================================

{investor_report}

============================================================
12-MONTH ROADMAP
============================================================

{roadmap_report}
"""

    st.download_button(
        label="📄 Download Startup Report",
        data=final_report,
        file_name="FounderAI_Report.txt",
        mime="text/plain",
        use_container_width=True,
        key="download_report"
    )

    st.success("🎉 Your complete startup analysis is ready!")