+"""Helper tool for Pigpen encoding and decoding.
+Run with: python pigpen_helper.py
+"""
+
+import string
+
+# Optional colors using colorama
+try:
+    from colorama import init, Fore, Style
+    init(autoreset=True)
+except Exception:
+    class _Dummy:
+        def __getattr__(self, name):
+            return ''
+    Fore = Style = _Dummy()
+
+
+def build_mappings():
+    """Return mappings between letters and Pigpen symbols."""
+    letters = list(string.ascii_uppercase)
+    symbols = [
+        # Tic-tac-toe grid without dots (A-I)
+        "┌", "┬", "┐",
+        "├", "┼", "┤",
+        "└", "┴", "┘",
+        # Same grid with dot (J-R)
+        "┌·", "┬·", "┐·",
+        "├·", "┼·", "┤·",
+        "└·", "┴·", "┘·",
+        # X-shapes (S-V)
+        "^", ">", "v", "<",
+        # X-shapes with dot (W-Z)
+        "^·", ">·", "v·", "<·",
+    ]
+    mapping = dict(zip(letters, symbols))
+    reverse = {v: k for k, v in mapping.items()}
+    return mapping, reverse
+
+
+def encode(text, mapping):
+    """Encode plaintext into Pigpen symbols."""
+    tokens = []
+    for ch in text:
+        up = ch.upper()
+        if up in mapping:
+            tokens.append(mapping[up])
+        elif ch == ' ':
+            tokens.append('')
+    return ' '.join(tokens)
+
+
+
+def decode(symbols, reverse):
+    """Decode Pigpen symbols into plaintext."""
+    parts = symbols.split(' ')
+    result = []
+    for p in parts:
+        if p == '':
+            result.append(' ')
+        elif p in reverse:
+            result.append(reverse[p])
+        else:
+            print(Fore.RED + f"Warning: symbol '{p}' not recognized." + Style.RESET_ALL)
+            result.append(p)
+    return ''.join(result)
+def caesar_shift(text, shift):
+    """Apply a Caesar shift to the text."""
+    result = []
+    for ch in text:
+        if ch.isalpha():
+            base = ord('A') if ch.isupper() else ord('a')
+            result.append(chr((ord(ch) - base + shift) % 26 + base))
+        else:
+            result.append(ch)
+    return ''.join(result)
+
+
+def frequency_analysis(text):
+    """Count how often each letter appears in text."""
+    counts = {}
+    for ch in text.upper():
+        if ch.isalpha():
+            counts[ch] = counts.get(ch, 0) + 1
+    return counts
+
+
+def brute_force_caesar(text):
+    """Try every Caesar shift and print the result."""
+    for s in range(26):
+        print(f"Shift {s:2}: {caesar_shift(text, s)}")
+
+
+def menu():
+    """Main user menu loop."""
+    mapping, reverse = build_mappings()
+    while True:
+        print(Fore.CYAN + "Pigpen Helper" + Style.RESET_ALL)
+        print("[1] Encode text with Pigpen")
+        print("[2] Decode text from Pigpen")
+        print("[3] Decode text from Pigpen then apply Caesar shift")
+        print("[4] Quit")
+        choice = input(Fore.YELLOW + "Choose an option: " + Style.RESET_ALL).strip()
+        if choice == '1':
+            plain = input("Enter plaintext: ")
+            print(encode(plain, mapping))
+        elif choice == '2':
+            cipher = input("Enter Pigpen (symbols separated by spaces): ")
+            print(decode(cipher, reverse))
+        elif choice == '3':
+            cipher = input("Enter Pigpen (symbols separated by spaces): ")
+            decoded = decode(cipher, reverse)
+            try:
+                n = int(input("Enter Caesar shift N: "))
+            except ValueError:
+                print(Fore.RED + "Invalid shift; using 0." + Style.RESET_ALL)
+                n = 0
+            print(caesar_shift(decoded, n))
+        elif choice == '4':
+            print("Bye!")
+            break
+        else:
+            print(Fore.RED + "Invalid option." + Style.RESET_ALL)
+        print()
+
+
+if __name__ == '__main__':
+    menu()
