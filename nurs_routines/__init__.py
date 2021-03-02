from .config import CONFIG_DICT

items = CONFIG_DICT.items()
print("Configuration settings:")
for i, j in items:
    print(f"\t{i}: {j}")
