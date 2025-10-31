#!/usr/bin/env python3
"""
Enhanced Laundromat Listings Database
Adds calculated metrics, market insights, and derived fields
"""

import json
import csv
from datetime import datetime
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict, field

# Import the original database
import sys
sys.path.append('/home/user/Laundie')
from compile_verified_listings import LaundryListingComplete, LaundryListingDatabase


class EnhancedListingCalculator:
    """Calculate additional business metrics and insights"""

    # Industry standard metrics
    INDUSTRY_AVERAGE_PROFIT_MARGIN = 0.35  # 35% profit margin
    INDUSTRY_AVERAGE_REVENUE_PER_WASHER = 4000  # $4,000/year per washer
    INDUSTRY_AVERAGE_PRICE_TO_REVENUE = 1.6  # 1.6x revenue multiple
    INDUSTRY_AVERAGE_PRICE_TO_EARNINGS = 4.3  # 4.3x earnings multiple

    # Regional market data (simplified)
    REGIONAL_DEMOGRAPHICS = {
        "NY": {"population_density": "Very High", "market_maturity": "Mature", "competition": "High"},
        "CA": {"population_density": "High", "market_maturity": "Mature", "competition": "High"},
        "TX": {"population_density": "Medium-High", "market_maturity": "Growing", "competition": "Medium"},
        "IL": {"population_density": "High", "market_maturity": "Mature", "competition": "Medium-High"},
        "PA": {"population_density": "Medium-High", "market_maturity": "Mature", "competition": "Medium"},
        "OH": {"population_density": "Medium", "market_maturity": "Mature", "competition": "Medium"},
        "FL": {"population_density": "High", "market_maturity": "Growing", "competition": "High"},
        "GA": {"population_density": "Medium", "market_maturity": "Growing", "competition": "Medium"},
        "TN": {"population_density": "Medium", "market_maturity": "Growing", "competition": "Low-Medium"},
        "MO": {"population_density": "Medium", "market_maturity": "Mature", "competition": "Medium"},
        "SC": {"population_density": "Medium", "market_maturity": "Growing", "competition": "Low-Medium"},
        "WA": {"population_density": "Medium-High", "market_maturity": "Mature", "competition": "Medium"},
        "AK": {"population_density": "Very Low", "market_maturity": "Established", "competition": "Low"},
        "WY": {"population_density": "Very Low", "market_maturity": "Established", "competition": "Very Low"},
    }

    @staticmethod
    def calculate_price_to_revenue_multiple(price: float, revenue: float) -> Optional[float]:
        """Calculate price-to-revenue multiple"""
        if price > 0 and revenue > 0:
            return round(price / revenue, 2)
        return None

    @staticmethod
    def calculate_price_to_earnings_multiple(price: float, earnings: float) -> Optional[float]:
        """Calculate price-to-earnings (P/E) multiple"""
        if price > 0 and earnings > 0:
            return round(price / earnings, 2)
        return None

    @staticmethod
    def calculate_profit_margin(revenue: float, earnings: float) -> Optional[float]:
        """Calculate profit margin percentage"""
        if revenue > 0 and earnings > 0:
            return round((earnings / revenue) * 100, 1)
        return None

    @staticmethod
    def calculate_estimated_roi(price: float, net_income: float) -> Optional[float]:
        """Calculate simple ROI (annual net income / purchase price)"""
        if price > 0 and net_income > 0:
            return round((net_income / price) * 100, 1)
        return None

    @staticmethod
    def calculate_payback_period(price: float, net_income: float) -> Optional[float]:
        """Calculate payback period in years"""
        if price > 0 and net_income > 0:
            return round(price / net_income, 1)
        return None

    @staticmethod
    def estimate_annual_revenue_from_equipment(washers: int, dryers: int) -> Optional[float]:
        """Estimate revenue based on equipment count (industry averages)"""
        if washers > 0:
            # Average $4,000/year per washer
            estimated_revenue = washers * 4000
            return round(estimated_revenue, 0)
        return None

    @staticmethod
    def infer_business_hours(business_type: str, hours: str) -> str:
        """Infer typical business hours if not specified"""
        if hours and hours.strip():
            return hours
        if "24" in hours.lower() or "24-hour" in business_type.lower():
            return "24 hours"
        # Default assumption for laundromats
        return "6 AM - 10 PM daily (typical)"

    @staticmethod
    def infer_owner_involvement(business_type: str) -> str:
        """Infer owner involvement level"""
        business_lower = business_type.lower()
        if "absentee" in business_lower:
            return "Absentee (minimal involvement)"
        elif "semi-absentee" in business_lower:
            return "Semi-absentee (part-time)"
        elif "self-serve" in business_lower or "coin" in business_lower:
            return "Low (self-service operation)"
        return "Variable (depends on operation)"

    @staticmethod
    def get_regional_insights(state: str) -> Dict[str, str]:
        """Get regional market insights"""
        return EnhancedListingCalculator.REGIONAL_DEMOGRAPHICS.get(
            state,
            {"population_density": "N/A", "market_maturity": "N/A", "competition": "N/A"}
        )


