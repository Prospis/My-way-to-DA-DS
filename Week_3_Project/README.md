# Uber & Lyft Price Analysis

## Dataset
- Source: [Kaggle - Uber & Lyft Dataset Boston, MA](https://www.kaggle.com/datasets/ravi72munde/uber-lyft-cab-prices)
- Size: 693,071 rides + 6,276 weather records
- Period: November-December 2018
- Location: Boston, MA

## Key Findings

1. **Lyft is 12% more expensive than Uber** ($17.35 vs $15.47 average)
2. **Premium vehicles cost 3-5x more** (Lux Black XL: $32 vs Shared: $6)
3. **Weather has minimal impact** on pricing (rain correlation ~0)
4. **Most rides cost $10-20** (99.7% of trips under $50)

## Tools Used
- Python 3.x
- Pandas (data manipulation)
- Matplotlib (visualization)
- Seaborn (advanced charts)

## Files
- `uber_lyft_analysis.ipynb` - Main analysis notebook
- `images/` - 5 visualizations
- `data/` - Raw datasets (not in repo)

## Limitations
- Dataset covers only 2 months (Nov-Dec 2018)
- Artificially balanced vehicle types
- No surge pricing patterns detected