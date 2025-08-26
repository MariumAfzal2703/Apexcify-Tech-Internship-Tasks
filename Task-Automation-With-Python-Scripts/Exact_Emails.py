import re

# 1. Email pattern (rule)
pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

# 2. Apni text file read karo
with open("simple.txt", "r") as f:
    text = f.read()

# 3. Regex se saari emails dhoondo
emails = re.findall(pattern, text)

# 4. Duplicate hatao aur sorting karo
unique_emails = sorted(set(emails))

# 5. Save new file mai likh do
with open("emails_only.txt", "w") as f:
    for e in unique_emails:
        f.write(e + "\n")

print("Done! Total emails:", len(unique_emails))