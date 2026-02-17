
"""
ANSI Blink Code Test
====================
Run this file in your terminal to see if blinking works.
Many modern terminals disable blink for accessibility.
"""

import time
import sys

def clear_line():
    """Clear current line"""
    print('\r\033[K', end='')

def test_static_blink():
    """Test static blinking text"""
    print("\n" + "="*70)
    print("STATIC BLINK TEST")
    print("="*70 + "\n")
    
    print("Code: print(\"\\033[6mRapid Blink\\033[0m\")")
    print("Output: \033[6mRapid Blink\033[0m")
    print()
    
    print("Slow Blink (Code 5):")
    print("\033[5m⚠ This should blink slowly\033[0m")
    print()
    
    print("Rapid Blink (Code 6):")
    print("\033[6m⚡ This should blink rapidly\033[0m")
    print()
    
    print("Colored Blink:")
    print("\033[5;31m🔴 Red Slow Blink\033[0m")
    print("\033[6;32m🟢 Green Rapid Blink\033[0m")
    print("\033[5;33m🟡 Yellow Slow Blink\033[0m")
    print()

def test_animated():
    """Test animated effects without ANSI blink"""
    print("\n" + "="*70)
    print("ANIMATED ALTERNATIVE (Works in all terminals)")
    print("="*70 + "\n")
    
    print("Press Ctrl+C to stop...\n")
    
    try:
        # Spinner
        spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        for _ in range(30):
            for frame in spinner:
                print(f'\r\033[36m{frame} Loading...\033[0m', end='', flush=True)
                time.sleep(0.1)
        print('\r\033[K', end='')
        
        # Pulse effect
        print("\n\033[1mPulse Effect:\033[0m")
        for i in range(10):
            intensity = abs(5 - i)
            print(f'\r\033[9{intensity}m● Status\033[0m', end='', flush=True)
            time.sleep(0.2)
        print('\r\033[K', end='')
        
        # Blinking simulation
        print("\n\033[1mBlink Simulation:\033[0m")
        for _ in range(10):
            print('\r\033[1;31m⚠ ALERT!\033[0m', end='', flush=True)
            time.sleep(0.5)
            print('\r' + ' '*10, end='', flush=True)
            time.sleep(0.5)
        print('\r\033[K', end='')
        
        print("\n\n\033[92m✓ Animation complete!\033[0m\n")
        
    except KeyboardInterrupt:
        print('\r\033[K\n\n\033[93m⚠ Animation stopped.\033[0m\n')

def test_all_styles():
    """Test all text styles"""
    print("\n" + "="*70)
    print("ALL ANSI TEXT STYLES")
    print("="*70 + "\n")
    
    styles = [
        ("Normal", "\033[0m", "Normal text"),
        ("Bold", "\033[1m", "Bold text"),
        ("Dim", "\033[2m", "Dim text"),
        ("Italic", "\033[3m", "Italic text"),
        ("Underline", "\033[4m", "Underline text"),
        ("Slow Blink", "\033[5m", "Slow blink text"),
        ("Rapid Blink", "\033[6m", "Rapid blink text"),
        ("Reverse", "\033[7m", "Reverse text"),
        ("Hidden", "\033[8m", "Hidden text (you can't see this)"),
        ("Strikethrough", "\033[9m", "Strikethrough text"),
    ]
    
    for name, code, sample in styles:
        print(f"{name:15} → {code}{sample}\033[0m")

def practical_examples():
    """Show practical use cases"""
    print("\n" + "="*70)
    print("PRACTICAL EXAMPLES")
    print("="*70 + "\n")
    
    print("1. Status Messages:")
    print("   \033[92m✓ Success\033[0m - Operation completed")
    print("   \033[5;93m⚠ Warning\033[0m - \033[5;1mImmediate action required\033[0m")
    print("   \033[91m✗ Error\033[0m - Something went wrong")
    print("   \033[96mℹ Info\033[0m - For your information")
    print()
    
    print("2. Progress Indicators:")
    bar = "█" * 15 + "░" * 15
    print(f"   \033[92m{bar}\033[0m 50%")
    print()
    
    print("3. Alerts:")
    print("   \033[1;4;5;31m!!! CRITICAL SYSTEM ALERT !!!\033[0m")
    print("   \033[6;7;33m>>> ATTENTION REQUIRED <<<\033[0m")
    print()
    
    print("4. Menu:")
    print("   \033[1;36m┌─────────────────────┐\033[0m")
    print("   \033[1;36m│\033[0m  1. Start         \033[1;36m│\033[0m")
    print("   \033[1;36m│\033[0m  2. Stop          \033[1;36m│\033[0m")
    print("   \033[1;36m│\033[0m  3. \033[5mExit\033[0m          \033[1;36m│\033[0m")
    print("   \033[1;36m└─────────────────────┘\033[0m")

def main():
    """Main test runner"""
    print("\n╔═══════════════════════════════════════════════════════════════════╗")
    print("║              ANSI BLINK CODE - LIVE OUTPUT TEST                   ║")
    print("╚═══════════════════════════════════════════════════════════════════╝")
    
    # Run tests
    test_static_blink()
    test_all_styles()
    practical_examples()
    
    # Ask if user wants to see animation
    print("\n" + "="*70)
    print("\nWould you like to see animated alternatives? (y/n): ", end="")
    try:
        response = input().strip().lower()
        if response == 'y':
            test_animated()
    except (KeyboardInterrupt, EOFError):
        print("\n")
    
    print("\n" + "="*70)
    print("⚠ IMPORTANT NOTES:")
    print("="*70)
    print("1. Blink codes (\\033[5m and \\033[6m) are part of the ANSI standard")
    print("2. Many modern terminals DISABLE blink for accessibility reasons")
    print("3. If you don't see blinking, your terminal doesn't support it")
    print("4. Try running this in different terminals:")
    print("   - Linux: xterm, gnome-terminal, konsole")
    print("   - macOS: Terminal.app, iTerm2")
    print("   - Windows: Windows Terminal, ConEmu")
    print("5. Use animated alternatives for better cross-terminal support")
    print("="*70 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[93mTest interrupted.\033[0m\n")
        sys.exit(0)