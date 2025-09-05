#!/usr/bin/env python3
"""
Fix Unicode Encoding Issues - Replace emoji characters with text equivalents
"""

import re
from pathlib import Path

def fix_unicode_in_file(file_path):
    """Fix Unicode encoding issues in a Python file"""
    
    # Emoji to text replacements
    replacements = {
        '🚀': '[START]',
        '🔍': '[SEARCH]',
        '✅': '[SUCCESS]',
        '❌': '[ERROR]',
        '⚠️': '[WARNING]',
        '💰': '[SALARY]',
        '🔗': '[LINK]',
        '🌍': '[GLOBAL]',
        '☁️': '[CLOUD]',
        '🏢': '[COMPANY]',
        '🌟': '[FEATURED]',
        '🏭': '[BPO]',
        '📱': '[PLATFORM]',
        '🎯': '[ORGANIZE]',
        '🤖': '[BOT]',
        '📊': '[STATS]',
        '⏰': '[TIME]',
        '📅': '[SCHEDULE]',
        '📁': '[FOLDER]',
        '📋': '[LOG]',
        '🧪': '[TEST]',
        '🐍': '[PYTHON]',
        '🎉': '[COMPLETE]',
        '💡': '[TIP]',
        '🪟': '[WINDOWS]',
        '🐧': '[LINUX]',
        '🍎': '[MACOS]',
        '📝': '[MANUAL]',
        '💥': '[CRASH]',
        '🔬': '[RUNNING]',
        '🎯': '[TARGET]'
    }
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Track changes
        changes_made = 0
        
        # Replace emojis in print statements only
        for emoji, replacement in replacements.items():
            if emoji in content:
                # Only replace in print statements to preserve Telegram messages
                pattern = rf'(print\([^)]*){re.escape(emoji)}([^)]*\))'
                matches = re.findall(pattern, content)
                if matches:
                    content = re.sub(pattern, rf'\1{replacement}\2', content)
                    changes_made += len(matches)
        
        if changes_made > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed {changes_made} Unicode issues in {file_path}")
        else:
            print(f"No Unicode issues found in {file_path}")
            
        return changes_made
        
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return 0

def main():
    """Fix Unicode issues in all Python files"""
    print("Fixing Unicode encoding issues...")
    
    # Files to fix
    files_to_fix = [
        "telegram_jobs.py",
        "daily_job_scheduler.py",
        "setup_reliable_scheduler.py",
        "test_scheduler.py"
    ]
    
    total_fixes = 0
    
    for file_name in files_to_fix:
        file_path = Path(file_name)
        if file_path.exists():
            fixes = fix_unicode_in_file(file_path)
            total_fixes += fixes
        else:
            print(f"File not found: {file_name}")
    
    print(f"\nTotal fixes applied: {total_fixes}")
    print("Unicode encoding issues fixed!")

if __name__ == "__main__":
    main()