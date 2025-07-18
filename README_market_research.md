# Market Research & Competitor Analysis – Streaming Services (2025)

## Overview

This project demonstrates how to compile publicly available market data, benchmark competitors, and conduct strategic analyses using SWOT and PESTLE frameworks. We focus on the U.S. video‑streaming service market in 2025 and analyse the major players—Amazon Prime Video, Netflix, Max, Disney+, Hulu, Paramount+, Apple TV+, Peacock and the aggregate “Other” category—by market share. The dataset comes from Statista figures reported in an Evoca market‑share study【472247096925510†L76-L105】.

## Project Structure

- **`us_streaming_market_share.csv`** – CSV dataset listing platforms and their U.S. market share percentages.
- **`market_research_analysis.py`** – Python script that loads the dataset, ranks platforms, calculates differences from the top competitor and produces bar and pie charts (`us_streaming_market_share_bar.png`, `us_streaming_market_share_pie.png`).
- **`market_share_summary.csv`** – Summary table of platforms, market share, ranking and difference from the leader.
- **`Market_Research_Competitor_Analysis.ipynb`** – Jupyter notebook documenting the analysis steps, including data loading, ranking, visualisation and insights.
- **`swot_analysis.md`** – SWOT analysis of Netflix, Amazon Prime Video and Disney+【628137180640470†L124-L134】【943408289325718†L178-L207】【775906557458188†L65-L72】.
- **`pestle_analysis.md`** – PESTLE analysis outlining political, economic, social and technological factors affecting the streaming industry【695573808259092†L51-L74】【695573808259092†L76-L89】.
- **`report_market_research.md`** – Detailed report combining quantitative findings with strategic insights and recommendations.

## Key Findings

- **Market leaders:** Amazon Prime Video (22 %) and Netflix (21 %) dominate the U.S. streaming market, together capturing nearly half of subscribers【472247096925510†L76-L105】.
- **Mid‑tier competitors:** Max (13 %), Disney+ (12 %) and Hulu (11 %) form a competitive middle tier.
- **Niche services:** Paramount+ (9 %), Apple TV+ (7 %), Peacock (1 %) and “Other” (4 %) hold smaller shares.
- **Strategic insights:** SWOT analysis highlights Netflix’s strong brand and original content, but notes rising debt and intense competition【628137180640470†L124-L134】【628137180640470†L137-L144】. Amazon Prime Video benefits from bundled services but suffers from a messy interface and limited original content【943408289325718†L178-L207】【943408289325718†L209-L226】. Disney+ excels in family‑friendly content but faces a niche audience and higher prices【775906557458188†L65-L72】【775906557458188†L73-L76】.
- **Macro factors:** PESTLE analysis underscores how geopolitical tensions, economic conditions, cultural preferences and technological advancements influence streaming services【695573808259092†L51-L74】【695573808259092†L76-L89】.

## Usage

1. Run `market_research_analysis.py` to generate the summary table (`market_share_summary.csv`) and visualisations (`us_streaming_market_share_bar.png`, `us_streaming_market_share_pie.png`).
   ```bash
   python3 market_research_analysis.py
   ```
2. Open `Market_Research_Competitor_Analysis.ipynb` to reproduce the analysis and review narrative insights.
3. Read `swot_analysis.md` and `pestle_analysis.md` for qualitative analyses.
4. Consult `report_market_research.md` for a comprehensive report, including recommendations for strategic actions.

## Insights and Recommendations

- **Differentiate content and pricing:** Mid‑tier services should invest in exclusive content and consider competitive pricing to compete with Amazon Prime Video and Netflix.
- **Bundle and partner:** Leveraging partnerships (e.g., telecom or gaming bundles) can expand reach and make offerings stickier.
- **Localise content:** Localised and multicultural content can capture audiences with regional preferences.
- **Ad‑supported and mobile tiers:** Low‑price mobile and ad‑supported plans attract price‑sensitive consumers and help gain share in emerging markets.
- **Improve user experience:** Streamlining interfaces and search functions, particularly for Prime Video, can improve retention.
- **Mitigate threats:** Counteract piracy, monitor regulatory changes and respond to competitive pricing to reduce churn.

This project illustrates how data collection, quantitative benchmarking and strategic frameworks can inform business and competitive decisions for streaming services and other industries.
