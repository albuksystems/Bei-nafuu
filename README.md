# PataHapa Prices - Hyper-Local SEO Traffic Delivery System

PataHapa Prices is an "indirect traffic delivery" platform designed to rank for high-intent local search terms in Mlolongo, Syokimau, Athi River, and surrounding areas. The goal is to capture local shoppers searching for home and lifestyle products on Google and direct them to paying local sellers.

## Business Model: Traffic Delivery

Unlike traditional affiliate sites, this platform focuses on **Hyper-Local SEO**. 
1. **Rank**: We build pages optimized for terms like "cheapest water tank Mlolongo".
2. **Capture**: We provide price references from major retailers (Jumia, Naivas) to build trust and content depth.
3. **Deliver**: We sell "Featured Seller" slots to local physical shops in these areas, delivering high-intent foot traffic or direct leads.

## Key Features

- **SEO-First Architecture**: Built-in Schema.json (JSON-LD) for Local Business and Products.
- **Hyper-Local Targeting**: Specifically targets Mlolongo, Syokimau, Athi River, Sabaki, and Katani.
- **Dynamic Price References**: Auto-updates daily from major Kenyan retailers via GitHub Actions.
- **Seller Monetization**: Dedicated slots for local sellers to list their shops and contact details.
- **Mobile-First**: Optimized for the high mobile usage in the Nairobi-Machakos corridor.

## Project Structure

```
patahapa-prices/
├── .github/
│   └── workflows/
│       └── scrape-prices.yml    # Daily scraping & SEO data refresh
├── scraper/
│   └── scrape.py               # Python scraper for local-demand products
├── data/
│   └── prices.json             # Reference price data
├── index.html                  # SEO-optimized landing page
└── README.md                   # Project documentation
```

## How to Add New Product Pages

To expand the platform to new product categories (e.g., "Solar Panels in Athi River"):

1. **Update Scraper**: Add the new category and relevant keywords to the `PRODUCTS` list in `scraper/scrape.py`.
2. **Update HTML**: 
   - Add a new `<div>` section in `index.html` for the category.
   - Ensure the `<h3>` includes the local search term (e.g., "Best Solar Panels Athi River").
   - Add the new category key to the `loadPrices()` JavaScript function to fetch the data.
3. **Optimize SEO**: Add a new entry to the JSON-LD schema if necessary.

## Onboarding Local Sellers

1. **Inbound**: Sellers click the "List Your Shop" CTA on the site.
2. **Verification**: PataHapa team verifies the physical location and stock of the seller.
3. **Placement**: Once payment is confirmed, replace the `seller-slot` placeholder in `index.html` with the seller's actual business name, logo, and WhatsApp/Phone link.

## SEO Strategy & Expected Timeline

- **Content Depth**: By combining local search terms with real-time price data from Jumia/Naivas, we provide more value than a simple directory.
- **Ranking Timeline**:
  - **Month 1**: Google indexing and initial ranking for long-tail keywords.
  - **Month 3**: Appearing on page 1 for specific "Product + Area" searches.
  - **Month 6**: Established authority in the Mlolongo/Syokimau corridor.
- **Tracking**: Use **Google Search Console** to monitor which local pages are bringing in the most traffic and adjust product focus accordingly.

## Maintenance

The site auto-updates its price references daily at 6 AM EAT via GitHub Actions. This keeps the content fresh in the eyes of Google's crawlers without manual intervention.

---
&copy; 2026 PataHapa. Serving the Nairobi-Machakos corridor.
