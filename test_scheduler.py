#!/usr/bin/env python3
"""
Test Scheduler - Test the daily job notification system
"""

import sys
import subprocess
from pathlib import Path
from datetime import datetime

def test_job_bot():
    """Test the main job bot"""
    print("[TEST] Testing main job bot...")
    try:
        result = subprocess.run([
            sys.executable, "telegram_jobs.py"
        ], capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            print("[SUCCESS] Job bot test successful!")
            print(f"[STATS] Output preview: {result.stdout[:200]}...")
            return True
        else:
            print("[ERROR] Job bot test failed!")
            print(f"Error: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("[TIME] Job bot test timed out")
        return False
    except Exception as e:
        print(f"[CRASH] Job bot test error: {e}")
        return False

def test_scheduler():
    """Test the scheduler system"""
    print("[TEST] Testing scheduler system...")
    try:
        # Import the scheduler to test dependencies
        from daily_job_scheduler import ReliableJobScheduler
        
        scheduler = ReliableJobScheduler()
        print("[SUCCESS] Scheduler imports successful!")
        
        # Test scheduler initialization
        if scheduler.job_script.exists():
            print("[SUCCESS] Job script found!")
        else:
            print("[ERROR] Job script not found!")
            return False
            
        print("[SUCCESS] Scheduler system test passed!")
        return True
        
    except ImportError as e:
        print(f"[ERROR] Missing dependency: {e}")
        print("[TIP] Run: pip install schedule")
        return False
    except Exception as e:
        print(f"[CRASH] Scheduler test error: {e}")
        return False

def check_environment():
    """Check the environment setup"""
    print("[SEARCH] Checking environment...")
    
    # Check Python version
    print(f"[PYTHON] Python version: {sys.version}")
    
    # Check required files
    required_files = [
        "telegram_jobs.py",
        "telegram_bot.py",
        "daily_job_scheduler.py",
        ".env"
    ]
    
    missing_files = []
    for file in required_files:
        if Path(file).exists():
            print(f"[SUCCESS] {file} found")
        else:
            print(f"[ERROR] {file} missing")
            missing_files.append(file)
    
    if missing_files:
        print(f"[WARNING] Missing files: {missing_files}")
        return False
    
    # Check dependencies
    try:
        import requests
        import schedule
        print("[SUCCESS] All dependencies available")
        return True
    except ImportError as e:
        print(f"[ERROR] Missing dependency: {e}")
        return False

def main():
    """Main test function"""
    print("[TEST] Agent-21 Scout Scheduler Test")
    print("=" * 40)
    print(f"[TIME] Test time: {datetime.now()}")
    print(f"[FOLDER] Working directory: {Path.cwd()}")
    
    # Run tests
    tests = [
        ("Environment Check", check_environment),
        ("Scheduler System", test_scheduler),
        ("Job Bot", test_job_bot)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n[RUNNING] Running {test_name}...")
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"[CRASH] {test_name} crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 40)
    print("[STATS] TEST RESULTS SUMMARY")
    print("=" * 40)
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
        if result:
            passed += 1
    
    print(f"\n[TARGET] Tests passed: {passed}/{len(results)}")
    
    if passed == len(results):
        print("[COMPLETE] ALL TESTS PASSED!")
        print("[SUCCESS] Your daily job notifications are ready!")
        print("[TIME] You'll receive jobs at 6:00 AM every day")
    else:
        print("[WARNING] Some tests failed. Please fix issues before relying on daily notifications.")
    
    return passed == len(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)