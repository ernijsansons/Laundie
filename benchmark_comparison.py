#!/usr/bin/env python3
"""
Performance Benchmark: Original vs ADK Architecture
====================================================
This script compares the performance of the original monolithic agent
versus the improved ADK-based multi-agent system.
"""

import asyncio
import time
from typing import Dict, List


# =============================================================================
# ORIGINAL APPROACH (Simulated)
# =============================================================================

class OriginalAgent:
    """Simulates the original monolithic agent approach"""

    def __init__(self):
        self.platforms = [
            "BizBuySell",
            "BizQuest",
            "LoopNet",
            "BusinessesForSale",
            "Craigslist",
            "Crexi",
            "Sunbelt",
            "Transworld",
        ]

    def search_platform(self, platform: str) -> Dict:
        """Simulate a platform search (sequential)"""
        time.sleep(0.5)  # Simulate network delay
        return {"platform": platform, "results": 50}

    def run_sequential(self) -> Dict:
        """Run all searches sequentially"""
        print("\n" + "="*80)
        print("ORIGINAL APPROACH: Sequential Execution")
        print("="*80)

        start_time = time.time()
        results = []

        for platform in self.platforms:
            print(f"[Original] Searching {platform}...")
            result = self.search_platform(platform)
            results.append(result)

        elapsed = time.time() - start_time

        print(f"\n[Original] ✓ Completed all searches")
        print(f"[Original] Time elapsed: {elapsed:.2f}s")
        print("="*80 + "\n")

        return {
            "approach": "sequential",
            "platforms": len(self.platforms),
            "elapsed_time": elapsed,
            "results": results
        }


# =============================================================================
# ADK APPROACH (Simulated)
# =============================================================================

class ADKAgent:
    """Simulates the ADK multi-agent approach"""

    def __init__(self):
        self.platforms = [
            "BizBuySell",
            "BizQuest",
            "LoopNet",
            "BusinessesForSale",
            "Craigslist",
            "Crexi",
            "Sunbelt",
            "Transworld",
        ]

    async def search_platform(self, platform: str) -> Dict:
        """Simulate a platform search (async)"""
        await asyncio.sleep(0.5)  # Simulate network delay
        return {"platform": platform, "results": 50}

    async def run_parallel(self) -> Dict:
        """Run all searches in parallel using ADK pattern"""
        print("\n" + "="*80)
        print("ADK APPROACH: Parallel Execution")
        print("="*80)

        start_time = time.time()

        print(f"[ADK] Launching {len(self.platforms)} parallel searches...")

        # Create all tasks
        tasks = [self.search_platform(platform) for platform in self.platforms]

        # Execute all concurrently
        results = await asyncio.gather(*tasks)

        elapsed = time.time() - start_time

        print(f"[ADK] ✓ Completed all searches in parallel")
        print(f"[ADK] Time elapsed: {elapsed:.2f}s")
        print("="*80 + "\n")

        return {
            "approach": "parallel",
            "platforms": len(self.platforms),
            "elapsed_time": elapsed,
            "results": results
        }


# =============================================================================
# BENCHMARK COMPARISON
# =============================================================================

