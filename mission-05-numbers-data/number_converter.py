"""
Number Converter - Digital Detective Mission 5
Converts an input decimal (base-10) integer into binary (base-2)
and hexadecimal (base-16) representations.
"""

def main():
    print("=" * 45)
    print("   Digital Detective: Number Converter")
    print("=" * 45)
    
    user_input = input("Enter a positive decimal number: ").strip()
    
    try:
        decimal_val = int(user_input)
        if decimal_val < 0:
            print("Note: Working with absolute magnitude.")
            decimal_val = abs(decimal_val)
            
        binary_val = bin(decimal_val)
        hex_val = hex(decimal_val)
        
        print("\n--- Conversion Results ---")
        print(f"Decimal (Base 10):     {decimal_val}")
        print(f"Binary (Base 2):       {binary_val}  (Raw: {binary_val[2:]})")
        print(f"Hexadecimal (Base 16): {hex_val.upper()}  (Raw: {hex_val[2:].upper()})")
        print("=" * 45)
        
    except ValueError:
        print("Error: Please enter a valid decimal integer.")

if __name__ == "__main__":
    main()
