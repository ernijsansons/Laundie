#!/usr/bin/env python3
"""
Laundromat Sales Agent - Comprehensive USA Laundromat Listing Finder
Searches across multiple platforms for laundromats for sale in the last 90 days
"""

import json
import re
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Set
from dataclasses import dataclass, asdict
from collections import defaultdict
import hashlib

@dataclass
class LaundryListing:
    """Data structure for a laundromat listing"""
    business_name: str
    city: str
    state: str
    zip_code: str
    full_address: str
    asking_price: str
    description: str
    listing_date: str
    source_url: str
    source_platform: str
    contact_info: str
    status: str

    def get_hash(self) -> str:
        """Generate unique hash for deduplication"""
        # Use location + price as primary identifier
        key = f"{self.city}_{self.state}_{self.asking_price}_{self.business_name}".lower()
        return hashlib.md5(key.encode()).hexdigest()

class LaundryListingAgent:
    """Agent to systematically search for laundromat listings"""

    def __init__(self):
        self.listings: Dict[str, LaundryListing] = {}
        self.search_queries = self._initialize_search_queries()
        self.sources_searched: Set[str] = set()
        self.start_date = datetime(2025, 8, 3)  # 90 days before Oct 31, 2025
        self.end_date = datetime(2025, 10, 31)

    def _initialize_search_queries(self) -> Dict[str, List[str]]:
        """Initialize comprehensive search queries for different platforms"""
        return {
            "business_brokers": [
                "laundromat for sale USA site:bizbuysell.com after:2025-08-03",
                "coin laundry business for sale site:bizbuysell.com after:2025-08-03",
                "laundromat for sale site:bizquest.com after:2025-08-03",
                "laundromat for sale site:businessesforsale.com after:2025-08-03",
                "coin laundry for sale site:loopnet.com after:2025-08-03",
            ],
            "commercial_real_estate": [
                "laundromat business for sale site:loopnet.com after:2025-08-03",
                "laundromat for sale site:crexi.com after:2025-08-03",
                "coin operated laundry for sale USA after:2025-08-03",
            ],
            "classifieds": [
                "laundromat for sale site:craigslist.org after:2025-08-03",
                "coin laundry business for sale site:craigslist.org after:2025-08-03",
                "washateria for sale site:craigslist.org after:2025-08-03",
            ],
            "social_media": [
                "laundromat for sale site:reddit.com after:2025-08-03",
                "laundromat business for sale site:facebook.com after:2025-08-03",
            ],
            "specialized_brokers": [
                "laundromat for sale site:sunbeltnetwork.com after:2025-08-03",
                "laundromat for sale site:tworld.com after:2025-08-03",
                "coin laundry for sale USA 2025",
            ],
            "state_specific": [],  # Will be populated dynamically
        }

    def add_listing(self, listing: LaundryListing) -> bool:
        """Add a listing if not duplicate"""
        listing_hash = listing.get_hash()
        if listing_hash not in self.listings:
            self.listings[listing_hash] = listing
            return True
        return False

    def get_all_queries(self) -> List[tuple]:
        """Get all search queries with their categories"""
        queries = []
        for category, query_list in self.search_queries.items():
            for query in query_list:
                queries.append((category, query))
        return queries

    def parse_listing_from_search_result(self, result_text: str, url: str, platform: str) -> Optional[LaundryListing]:
        """Attempt to parse listing data from search result text"""
        # This is a placeholder - actual parsing would happen after fetching page content
        # For now, we'll return None and handle parsing in the main execution loop
        return None

    def generate_report(self) -> str:
        """Generate comprehensive markdown report of all findings"""
        if not self.listings:
            return "# Laundromat Listings Report\n\nNo listings found.\n"

        # Sort by state, then price
        sorted_listings = sorted(
            self.listings.values(),
            key=lambda x: (x.state, self._extract_price_for_sort(x.asking_price)),
            reverse=False
        )

        report = f"""# Comprehensive Laundromat Listings Report
## USA Laundromats For Sale (Last 90 days: Aug 3 - Oct 31, 2025)

**Total Listings Found:** {len(self.listings)}
**Sources Searched:** {len(self.sources_searched)}
**Date Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

---

## All Listings

| Business Name | Location | Price | Description | Listing Date | Source | Contact | Status |
|--------------|----------|-------|-------------|--------------|--------|---------|--------|
"""

        for listing in sorted_listings:
            location = f"{listing.city}, {listing.state} {listing.zip_code}".strip()
            description = listing.description[:100] + "..." if len(listing.description) > 100 else listing.description
            description = description.replace("|", "\\|").replace("\n", " ")

            report += f"| {listing.business_name} | {location} | {listing.asking_price} | {description} | {listing.listing_date} | [{listing.source_platform}]({listing.source_url}) | {listing.contact_info} | {listing.status} |\n"

        # Add summary by state
        report += "\n\n## Summary by State\n\n"
        state_counts = defaultdict(int)
        for listing in sorted_listings:
            state_counts[listing.state] += 1

        for state, count in sorted(state_counts.items()):
            report += f"- **{state}**: {count} listings\n"

        return report

    def _extract_price_for_sort(self, price_str: str) -> float:
        """Extract numeric price for sorting"""
        # Remove $ , and other non-numeric characters except decimal
        cleaned = re.sub(r'[^\d.]', '', price_str)
        try:
            return float(cleaned) if cleaned else 0
        except:
            return 0

    def save_results(self, filename: str = "laundromat_listings.json"):
        """Save results to JSON file"""
        with open(filename, 'w') as f:
            json.dump([asdict(listing) for listing in self.listings.values()], f, indent=2)

# Initialize the agent
agent = LaundryListingAgent()

print("=" * 80)
print("LAUNDROMAT SALES AGENT - INITIALIZED")
print("=" * 80)
print(f"Search Period: {agent.start_date.strftime('%Y-%m-%d')} to {agent.end_date.strftime('%Y-%m-%d')}")
print(f"Total Search Queries Prepared: {sum(len(v) for v in agent.search_queries.values())}")
print("\nAgent ready for systematic search execution...")
print("=" * 80)
