#!/usr/bin/env python3
"""
Quick Bot Test - Test if the job bot can run without errors
"""

import sys
import subprocess
import signal
from pathlib import Path

def test_bot_startup():
    """Test if the bot can start without Unicode errors"""
    try:
        # Start the bot process
        process = subprocess.Popen([
            sys.executable, "telegram_jobs.py"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Wait for 10 seconds to see if it starts properly
        try:
            stdout, stderr = process.communicate(timeout=10)
            
            if process.returncode == 0:
                print("[SUCCESS] Bot completed successfully!")
                return True
            else:
                print(f"[ERROR] Bot failed with return code {process.returncode}")
                if stderr:
                    print(f"Error details: {stderr[:200]}...")
                return False
                
        except subprocess.TimeoutExpired:
            # Bot is still running after 10 seconds, which means it started successfully
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
            
            print("[SUCCESS] Bot started successfully (terminated after 10s)")
            return True
            
    except Exception as e:
        print(f"[ERROR] Failed to start bot: {e}")
        return False

def main():
    """Main test function"""
    print("Quick Bot Test - Testing startup...")
    
    if not Path("telegram_jobs.py").exists():
        print("[ERROR] telegram_jobs.py not found!")
        return False
    
    success = test_bot_startup()
    
    if success:
        print("\n[COMPLETE] Bot test passed!")
        print("[SUCCESS] Your daily scheduler should work properly")
    else:
        print("\n[WARNING] Bot test failed!")
        print("[TIP] Check the error messages above")
    
    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)