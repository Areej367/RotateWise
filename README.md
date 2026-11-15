# 🌾 RotateWise: Crop Rotation Advisor

A decision-support web app for the **2026 NASA Space Apps Challenge** (crop-rotation / soil-health challenge).
It helps farmers anywhere compare crop rotations that protect soil, save water and adapt to changing weather,
using NASA POWER climate data plus the farmer's own soil, water, equipment, market and priorities.

> A supportive tool: it highlights patterns and possibilities. It does **not** replace farmer judgment or local agricultural expertise.

## Features
- Compares **4 rotation strategies**, including the farmer's existing one
- Each card explains: why suggested, benefits, risks for local review, evidence and data gaps
- Climate page: rainfall, temperature, dry months, frost-risk months, monthly water balance
- Field calendar showing bare-soil months; cover crops fill the gaps
- Vulnerable-season warnings for the existing rotation
- 5-year soil-health outlook per rotation
- Field risk map (erosion, water stress, frost pockets): existing rotation vs top match
- **Confidence score**: each rotation re-scored in 20 simulated climate futures
- Rainfall and warming scenario sliders; custom climate data entry for any location
- Downloadable action plan (PDF), settings saved on-device (no login), dark mode, accessible and responsive

## NASA data
Monthly temperature (T2M) and rainfall (PRECTOTCORR) from the **NASA POWER** long-term climatology API for one
representative point per region. `fetch_nasa_power.py` regenerates the values.
SMAP, MODIS/Landsat NDVI, GPM, ECOSTRESS and GRACE-FO are planned future layers (not used yet).

## Run it
No build step. Open `index.html` in a browser, or serve the folder:

    python3 -m http.server 8000

### Deploy on GitHub Pages
1. Push this folder to a GitHub repository.
2. Repo **Settings → Pages → Deploy from a branch → main / (root)**.
3. Your app will be live at `https://<username>.github.io/<repo>/`.

## How scoring works
Each rotation is rated 0–1 on water use, income, nitrogen fixing, soil cover, organic matter, heat resilience and
rainfall fit. Farmer priority sliders weight these. Growing windows come from the local temperature curve.
A robustness test reports how often each rotation stays the top choice across 20 simulated futures.

## Limitations
- Crop ratings are simplified 1–5 estimates; climate is one point per region.
- The field map is a schematic driven by a user-entered slope.
- Crop water demand is roughly estimated from temperature.
- Validate every suggestion with local agronomists (soil tests, seed, pests, markets, water rights).

Built for the NASA Space Apps Challenge 2026.

## AI disclosure
The code, text and home-page illustration of this project were created with AI assistance (Claude by Anthropic) and reviewed by the author. The scoring model is rule-based and contains no AI model. No NASA logos or branding are used. Climate data come from the NASA POWER API.

## License
Released under the [MIT License](LICENSE).