class EnhancedLaundryDatabase:
    """Enhanced database with calculated metrics"""

    def __init__(self):
        # Load original database
        self.original_db = LaundryListingDatabase()
        self.enhanced_listings = []
        self.calculator = EnhancedListingCalculator()

        # Enhance each listing
        self._enhance_all_listings()

    def _enhance_all_listings(self):
        """Add calculated fields to all listings"""
        for listing in self.original_db.listings:
            enhanced = self._enhance_single_listing(listing)
            self.enhanced_listings.append(enhanced)

    def _enhance_single_listing(self, listing: LaundryListingComplete) -> Dict[str, Any]:
        """Enhance a single listing with calculated metrics"""
        # Convert to dict
        enhanced = asdict(listing)

        # Add calculated financial metrics
        if listing.asking_price_numeric > 0 and listing.gross_revenue_numeric > 0:
            enhanced['price_to_revenue_multiple'] = self.calculator.calculate_price_to_revenue_multiple(
                listing.asking_price_numeric, listing.gross_revenue_numeric
            )
        else:
            enhanced['price_to_revenue_multiple'] = None

        if listing.asking_price_numeric > 0 and listing.net_income_numeric > 0:
            enhanced['price_to_earnings_multiple'] = self.calculator.calculate_price_to_earnings_multiple(
                listing.asking_price_numeric, listing.net_income_numeric
            )
            enhanced['estimated_roi_percent'] = self.calculator.calculate_estimated_roi(
                listing.asking_price_numeric, listing.net_income_numeric
            )
            enhanced['payback_period_years'] = self.calculator.calculate_payback_period(
                listing.asking_price_numeric, listing.net_income_numeric
            )
        else:
            enhanced['price_to_earnings_multiple'] = None
            enhanced['estimated_roi_percent'] = None
            enhanced['payback_period_years'] = None

        if listing.gross_revenue_numeric > 0 and listing.net_income_numeric > 0:
            enhanced['profit_margin_percent'] = self.calculator.calculate_profit_margin(
                listing.gross_revenue_numeric, listing.net_income_numeric
            )
        else:
            enhanced['profit_margin_percent'] = None

        # Estimate revenue from equipment if not provided
        if not listing.gross_revenue_numeric or listing.gross_revenue_numeric == 0:
            try:
                washers = int(listing.number_of_washers) if listing.number_of_washers else 0
                dryers = int(listing.number_of_dryers) if listing.number_of_dryers else 0
                if washers > 0:
                    enhanced['estimated_revenue_from_equipment'] = self.calculator.estimate_annual_revenue_from_equipment(
                        washers, dryers
                    )
                else:
                    enhanced['estimated_revenue_from_equipment'] = None
            except (ValueError, TypeError):
                enhanced['estimated_revenue_from_equipment'] = None
        else:
            enhanced['estimated_revenue_from_equipment'] = None

        # Add regional insights
        regional = self.calculator.get_regional_insights(listing.state)
        enhanced['market_population_density'] = regional['population_density']
        enhanced['market_maturity'] = regional['market_maturity']
        enhanced['market_competition_level'] = regional['competition']

        # Infer operational details
        enhanced['inferred_hours'] = self.calculator.infer_business_hours(
            listing.business_type, listing.hours_of_operation
        )
        enhanced['inferred_owner_involvement'] = self.calculator.infer_owner_involvement(
            listing.business_type
        )

        # Add value assessment
        enhanced['value_assessment'] = self._assess_value(enhanced, listing)

        # Calculate enhanced completeness (with new fields)
        total_fields = len(enhanced)
        filled_fields = sum(1 for v in enhanced.values() if v not in [None, "", 0, 0.0, "No", False, "N/A"])
        enhanced['enhanced_completeness_score'] = round(filled_fields / total_fields, 2)

        return enhanced

    def _assess_value(self, enhanced: Dict, listing: LaundryListingComplete) -> str:
        """Provide a value assessment based on available metrics"""
        assessments = []

        # Check price-to-revenue multiple
        if enhanced.get('price_to_revenue_multiple'):
            multiple = enhanced['price_to_revenue_multiple']
            if multiple < 1.3:
                assessments.append("Strong value (low price-to-revenue)")
            elif multiple < 1.8:
                assessments.append("Fair value (market rate)")
            else:
                assessments.append("Premium pricing (high multiple)")

        # Check ROI
        if enhanced.get('estimated_roi_percent'):
            roi = enhanced['estimated_roi_percent']
            if roi > 20:
                assessments.append("Excellent ROI (>20%)")
            elif roi > 12:
                assessments.append("Good ROI (12-20%)")
            else:
                assessments.append("Moderate ROI (<12%)")

        # Check payback period
        if enhanced.get('payback_period_years'):
            payback = enhanced['payback_period_years']
            if payback < 4:
                assessments.append("Fast payback (<4 years)")
            elif payback < 6:
                assessments.append("Moderate payback (4-6 years)")
            else:
                assessments.append("Long payback (>6 years)")

        # Special features
        if listing.real_estate_included == "Yes":
            assessments.append("Includes real estate (asset value)")

        if "new" in listing.equipment_condition.lower():
            assessments.append("New equipment (low capex)")

        if listing.years_established and "year" in listing.years_established.lower():
            assessments.append("Established business (stable)")

        if not assessments:
            return "Insufficient data for valuation"

        return "; ".join(assessments)

    def export_enhanced_csv(self, filename: str = "laundromat_listings_enhanced.csv"):
        """Export enhanced listings to CSV"""
        if not self.enhanced_listings:
            print("No listings to export")
            return

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = list(self.enhanced_listings[0].keys())
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for listing in self.enhanced_listings:
                writer.writerow(listing)

        print(f"✓ Exported {len(self.enhanced_listings)} enhanced listings to {filename}")

    def export_enhanced_json(self, filename: str = "laundromat_listings_enhanced.json"):
        """Export enhanced listings to JSON"""
        if not self.enhanced_listings:
            print("No listings to export")
            return

        # Calculate aggregate statistics
        with_price = [l for l in self.enhanced_listings if l['asking_price_numeric'] > 0]
        with_revenue = [l for l in self.enhanced_listings if l['gross_revenue_numeric'] > 0]
        with_roi = [l for l in self.enhanced_listings if l['estimated_roi_percent']]

        data = {
            "metadata": {
                "export_date": datetime.now().isoformat(),
                "total_listings": len(self.enhanced_listings),
                "verified_listings": sum(1 for l in self.enhanced_listings if l['verified']),
                "enhanced_with_calculations": True,
                "average_enhanced_completeness": round(
                    sum(l['enhanced_completeness_score'] for l in self.enhanced_listings) / len(self.enhanced_listings), 2
                ),
                "listings_with_price": len(with_price),
                "listings_with_revenue": len(with_revenue),
                "listings_with_roi_calc": len(with_roi),
                "average_asking_price": round(sum(l['asking_price_numeric'] for l in with_price) / len(with_price), 0) if with_price else 0,
                "average_revenue": round(sum(l['gross_revenue_numeric'] for l in with_revenue) / len(with_revenue), 0) if with_revenue else 0,
                "average_roi_percent": round(sum(l['estimated_roi_percent'] for l in with_roi) / len(with_roi), 1) if with_roi else 0,
            },
            "listings": self.enhanced_listings
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

        print(f"✓ Exported {len(self.enhanced_listings)} enhanced listings to {filename}")

    def generate_enhanced_summary(self):
        """Generate enhanced summary report"""
        total = len(self.enhanced_listings)

        # Financial metrics
        with_price = [l for l in self.enhanced_listings if l['asking_price_numeric'] > 0]
        with_revenue = [l for l in self.enhanced_listings if l['gross_revenue_numeric'] > 0]
        with_roi = [l for l in self.enhanced_listings if l['estimated_roi_percent']]
        with_multiple = [l for l in self.enhanced_listings if l['price_to_revenue_multiple']]

        avg_price = sum(l['asking_price_numeric'] for l in with_price) / len(with_price) if with_price else 0
        avg_revenue = sum(l['gross_revenue_numeric'] for l in with_revenue) / len(with_revenue) if with_revenue else 0
        avg_roi = sum(l['estimated_roi_percent'] for l in with_roi) / len(with_roi) if with_roi else 0
        avg_multiple = sum(l['price_to_revenue_multiple'] for l in with_multiple) / len(with_multiple) if with_multiple else 0

        report = f"""
{'='*80}
ENHANCED LAUNDROMAT LISTINGS DATABASE - SUMMARY REPORT
{'='*80}

OVERVIEW
--------
Total Listings: {total}
Enhanced with Calculated Metrics: {total}
Average Enhanced Completeness: {sum(l['enhanced_completeness_score'] for l in self.enhanced_listings) / total:.1%}

FINANCIAL ANALYSIS
------------------
Listings with Price Data: {len(with_price)} ({len(with_price)/total*100:.1f}%)
Average Asking Price: ${avg_price:,.0f}

Listings with Revenue Data: {len(with_revenue)} ({len(with_revenue)/total*100:.1f}%)
Average Annual Revenue: ${avg_revenue:,.0f}

Listings with ROI Calculations: {len(with_roi)} ({len(with_roi)/total*100:.1f}%)
Average ROI: {avg_roi:.1f}%

Listings with Valuation Multiples: {len(with_multiple)} ({len(with_multiple)/total*100:.1f}%)
Average Price-to-Revenue Multiple: {avg_multiple:.2f}x

INVESTMENT QUALITY
------------------
"""

        # Categorize by ROI
        excellent_roi = [l for l in with_roi if l['estimated_roi_percent'] > 20]
        good_roi = [l for l in with_roi if 12 <= l['estimated_roi_percent'] <= 20]
        moderate_roi = [l for l in with_roi if l['estimated_roi_percent'] < 12]

        report += f"Excellent ROI (>20%): {len(excellent_roi)} listings\n"
        report += f"Good ROI (12-20%): {len(good_roi)} listings\n"
        report += f"Moderate ROI (<12%): {len(moderate_roi)} listings\n\n"

        # Categorize by payback period
        with_payback = [l for l in self.enhanced_listings if l['payback_period_years']]
        fast_payback = [l for l in with_payback if l['payback_period_years'] < 4]
        moderate_payback = [l for l in with_payback if 4 <= l['payback_period_years'] <= 6]
        long_payback = [l for l in with_payback if l['payback_period_years'] > 6]

        report += "PAYBACK PERIOD ANALYSIS\n"
        report += "-----------------------\n"
        report += f"Fast Payback (<4 years): {len(fast_payback)} listings\n"
        report += f"Moderate Payback (4-6 years): {len(moderate_payback)} listings\n"
        report += f"Long Payback (>6 years): {len(long_payback)} listings\n\n"

        # Real estate opportunities
        with_real_estate = [l for l in self.enhanced_listings if l['real_estate_included'] == 'Yes']
        report += f"REAL ESTATE INCLUDED: {len(with_real_estate)} listings\n"
        report += "=" * 80 + "\n\n"

        # Top opportunities by calculated metrics
        report += "TOP INVESTMENT OPPORTUNITIES (by ROI)\n"
        report += "-------------------------------------\n"
        top_roi = sorted(with_roi, key=lambda x: x['estimated_roi_percent'], reverse=True)[:10]
        for i, listing in enumerate(top_roi, 1):
            report += f"{i}. {listing['business_name']} ({listing['state']}) - {listing['estimated_roi_percent']:.1f}% ROI\n"
            report += f"   Price: ${listing['asking_price_numeric']:,.0f}, Net Income: ${listing['net_income_numeric']:,.0f}/year\n"

        report += "\n" + "=" * 80 + "\n"

        return report


def main():
    print("\n" + "="*80)
    print("ENHANCED LAUNDROMAT DATABASE - WITH CALCULATED METRICS")
    print("="*80 + "\n")

    # Initialize enhanced database
    db = EnhancedLaundryDatabase()

    print(f"✓ Loaded and enhanced {len(db.enhanced_listings)} verified listings\n")

    # Generate and display summary
    report = db.generate_enhanced_summary()
    print(report)

    # Export enhanced data
    db.export_enhanced_csv()
    db.export_enhanced_json()

    print("\n✅ Enhanced database compilation complete!")
    print(f"   - {len(db.enhanced_listings)} verified listings with calculated metrics")
    print(f"   - CSV export: laundromat_listings_enhanced.csv")
    print(f"   - JSON export: laundromat_listings_enhanced.json")
    print()


if __name__ == "__main__":
    main()
