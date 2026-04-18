"""
VS Code Terminal ANSI Test
Run this in VS Code's integrated terminal to see live effects
"""

print("\n" + "="*70)
print("🎨 VS CODE TERMINAL - ANSI LIVE TEST")
print("="*70 + "\n")

# Your specific blink code
print("1. RAPID BLINK CODE:")
print("   Code: \\033[6m")
print("   Live: \033[6mRapid Blink Text\033[0m")
print()

# All blink variations
print("2. ALL BLINK CODES:")
print("   Slow Blink (5):  \033[5m⚠ Blinking Warning\033[0m")
print("   Rapid Blink (6): \033[6m⚡ Blinking Alert\033[0m")
print()

# Text styles that WILL work in VS Code
print("3. STYLES THAT WORK IN VS CODE:")
print("   \033[1mBold\033[0m")
print("   \033[2mDim\033[0m")
print("   \033[3mItalic\033[0m")
print("   \033[4mUnderline\033[0m")
print("   \033[9mStrikethrough\033[0m")
print("   \033[7mReverse/Inverted\033[0m")
print()

# Colors that WILL work
print("4. COLORS (These definitely work!):")
print("   \033[31m● Red\033[0m")
print("   \033[32m● Green\033[0m")
print("   \033[33m● Yellow\033[0m")
print("   \033[34m● Blue\033[0m")
print("   \033[35m● Magenta\033[0m")
print("   \033[36m● Cyan\033[0m")
print()

# Bright colors
print("5. BRIGHT COLORS:")
print("   \033[91m● Bright Red\033[0m")
print("   \033[92m● Bright Green\033[0m")
print("   \033[93m● Bright Yellow\033[0m")
print("   \033[94m● Bright Blue\033[0m")
print("   \033[95m● Bright Magenta\033[0m")
print("   \033[96m● Bright Cyan\033[0m")
print()

# Background colors
print("6. BACKGROUND COLORS:")
print("   \033[41m Red BG \033[0m")
print("   \033[42m Green BG \033[0m")
print("   \033[43m Yellow BG \033[0m")
print("   \033[44m Blue BG \033[0m")
print()

# Combined styles
print("7. COMBINED STYLES:")
print("   \033[1;31mBold Red\033[0m")
print("   \033[4;32mUnderlined Green\033[0m")
print("   \033[1;4;33mBold Underlined Yellow\033[0m")
print("   \033[7;35mInverted Magenta\033[0m")
print()

# RGB colors (24-bit)
print("8. RGB TRUE COLOR:")
print("   \033[38;2;255;100;0mCustom Orange (RGB)\033[0m")
print("   \033[38;2;255;182;193mLight Pink (RGB)\033[0m")
print("   \033[38;2;70;130;180mSteel Blue (RGB)\033[0m")
print()

# Practical examples
print("9. PRACTICAL STATUS MESSAGES:")
print("   \033[1;92m✓ SUCCESS\033[0m - Operation completed")
print("   \033[1;93m⚠ WARNING\033[0m - Check this issue")
print("   \033[1;91m✗ ERROR\033[0m - Something failed")
print("   \033[1;96mℹ INFO\033[0m - Additional information")
print()

# Progress bar
print("10. PROGRESS BAR:")
progress = 65
bar_filled = "█" * (progress // 2)
bar_empty = "░" * (50 - progress // 2)
print(f"    \033[92m{bar_filled}{bar_empty}\033[0m {progress}%")
print()

# Box
print("11. COLORED BOX:")
print("    \033[36m╔════════════════════════════╗\033[0m")
print("    \033[36m║\033[0m  \033[1mVS Code Terminal Test\033[0m  \033[36m║\033[0m")
print("    \033[36m║\033[0m  All colors working! ✓     \033[36m║\033[0m")
print("    \033[36m╚════════════════════════════╝\033[0m")
print()

print("="*70)
print("📝 NOTE:")
print("   - VS Code terminal supports most ANSI codes")
print("   - Blink codes (5, 6) usually DON'T work (disabled by default)")
print("   - All colors and text styles WILL work perfectly")
print("   - RGB true color is fully supported")
print("="*70 + "\n")

# Interactive test
print("\n🔄 Want to test interactively? Try these commands:")
print("   1. Run this file: python vscode_test.py")
print("   2. Or in Python REPL: python3")
print("      >>> print('\\033[91mRed\\033[0m')")
print("      >>> print('\\033[1;4;92mBold Underline Green\\033[0m')")
print()