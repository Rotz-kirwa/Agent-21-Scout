#!/usr/bin/env python3
"""
Debug Bot Error - Find the exact error in the job bot
"""

import sys
import traceback

try:
    from telegram_jobs import JobScout
    
    print("✅ Import successful")
    
    scout = JobScout()
    print("✅ JobScout instance created")
    
    # Try to run the daily scout
    scout.run_daily_scout()
    print("✅ Daily scout completed")
    
except Exception as e:
    print(f"❌ Error occurred: {e}")
    print("\nFull traceback:")
    traceback.print_exc()