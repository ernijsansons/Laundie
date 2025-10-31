#!/usr/bin/env python3
"""
Comprehensive Laundromat Listings Database Builder
==================================================
Compiles all verified listings with complete data fields
"""

import json
import csv
from datetime import datetime
from typing import List, Dict, Any
from dataclasses import dataclass, asdict, field


@dataclass
class LaundryListingComplete:
    """Complete laundromat listing with all fields"""
    # Identifiers
    listing_id: str

    # Business Information
    business_name: str
    dba_name: str = ""

    # Location Details
    street_address: str = ""
    city: str = ""
    state: str = ""
    zip_code: str = ""
    county: str = ""
    full_address: str = ""

    # Financial Information
    asking_price: str = ""
    asking_price_numeric: float = 0.0
    gross_revenue: str = ""
    gross_revenue_numeric: float = 0.0
    net_income: str = ""
    net_income_numeric: float = 0.0
    cash_flow: str = ""
    ebitda: str = ""
    monthly_revenue: str = ""
    monthly_expenses: str = ""

    # Property Details
    square_footage: str = ""
    building_owned_or_leased: str = ""
    monthly_rent: str = ""
    lease_terms: str = ""
    lease_expiration: str = ""
    real_estate_included: str = "No"
    property_type: str = ""

    # Equipment & Facilities
    number_of_washers: str = ""
    number_of_dryers: str = ""
    washer_brands: str = ""
    dryer_brands: str = ""
    equipment_age: str = ""
    equipment_condition: str = ""
    recent_upgrades: str = ""
    card_system: str = ""
    additional_equipment: str = ""

    # Business Operations
    years_established: str = ""
    hours_of_operation: str = ""
    employees: str = ""
    owner_involvement: str = ""
    business_type: str = ""  # attended, unattended, semi-absentee
    services_offered: str = ""

    # Market Information
    demographics: str = ""
    competition: str = ""
    growth_potential: str = ""
    reason_for_sale: str = ""

    # Listing Details
    listing_date: str = ""
    days_on_market: str = ""
    source_platform: str = ""
    source_url: str = ""
    listing_status: str = "Active"
    last_updated: str = ""

    # Contact Information
    broker_name: str = ""
    broker_company: str = ""
    broker_phone: str = ""
    broker_email: str = ""
    contact_method: str = ""

    # Additional Details
    description: str = ""
    highlights: str = ""
    photos_available: str = "No"
    financing_available: str = ""
    seller_financing: str = ""
    training_included: str = ""

    # Verification
    verified: bool = False
    verification_date: str = ""
    data_completeness_score: float = 0.0


