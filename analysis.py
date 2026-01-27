#!/usr/bin/env python3
"""
Google Trends Investigation: Testing Hanania's "Origin of Woke" Model
=====================================================================
Event X: Trump Executive Order "Restoring Equality of Opportunity and Meritocracy"
               (April 23, 2025)
Construct Y: Institutional DEI salience / compliance activity
Geography: United States (US)

This script collects Google Trends data, computes pre/post statistics,
generates plots, and runs robustness checks for the QSS assignment.
"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from pytrends.request import TrendReq
import time
import os
import json

# ── Configuration ───────────────────────────────────────────────────
EVENT_DATE = pd.Timestamp('2025-04-23')
EVENT_LABEL = 'EO Signed\n(Apr 23, 2025)'
TIMEFRAME = '2020-04-01 2026-01-27'   # ~5 years before shock through present
GEO = 'US'
OUTPUT_DIR = 'output'

KEYWORDS = [
    'DEI',
    'HR',
    'unconscious bias',
    'structural racism',
]

# Topic mid → display label
TOPICS = {
    '/g/11sfpd6bdm': 'Diversity, equity, and inclusion (Topic)',
    '/m/020t58':     'Diversity training (Topic)',
}

# Robustness: synonym swap
SYNONYM_SWAP = {
    'original': 'structural racism',
    'synonym':  'systemic racism',
}

# Robustness: negative control (term that should NOT move with the event)
NEGATIVE_CONTROL = 'recipe ideas'

# Robustness: geography check
ALT_GEO = 'US-CA'   # California
ALT_GEO_LABEL = 'California'

# Robustness: window check (narrower 6-month window around the shock)
SHORT_TIMEFRAME = '2025-01-01 2026-01-27'   # 4 months before + 9 months after
SHORT_EVENT_DATE = EVENT_DATE

SLEEP = 3  # seconds between API calls

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Helper functions ────────────────────────────────────────────────

def fetch_trends(keywords, timeframe=TIMEFRAME, geo=GEO, sleep=SLEEP):
    """Fetch Google Trends data for a list of keywords/topic mids."""
    pytrends = TrendReq(hl='en-US', tz=360)
    all_data = {}
    for kw in keywords:
        pytrends.build_payload([kw], cat=0, timeframe=timeframe, geo=geo)
        df = pytrends.interest_over_time()
        if not df.empty:
            col = df.columns[0]
            all_data[kw] = df[col]
        else:
            print(f"  WARNING: No data for '{kw}' (timeframe={timeframe}, geo={geo})")
            all_data[kw] = pd.Series(dtype=float)
        time.sleep(sleep)
    return pd.DataFrame(all_data)


def pre_post_stats(series, event_date=EVENT_DATE):
    """Compute pre-mean, post-mean, peak near/after event."""
    pre = series[series.index < event_date]
    post = series[series.index >= event_date]
    pre_mean = pre.mean() if len(pre) > 0 else np.nan
    post_mean = post.mean() if len(post) > 0 else np.nan
    peak_post = post.max() if len(post) > 0 else np.nan
    peak_post_date = post.idxmax() if len(post) > 0 and not post.isna().all() else None
    return {
        'pre_mean': round(pre_mean, 2),
        'post_mean': round(post_mean, 2),
        'peak_post': int(peak_post) if not np.isnan(peak_post) else None,
        'peak_post_date': str(peak_post_date.date()) if peak_post_date is not None else None,
        'diff': round(post_mean - pre_mean, 2) if not (np.isnan(pre_mean) or np.isnan(post_mean)) else None,
        'ratio': round(post_mean / pre_mean, 3) if pre_mean and pre_mean > 0 else None,
        'n_pre': len(pre),
        'n_post': len(post),
    }


def plot_series(df, title, filename, event_date=EVENT_DATE, event_label=EVENT_LABEL):
    """Plot time series with vertical event line."""
    fig, ax = plt.subplots(figsize=(14, 6))
    for col in df.columns:
        ax.plot(df.index, df[col], linewidth=1.3, label=col, alpha=0.85)
    ax.axvline(event_date, color='red', linestyle='--', linewidth=2, alpha=0.7)
    ax.text(event_date, ax.get_ylim()[1] * 0.95, event_label,
            ha='center', va='top', fontsize=9, color='red',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.8))
    ax.set_title(title, fontsize=13, fontweight='bold')
    ax.set_xlabel('Date')
    ax.set_ylabel('Google Trends Index (0–100)')
    ax.legend(loc='upper left', fontsize=8)
    # Adapt axis formatting to time span
    span_days = (df.index[-1] - df.index[0]).days if len(df) > 1 else 30
    if span_days > 365:
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
        ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
    elif span_days > 60:
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
        ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))
    else:
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=3))
    plt.xticks(rotation=45)
    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  Saved plot: {path}")
    return path


def print_stats_table(stats_dict, label=''):
    """Pretty-print statistics table."""
    print(f"\n{'='*70}")
    print(f"  {label}")
    print(f"{'='*70}")
    print(f"{'Term':<35} {'Pre':>6} {'Post':>6} {'Peak':>5} {'Diff':>7} {'Ratio':>7}")
    print(f"{'-'*35} {'-'*6} {'-'*6} {'-'*5} {'-'*7} {'-'*7}")
    for term, s in stats_dict.items():
        pre_str = f"{s['pre_mean']:.1f}" if s['pre_mean'] is not None else 'N/A'
        post_str = f"{s['post_mean']:.1f}" if s['post_mean'] is not None else 'N/A'
        peak_str = f"{s['peak_post']}" if s['peak_post'] is not None else 'N/A'
        diff_str = f"{s['diff']:+.1f}" if s['diff'] is not None else 'N/A'
        ratio_str = f"{s['ratio']:.3f}" if s['ratio'] is not None else 'N/A'
        print(f"{term:<35} {pre_str:>6} {post_str:>6} {peak_str:>5} {diff_str:>7} {ratio_str:>7}")
    print()


# ── MAIN ANALYSIS ───────────────────────────────────────────────────

def main():
    results = {}   # will hold all results for JSON export

    # ── Q4/Q5: Keyword data ─────────────────────────────────────────
    print("\n" + "="*70)
    print("  COLLECTING KEYWORD DATA (Q4/Q5)")
    print("="*70)
    kw_df = fetch_trends(KEYWORDS)
    kw_df.to_csv(os.path.join(OUTPUT_DIR, 'keywords_data.csv'))

    kw_stats = {}
    for col in kw_df.columns:
        kw_stats[col] = pre_post_stats(kw_df[col])
    print_stats_table(kw_stats, label='KEYWORD STATISTICS (Q5)')
    results['keyword_stats'] = kw_stats

    plot_series(kw_df,
                'Google Trends: DEI-Related Keywords (US)\n'
                'Event: Trump EO "Restoring Equality of Opportunity and Meritocracy" (Apr 23, 2025)',
                'keywords_plot.png')

    # ── Q6: Topic data ──────────────────────────────────────────────
    print("\n" + "="*70)
    print("  COLLECTING TOPIC DATA (Q6)")
    print("="*70)
    topic_mids = list(TOPICS.keys())
    topic_labels = list(TOPICS.values())
    topic_df = fetch_trends(topic_mids)
    # Rename columns to human-readable labels
    topic_df.columns = [TOPICS.get(c, c) for c in topic_df.columns]
    topic_df.to_csv(os.path.join(OUTPUT_DIR, 'topics_data.csv'))

    topic_stats = {}
    for col in topic_df.columns:
        topic_stats[col] = pre_post_stats(topic_df[col])
    print_stats_table(topic_stats, label='TOPIC STATISTICS (Q6)')
    results['topic_stats'] = topic_stats

    plot_series(topic_df,
                'Google Trends: DEI-Related Topics (US)\n'
                'Event: Trump EO "Restoring Equality of Opportunity and Meritocracy" (Apr 23, 2025)',
                'topics_plot.png')

    # ── Q7: Ayers-lite effects ──────────────────────────────────────
    print("\n" + "="*70)
    print("  AYERS-LITE EFFECTS (Q7)")
    print("="*70)
    print("\n  Keywords:")
    for term, s in kw_stats.items():
        diff = s['diff']
        ratio = s['ratio']
        print(f"    {term}: post−pre = {diff:+.1f},  post/pre = {ratio:.3f}" if diff is not None and ratio is not None else f"    {term}: insufficient data")

    print("\n  Topics:")
    for term, s in topic_stats.items():
        diff = s['diff']
        ratio = s['ratio']
        print(f"    {term}: post−pre = {diff:+.1f},  post/pre = {ratio:.3f}" if diff is not None and ratio is not None else f"    {term}: insufficient data")

    results['ayers_lite'] = {
        'keywords': {k: {'diff': v['diff'], 'ratio': v['ratio']} for k, v in kw_stats.items()},
        'topics': {k: {'diff': v['diff'], 'ratio': v['ratio']} for k, v in topic_stats.items()},
    }

    # ── Q8: Robustness checks ──────────────────────────────────────
    print("\n" + "="*70)
    print("  ROBUSTNESS CHECKS (Q8)")
    print("="*70)

    # --- Check 1: Synonym swap ---
    print("\n  [Check 1] Synonym swap: replacing '{}' with '{}'".format(
        SYNONYM_SWAP['original'], SYNONYM_SWAP['synonym']))
    synonym_df = fetch_trends([SYNONYM_SWAP['original'], SYNONYM_SWAP['synonym']])
    synonym_stats = {}
    for col in synonym_df.columns:
        synonym_stats[col] = pre_post_stats(synonym_df[col])
    print_stats_table(synonym_stats, label='SYNONYM SWAP')
    synonym_df.to_csv(os.path.join(OUTPUT_DIR, 'robustness_synonym.csv'))
    plot_series(synonym_df,
                'Robustness: Synonym Swap\n'
                f'"{SYNONYM_SWAP["original"]}" vs "{SYNONYM_SWAP["synonym"]}"',
                'robustness_synonym_plot.png')
    results['robustness_synonym'] = synonym_stats

    # --- Check 2: Negative control ---
    print(f"\n  [Check 2] Negative control: '{NEGATIVE_CONTROL}'")
    neg_df = fetch_trends([NEGATIVE_CONTROL])
    neg_stats = {}
    for col in neg_df.columns:
        neg_stats[col] = pre_post_stats(neg_df[col])
    print_stats_table(neg_stats, label='NEGATIVE CONTROL')
    neg_df.to_csv(os.path.join(OUTPUT_DIR, 'robustness_negative_control.csv'))
    plot_series(neg_df,
                f'Robustness: Negative Control ("{NEGATIVE_CONTROL}")',
                'robustness_negative_control_plot.png')
    results['robustness_negative_control'] = neg_stats

    # --- Check 3: Window check (narrower window around the shock) ---
    print(f"\n  [Check 3] Window check: narrower window ({SHORT_TIMEFRAME})")
    short_df = fetch_trends(KEYWORDS, timeframe=SHORT_TIMEFRAME)
    short_stats = {}
    for col in short_df.columns:
        short_stats[col] = pre_post_stats(short_df[col], event_date=SHORT_EVENT_DATE)
    print_stats_table(short_stats, label=f'WINDOW CHECK ({SHORT_TIMEFRAME})')
    short_df.to_csv(os.path.join(OUTPUT_DIR, 'robustness_window.csv'))
    plot_series(short_df,
                f'Robustness: Narrower Window ({SHORT_TIMEFRAME})\n'
                'Event: Trump EO (Apr 23, 2025)',
                'robustness_window_plot.png')
    results['robustness_window'] = short_stats

    # ── Save all results as JSON ────────────────────────────────────
    # Convert any non-serializable types
    def clean_for_json(obj):
        if isinstance(obj, dict):
            return {k: clean_for_json(v) for k, v in obj.items()}
        if isinstance(obj, (np.integer,)):
            return int(obj)
        if isinstance(obj, (np.floating,)):
            return float(obj)
        if isinstance(obj, (np.ndarray,)):
            return obj.tolist()
        return obj

    with open(os.path.join(OUTPUT_DIR, 'results.json'), 'w') as f:
        json.dump(clean_for_json(results), f, indent=2, default=str)

    print(f"\n  All results saved to {OUTPUT_DIR}/results.json")
    print("  Analysis complete!\n")


if __name__ == '__main__':
    main()