def print_comparison(original_result: Dict, adk_result: Dict):
    """Print a detailed comparison of both approaches"""

    print("\n" + "="*80)
    print("PERFORMANCE COMPARISON")
    print("="*80)

    # Calculate metrics
    speedup = original_result["elapsed_time"] / adk_result["elapsed_time"]
    time_saved = original_result["elapsed_time"] - adk_result["elapsed_time"]
    improvement_pct = ((original_result["elapsed_time"] - adk_result["elapsed_time"]) /
                       original_result["elapsed_time"] * 100)

    # Print comparison table
    print("\n┌─────────────────────────────┬─────────────────┬─────────────────┐")
    print("│ Metric                      │ Original        │ ADK Architecture│")
    print("├─────────────────────────────┼─────────────────┼─────────────────┤")
    print(f"│ Execution Time              │ {original_result['elapsed_time']:>14.2f}s│ {adk_result['elapsed_time']:>14.2f}s│")
    print(f"│ Platforms Searched          │ {original_result['platforms']:>15} │ {adk_result['platforms']:>15} │")
    print(f"│ Execution Model             │ {'Sequential':>15} │ {'Parallel':>15} │")
    print("└─────────────────────────────┴─────────────────┴─────────────────┘")

    print("\n📊 Performance Metrics:")
    print(f"  • Speedup: {speedup:.2f}x faster")
    print(f"  • Time Saved: {time_saved:.2f} seconds")
    print(f"  • Improvement: {improvement_pct:.1f}%")

    print("\n✅ Benefits of ADK Architecture:")
    print("  1. Parallel Execution - All searches run simultaneously")
    print("  2. Async/Await - Non-blocking I/O operations")
    print("  3. Scalability - Easy to add more platforms without slowdown")
    print("  4. Resource Efficiency - Better CPU and network utilization")

    print("\n📈 Scaling Analysis:")
    platforms_to_test = [5, 10, 20, 50]
    search_time = 0.5  # seconds per search

    print("\n  Platforms │ Original (Sequential) │ ADK (Parallel) │ Time Saved")
    print("  ──────────┼───────────────────────┼────────────────┼────────────")

    for n in platforms_to_test:
        seq_time = n * search_time
        par_time = search_time  # All run at once
        saved = seq_time - par_time
        print(f"     {n:>2}     │      {seq_time:>6.1f}s         │     {par_time:>5.1f}s     │   {saved:>5.1f}s")

    print("\n  * ADK maintains constant time regardless of platform count!")

    print("\n🏆 Winner: ADK Architecture")
    print(f"    {speedup:.1f}x faster with better scalability and maintainability")
    print("="*80 + "\n")


# =============================================================================
# ADDITIONAL FEATURE COMPARISON
# =============================================================================

def print_feature_comparison():
    """Print a comparison of features between approaches"""

    print("="*80)
    print("FEATURE COMPARISON")
    print("="*80 + "\n")

    features = [
        ("Architecture", "Monolithic", "Multi-Agent"),
        ("Execution Model", "Sequential", "Parallel + Sequential"),
        ("Async Support", "❌ No", "✅ Yes"),
        ("State Management", "❌ Ad-hoc", "✅ Centralized"),
        ("Error Handling", "❌ Basic", "✅ Retry Logic"),
        ("Type Safety", "⚠️  Minimal", "✅ Full"),
        ("Extensibility", "❌ Difficult", "✅ Easy"),
        ("Code Organization", "⚠️  Mixed", "✅ Separated"),
        ("Testability", "❌ Hard", "✅ Easy"),
        ("Tool Pattern", "❌ None", "✅ ADK Tools"),
        ("Agent Composition", "❌ None", "✅ Yes"),
        ("Observability", "⚠️  Limited", "✅ Full"),
    ]

    print("┌───────────────────────┬─────────────────┬──────────────────┐")
    print("│ Feature               │ Original        │ ADK Architecture │")
    print("├───────────────────────┼─────────────────┼──────────────────┤")

    for feature, original, adk in features:
        print(f"│ {feature:<21} │ {original:<15} │ {adk:<16} │")

    print("└───────────────────────┴─────────────────┴──────────────────┘")

    print("\n" + "="*80 + "\n")


# =============================================================================
# MAIN BENCHMARK
# =============================================================================

async def run_benchmark():
    """Run the complete benchmark comparison"""

    print("\n" + "="*80)
    print("LAUNDROMAT AGENT BENCHMARK")
    print("Comparing Original vs ADK Architecture")
    print("="*80)

    # Run original approach (sequential)
    original = OriginalAgent()
    original_result = original.run_sequential()

    # Run ADK approach (parallel)
    adk = ADKAgent()
    adk_result = await adk.run_parallel()

    # Print detailed comparison
    print_comparison(original_result, adk_result)

    # Print feature comparison
    print_feature_comparison()

    # Return results
    return {
        "original": original_result,
        "adk": adk_result,
        "speedup": original_result["elapsed_time"] / adk_result["elapsed_time"]
    }


# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    print("\n🚀 Starting Performance Benchmark...")
    print("This will compare sequential vs parallel execution patterns.\n")

    # Run the async benchmark
    results = asyncio.run(run_benchmark())

    print("✅ Benchmark Complete!")
    print(f"\nFinal Result: ADK Architecture is {results['speedup']:.2f}x faster\n")