class LaundryListingDatabase:
    """Database of all verified laundromat listings with complete information"""

    def __init__(self):
        self.listings: List[LaundryListingComplete] = []
        self._populate_verified_listings()

    def _populate_verified_listings(self):
        """Populate database with all verified listings from our research"""

        # =====================================================================
        # CRAIGSLIST LISTINGS (Verified from searches)
        # =====================================================================

        self.listings.append(LaundryListingComplete(
            listing_id="CL-NY-001",
            business_name="Yonkers Laundromat",
            street_address="Location in Yonkers",
            city="Yonkers",
            state="NY",
            zip_code="",
            full_address="Yonkers, Westchester County, NY",
            asking_price="Not Listed",
            asking_price_numeric=0.0,
            gross_revenue="$13,000-$14,000/month",
            gross_revenue_numeric=156000.0,  # Annual estimate
            monthly_revenue="$13,000-$14,000",
            equipment_condition="Brand New Machines",
            recent_upgrades="Totally renovated",
            listing_date="January 2025",
            source_platform="Craigslist",
            source_url="https://newyork.craigslist.org/wch/bfs/d/yonkers-yonkers-laundromat-for-sale-top/7815592650.html",
            listing_status="Active",
            description="Top location, brand new machines, totally renovated",
            highlights="New equipment, high traffic location, strong monthly income",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.55
        ))

        self.listings.append(LaundryListingComplete(
            listing_id="CL-NY-002",
            business_name="Queens Laundromat",
            street_address="Forest Hills area",
            city="Queens",
            state="NY",
            zip_code="",
            county="Queens County",
            full_address="Forest Hills, Queens, NY",
            asking_price="$280,000",
            asking_price_numeric=280000.0,
            gross_revenue="$20,000/month",
            gross_revenue_numeric=240000.0,
            net_income="$5,000-$6,000/month",
            net_income_numeric=66000.0,  # Annual estimate
            monthly_revenue="$20,000",
            listing_date="2025",
            source_platform="Craigslist",
            source_url="https://newyork.craigslist.org/que/bfd/d/forest-hills-laundromat-for-sale-queens/7842094786.html",
            listing_status="Active",
            description="Established operation with strong monthly cash flow",
            highlights="$20K monthly gross, $5-6K monthly net, established customer base",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.65
        ))

        self.listings.append(LaundryListingComplete(
            listing_id="CL-CA-001",
            business_name="Taraval Street Laundromat",
            street_address="Taraval Street",
            city="San Francisco",
            state="CA",
            zip_code="",
            full_address="Taraval St, San Francisco, CA",
            asking_price="Not Listed",
            gross_revenue="$240,000+ average (6-year avg)",
            gross_revenue_numeric=240000.0,
            years_established="Long-established",
            business_type="Self-serve",
            listing_date="May 2025",
            source_platform="Craigslist",
            source_url="https://sfbay.craigslist.org/sfc/bfs/d/san-francisco-for-sale-established-self/7848081926.html",
            listing_status="Active",
            description="Long-established self-serve laundromat with consistent revenue history",
            highlights="6-year average gross over $240K, established customer base, prime SF location",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.50
        ))

        self.listings.append(LaundryListingComplete(
            listing_id="CL-IL-001",
            business_name="Wheeling Laundromat & Real Estate",
            street_address="Wheeling, IL",
            city="Wheeling",
            state="IL",
            zip_code="",
            full_address="Wheeling, IL",
            asking_price="$375,000",
            asking_price_numeric=375000.0,
            years_established="Established 1970s (early)",
            real_estate_included="Yes",
            property_type="Building + 3-bedroom apartment + parking lot",
            business_type="Turn-key",
            listing_date="2025",
            source_platform="Craigslist",
            source_url="https://chicago.craigslist.org/nwc/bfs/d/wheeling-turn-key-laundromat-and-real/7829594940.html",
            listing_status="Active",
            description="Turn-key laundromat established in early 1970s, includes real estate: laundromat, upstairs 3-bedroom apartment, and adjacent paved parking lot",
            highlights="Includes building, apartment rental income, parking, established 50+ years",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.60
        ))

        self.listings.append(LaundryListingComplete(
            listing_id="CL-CA-002",
            business_name="Citrus Heights Laundromat",
            street_address="100 N. 1st St (nearby reference)",
            city="Citrus Heights",
            state="CA",
            zip_code="",
            county="Sacramento County",
            full_address="Citrus Heights, Sacramento area, CA",
            asking_price="$269,000",
            asking_price_numeric=269000.0,
            monthly_revenue="$6,700 average",
            gross_revenue_numeric=80400.0,  # Annual
            equipment_age="Purchased 2022",
            washer_brands="Dexter",
            dryer_brands="Dexter",
            equipment_condition="All new equipment",
            recent_upgrades="All new Dexter equipment purchased in 2022",
            listing_date="2025",
            source_platform="Craigslist",
            source_url="https://sacramento.craigslist.org/reo/d/sacramento-laundromat-citrus-heights/7817348740.html",
            listing_status="Active",
            description="Laundromat with all new Dexter equipment purchased in 2022, average monthly sales $6,700",
            highlights="New equipment (2022), $6.7K monthly sales, Sacramento market",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.70
        ))

        # =====================================================================
        # CHICAGO AREA LISTINGS (Multiple sources)
        # =====================================================================

        self.listings.append(LaundryListingComplete(
            listing_id="CHI-001",
            business_name="Albany Park Coin Laundry",
            street_address="3516 West Lawrence Ave",
            city="Chicago",
            state="IL",
            zip_code="60625",
            full_address="3516 West Lawrence Ave, Chicago, IL 60625",
            asking_price="$175,000",
            asking_price_numeric=175000.0,
            business_type="Coin laundry operation",
            listing_date="2025",
            source_platform="Multiple (BizBuySell, LoopNet)",
            listing_status="Active",
            description="Coin laundry operation in Albany Park neighborhood",
            highlights="Established location, residential area",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.45
        ))

        self.listings.append(LaundryListingComplete(
            listing_id="CHI-002",
            business_name="Bubble City Laundromat",
            street_address="1425 W. Morse Ave",
            city="Chicago",
            state="IL",
            zip_code="60626",
            full_address="1425 W. Morse Ave, Chicago, IL 60626",
            asking_price="$190,000",
            asking_price_numeric=190000.0,
            listing_date="2025",
            source_platform="Multiple",
            listing_status="Active",
            description="Laundromat in Rogers Park area",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.40
        ))

        self.listings.append(LaundryListingComplete(
            listing_id="CHI-003",
            business_name="Moonlight Coin Laundry",
            street_address="5304 W Fullerton Ave",
            city="Chicago",
            state="IL",
            zip_code="60639",
            full_address="5304 W Fullerton Ave, Chicago, IL 60639",
            asking_price="$170,000",
            asking_price_numeric=170000.0,
            business_type="Coin laundry",
            listing_date="2025",
            source_platform="Multiple",
            listing_status="Active",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.40
        ))

        self.listings.append(LaundryListingComplete(
            listing_id="CHI-004",
            business_name="Friendly Wash Laundromat",
            street_address="3858 N Kedzie Ave",
            city="Chicago",
            state="IL",
            zip_code="",
            full_address="3858 N Kedzie Ave, Chicago, IL",
            asking_price="$790,000",
            asking_price_numeric=790000.0,
            business_type="Established laundromat",
            listing_date="2025",
            source_platform="Multiple",
            listing_status="Active",
            description="Premium established laundromat in Chicago",
            highlights="High asking price indicates strong performance",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.40
        ))

        # =====================================================================
        # FACEBOOK MARKETPLACE LISTINGS
        # =====================================================================

        self.listings.append(LaundryListingComplete(
            listing_id="FB-CA-001",
            business_name="Campbell Laundromat & Pure Water Business",
            street_address="Campbell area",
            city="Campbell",
            state="CA",
            zip_code="",
            full_address="Campbell, CA (San Jose area)",
            asking_price="$300,000",
            asking_price_numeric=300000.0,
            number_of_washers="52",
            number_of_dryers="41",
            services_offered="Laundromat + Pure Water Business",
            listing_date="2025",
            source_platform="Facebook Marketplace",
            listing_status="Active",
            description="Laundromat with 52 washers and 41 dryers, includes pure water business",
            highlights="Large capacity (52W/41D), dual business model, Silicon Valley area",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.55
        ))

        self.listings.append(LaundryListingComplete(
            listing_id="FB-TX-001",
            business_name="Dallas Laundromat",
            street_address="Dallas area",
            city="Dallas",
            state="TX",
            zip_code="",
            full_address="Dallas, TX",
            asking_price="$210,000",
            asking_price_numeric=210000.0,
            equipment_condition="Most machines new, good condition",
            listing_date="2025",
            source_platform="Facebook Marketplace",
            listing_status="Active",
            description="Laundromat with mostly new machines in good condition",
            highlights="New equipment, Dallas market",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.45
        ))

        self.listings.append(LaundryListingComplete(
            listing_id="FB-NY-001",
            business_name="Sound Beach Laundromat & Property",
            street_address="Sound Beach",
            city="Sound Beach",
            state="NY",
            zip_code="",
            county="Suffolk County",
            full_address="Sound Beach, NY (Long Island)",
            asking_price="$1,395,000",
            asking_price_numeric=1395000.0,
            net_income="$168,000/year",
            net_income_numeric=168000.0,
            real_estate_included="Yes",
            property_type="Laundromat + Real Estate",
            listing_date="2025",
            source_platform="Facebook/Pesce Commercial",
            broker_name="Chris Pesce",
            broker_company="Pesce Commercial",
            listing_status="Active",
            description="Laundromat and property for sale, nets $168K per year",
            highlights="Includes real estate, strong net income $168K/year, Long Island location",
            financing_available="Yes",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.65
        ))

        self.listings.append(LaundryListingComplete(
            listing_id="FB-MO-001",
            business_name="Springfield Laundromat",
            street_address="Springfield area",
            city="Springfield",
            state="MO",
            zip_code="",
            full_address="Springfield, MO",
            square_footage="1,400 sq ft",
            real_estate_included="Yes",
            business_type="Fully operational coin laundromat",
            listing_date="2025",
            source_platform="Facebook Marketplace",
            listing_status="Active",
            description="Fully operational 1,400 square foot coin laundromat, includes real estate",
            highlights="Includes building, turnkey operation",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.45
        ))

        self.listings.append(LaundryListingComplete(
            listing_id="FB-TX-002",
            business_name="Bertram Self-Serve Laundromat",
            street_address="Bertram area",
            city="Bertram",
            state="TX",
            zip_code="",
            full_address="Bertram, TX",
            business_type="Self-serve, rent space model",
            building_owned_or_leased="Leased",
            listing_date="2025",
            source_platform="Facebook Marketplace",
            listing_status="Active",
            description="Self-serve laundromat business, rent the space and purchase established business",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.35
        ))

        # =====================================================================
        # MAJOR PORTFOLIO / SPECIAL LISTINGS
        # =====================================================================

        self.listings.append(LaundryListingComplete(
            listing_id="PORT-TN-001",
            business_name="Memphis Laundromat Portfolio (9 Locations)",
            street_address="Multiple locations",
            city="Memphis",
            state="TN",
            zip_code="",
            full_address="Memphis, TN - 9 locations",
            asking_price="Not Listed",
            gross_revenue="$3.3M trending for 2025",
            gross_revenue_numeric=3300000.0,
            number_of_washers="Multiple locations",
            equipment_age="Less than 1 year old",
            equipment_condition="Most equipment less than 1 year old",
            business_type="Portfolio of 9 laundromats",
            listing_date="2025",
            source_platform="BizQuest",
            listing_status="Active",
            description="Portfolio of 9 laundromats in Memphis, TN with 2025 sales trending towards $3.3M revenue, most equipment less than 1 year old",
            highlights="9 locations, $3.3M revenue, new equipment, portfolio opportunity",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.60
        ))

        self.listings.append(LaundryListingComplete(
            listing_id="SPEC-TN-001",
            business_name="Knoxville Laundromat",
            street_address="Knoxville area",
            city="Knoxville",
            state="TN",
            zip_code="",
            full_address="Knoxville, TN",
            business_type="Well established coin laundry",
            reason_for_sale="Health reasons",
            listing_date="2025",
            source_platform="LaundromatsForSale.com",
            listing_status="Active",
            description="Well established coin laundry for sale due to health reasons",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.30
        ))

        # =====================================================================
        # SPECIALIZED/UNIQUE LISTINGS
        # =====================================================================

        self.listings.append(LaundryListingComplete(
            listing_id="SUNB-OH-001",
            business_name="Cleveland Coinless Laundromat",
            street_address="Cleveland area",
            city="Cleveland",
            state="OH",
            zip_code="",
            full_address="Cleveland, OH",
            asking_price="Down payment $350,000",
            gross_revenue="$342,000/year",
            gross_revenue_numeric=342000.0,
            card_system="Coinless (card system)",
            financing_available="Yes",
            seller_financing="Yes - $350K down",
            listing_date="2025",
            source_platform="Sunbelt Network",
            listing_status="Active",
            description="Coinless laundromat making $342,000/year, seller financing available with $350K down",
            highlights="Card system, strong revenue, seller financing",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.55
        ))

        self.listings.append(LaundryListingComplete(
            listing_id="AK-001",
            business_name="Homer Alaska Laundromat",
            street_address="Homer",
            city="Homer",
            state="AK",
            zip_code="",
            full_address="Homer, AK",
            number_of_washers="37",
            number_of_dryers="33",
            years_established="35+ years",
            real_estate_included="Yes",
            property_type="Land, building, business, all equipment",
            services_offered="Coin laundry, wash-dry-fold, dry cleaning pickup/dropoff, showers",
            listing_date="2025",
            source_platform="BusinessMart",
            contact_method="wht6mtn@gmail.com",
            listing_status="Active",
            description="35+ year established laundromat in Homer, Alaska with 37 washers, 33 dryers, includes land, building, business and all equipment. Services: coin laundry, wash-dry-fold, dry cleaning pickup/dropoff, showers",
            highlights="Alaska location, 35+ years established, includes real estate, multiple services",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.70
        ))

        self.listings.append(LaundryListingComplete(
            listing_id="WY-001",
            business_name="Cheyenne Laundromat & Salon",
            street_address="900 W. Lincolnway",
            city="Cheyenne",
            state="WY",
            zip_code="82001",
            full_address="900 W. Lincolnway, Cheyenne, WY 82001",
            number_of_washers="42",
            number_of_dryers="26",
            years_established="70 years",
            square_footage="720 sq ft retail space (salon)",
            real_estate_included="Yes (lot included)",
            property_type="Building + lot",
            additional_equipment="Various laundry equipment",
            services_offered="Laundromat + retail space (currently salon)",
            broker_phone="307-331-7285",
            broker_name="Paula",
            listing_date="2025",
            source_platform="Multiple",
            listing_status="Active",
            description="Laundromat in business for 70 years with 42 washers, 26 dryers, various equipment. Includes 720 sq ft retail space currently set up as salon with separate entrance. Lot included in sale.",
            highlights="70 years in business, includes building + lot, dual income (laundry + salon rental)",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.75
        ))

        # =====================================================================
        # CREXI COMMERCIAL REAL ESTATE LISTINGS
        # =====================================================================

        self.listings.append(LaundryListingComplete(
            listing_id="CREXI-CA-001",
            business_name="Pearl Senter Laundromat",
            street_address="2266 Senter Road",
            city="San Jose",
            state="CA",
            zip_code="",
            full_address="2266 Senter Road, San Jose, CA",
            property_type="Commercial laundromat property",
            demographics="Busy area across from Costco, surrounded by high-density apartments",
            listing_date="2025",
            source_platform="Crexi",
            listing_status="Active",
            description="Laundromat in busy area across from Costco, surrounded by high-density apartments",
            highlights="High-traffic location, Costco proximity, dense residential area",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.45
        ))

        self.listings.append(LaundryListingComplete(
            listing_id="CREXI-SC-001",
            business_name="Greenville Laundromat",
            street_address="Greenville area",
            city="Greenville",
            state="SC",
            zip_code="",
            full_address="Greenville, SC",
            washer_brands="Continental",
            dryer_brands="Continental",
            equipment_condition="Commercial grade",
            listing_date="2025",
            source_platform="Crexi",
            listing_status="Active",
            description="Established laundromat with Continental commercial washers and dryers",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.35
        ))

        self.listings.append(LaundryListingComplete(
            listing_id="CREXI-GA-001",
            business_name="Eastman Laundromat",
            street_address="204 Griffin Ave",
            city="Eastman",
            state="GA",
            zip_code="31023",
            full_address="204 Griffin Ave, Eastman, GA 31023",
            square_footage="3,200 SF",
            property_type="0.27 acre",
            demographics="Near one of busiest intersections in town",
            real_estate_included="Yes",
            listing_date="2025",
            source_platform="Crexi",
            listing_status="Active",
            description="±3,200 SF established laundromat on 0.27 acre near one of the busiest intersections in town",
            highlights="Prime location, includes land, high traffic area",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.50
        ))

        self.listings.append(LaundryListingComplete(
            listing_id="CREXI-PA-001",
            business_name="Reading Laundromat Package (4 Locations)",
            street_address="Multiple locations",
            city="Reading",
            state="PA",
            zip_code="",
            full_address="Reading, PA - 4 locations",
            business_type="Package deal - 4 laundromat locations",
            listing_date="2025",
            source_platform="Crexi",
            listing_status="Active",
            description="Package deal of 4 laundromat locations in Reading, PA",
            highlights="Portfolio opportunity, 4 locations, single purchase",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.35
        ))

        self.listings.append(LaundryListingComplete(
            listing_id="CREXI-PA-002",
            business_name="Philadelphia Laundromat Portfolio (3 Locations)",
            street_address="5650 Rising Sun Ave + 2 others",
            city="Philadelphia",
            state="PA",
            zip_code="19120",
            full_address="5650 Rising Sun Ave, Philadelphia, PA 19120 + 2 other locations",
            business_type="Portfolio of 3 laundromats",
            listing_date="2025",
            source_platform="Crexi",
            listing_status="Active",
            description="Portfolio of three laundromats for sale in Philadelphia",
            highlights="3 locations, Philadelphia market, portfolio deal",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.40
        ))

        self.listings.append(LaundryListingComplete(
            listing_id="CREXI-WA-001",
            business_name="Lake Chelan 24-Hour Laundromat",
            street_address="84 Wapato Way",
            city="Manson",
            state="WA",
            zip_code="",
            full_address="84 Wapato Way, Manson, WA (Lake Chelan area)",
            gross_revenue="$60,000/year",
            gross_revenue_numeric=60000.0,
            hours_of_operation="24 hours",
            business_type="Self-service, 24-hour",
            financing_available="Yes",
            seller_financing="Yes",
            listing_date="2025",
            source_platform="Crexi",
            listing_status="Active",
            description="24-hour self-service laundromat generating $60K annually, seller financing available",
            highlights="24-hour operation, $60K revenue, seller financing, tourist area",
            verified=True,
            verification_date="2025-10-31",
            data_completeness_score=0.60
        ))

    def calculate_completeness_score(self, listing: LaundryListingComplete) -> float:
        """Calculate data completeness percentage"""
        fields = asdict(listing)
        total_fields = len(fields)
        filled_fields = sum(1 for v in fields.values() if v and v != "" and v != 0.0 and v != "No" and v != False)
        return round(filled_fields / total_fields, 2)

    def export_to_csv(self, filename: str = "laundromat_listings_complete.csv"):
        """Export all listings to CSV"""
        if not self.listings:
            print("No listings to export")
            return

        # Update completeness scores
        for listing in self.listings:
            listing.data_completeness_score = self.calculate_completeness_score(listing)

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = list(asdict(self.listings[0]).keys())
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for listing in self.listings:
                writer.writerow(asdict(listing))

        print(f"✓ Exported {len(self.listings)} listings to {filename}")

    def export_to_json(self, filename: str = "laundromat_listings_complete.json"):
        """Export all listings to JSON"""
        if not self.listings:
            print("No listings to export")
            return

        # Update completeness scores
        for listing in self.listings:
            listing.data_completeness_score = self.calculate_completeness_score(listing)

        data = {
            "metadata": {
                "export_date": datetime.now().isoformat(),
                "total_listings": len(self.listings),
                "verified_listings": sum(1 for l in self.listings if l.verified),
                "average_completeness": round(sum(l.data_completeness_score for l in self.listings) / len(self.listings), 2),
                "states_covered": len(set(l.state for l in self.listings)),
                "platforms_sourced": len(set(l.source_platform for l in self.listings)),
            },
            "listings": [asdict(listing) for listing in self.listings]
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

        print(f"✓ Exported {len(self.listings)} listings to {filename}")

    def generate_summary_report(self):
        """Generate comprehensive summary report"""
        total = len(self.listings)
        verified = sum(1 for l in self.listings if l.verified)
        avg_completeness = round(sum(l.data_completeness_score for l in self.listings) / total, 2) if total > 0 else 0

        # Price statistics
        with_price = [l for l in self.listings if l.asking_price_numeric > 0]
        avg_price = sum(l.asking_price_numeric for l in with_price) / len(with_price) if with_price else 0
        min_price = min((l.asking_price_numeric for l in with_price), default=0)
        max_price = max((l.asking_price_numeric for l in with_price), default=0)

        # Revenue statistics
        with_revenue = [l for l in self.listings if l.gross_revenue_numeric > 0]
        avg_revenue = sum(l.gross_revenue_numeric for l in with_revenue) / len(with_revenue) if with_revenue else 0

        # Geographic coverage
        states = set(l.state for l in self.listings)
        platforms = set(l.source_platform for l in self.listings)

        report = f"""
{'='*80}
VERIFIED LAUNDROMAT LISTINGS DATABASE - SUMMARY REPORT
{'='*80}

OVERVIEW
--------
Total Listings: {total}
Verified Listings: {verified} ({verified/total*100:.1f}%)
Average Data Completeness: {avg_completeness*100:.0f}%
States Covered: {len(states)}
Source Platforms: {len(platforms)}

FINANCIAL DATA
--------------
Listings with Price Data: {len(with_price)} ({len(with_price)/total*100:.1f}%)
Average Asking Price: ${avg_price:,.0f}
Price Range: ${min_price:,.0f} - ${max_price:,.0f}

Listings with Revenue Data: {len(with_revenue)} ({len(with_revenue)/total*100:.1f}%)
Average Annual Revenue: ${avg_revenue:,.0f}

GEOGRAPHIC DISTRIBUTION
-----------------------
States Represented: {', '.join(sorted(states))}

Most Listings by State:
"""

        # Count by state
        state_counts = {}
        for listing in self.listings:
            state_counts[listing.state] = state_counts.get(listing.state, 0) + 1

        for state, count in sorted(state_counts.items(), key=lambda x: x[1], reverse=True):
            report += f"  {state}: {count} listings\n"

        report += f"\nSOURCE PLATFORMS\n"
        report += f"----------------\n"

        # Count by platform
        platform_counts = {}
        for listing in self.listings:
            platform_counts[listing.source_platform] = platform_counts.get(listing.source_platform, 0) + 1

        for platform, count in sorted(platform_counts.items(), key=lambda x: x[1], reverse=True):
            report += f"  {platform}: {count} listings\n"

        report += f"\nDATA QUALITY METRICS\n"
        report += f"--------------------\n"
        report += f"Listings with Full Address: {sum(1 for l in self.listings if l.full_address)}\n"
        report += f"Listings with Price: {len(with_price)}\n"
        report += f"Listings with Revenue: {len(with_revenue)}\n"
        report += f"Listings with Equipment Details: {sum(1 for l in self.listings if l.number_of_washers)}\n"
        report += f"Listings with Contact Info: {sum(1 for l in self.listings if l.broker_phone or l.broker_email or l.contact_method)}\n"
        report += f"Listings with Real Estate Included: {sum(1 for l in self.listings if l.real_estate_included == 'Yes')}\n"

        report += f"\nCOMPLETENESS BY LISTING\n"
        report += f"-----------------------\n"

        for listing in sorted(self.listings, key=lambda x: x.data_completeness_score, reverse=True)[:10]:
            report += f"  {listing.listing_id}: {listing.business_name:<40} {listing.data_completeness_score*100:.0f}% complete\n"

        report += f"\n{'='*80}\n"

        return report


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    print("\n" + "="*80)
    print("LAUNDROMAT LISTINGS DATABASE - VERIFIED DATA COMPILATION")
    print("="*80 + "\n")

    # Initialize database
    db = LaundryListingDatabase()

    print(f"✓ Loaded {len(db.listings)} verified listings\n")

    # Generate and display summary
    report = db.generate_summary_report()
    print(report)

    # Export to CSV
    db.export_to_csv()

    # Export to JSON
    db.export_to_json()

    print("\n✅ Database compilation complete!")
    print(f"   - {len(db.listings)} verified listings")
    print(f"   - CSV export: laundromat_listings_complete.csv")
    print(f"   - JSON export: laundromat_listings_complete.json")
    print()


if __name__ == "__main__":
    main()
