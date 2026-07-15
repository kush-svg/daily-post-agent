import yaml
import sys

def main():
    with open("queue.yaml", "r", encoding="utf-8") as f:
        items = yaml.safe_load(f) or []
        
    pending_idx = next((i for i, item in enumerate(items) if item.get("status") == "pending"), None)
    if pending_idx is None:
        print("No pending items.")
        sys.exit(0)
        
    item = items[pending_idx]
    print(f"Marking item as published: {item.get('text', '')[:30]}...")
    
    # Update item status
    item["status"] = "published"
    
    # Write back to yaml
    with open("queue.yaml", "w", encoding="utf-8") as f:
        yaml.dump(items, f, sort_keys=False, allow_unicode=True)
            
    print("Done!")

if __name__ == "__main__":
    main()
