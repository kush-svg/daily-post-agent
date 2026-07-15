import yaml
import sys

def main():
    try:
        with open("queue.yaml", "r", encoding="utf-8") as f:
            items = yaml.safe_load(f) or []
    except FileNotFoundError:
        print("### ❌ queue.yaml not found!")
        sys.exit(1)

    pending_item = next((item for item in items if item.get("status") == "pending"), None)

    if not pending_item:
        print("### 🔴 Queue is empty! No pending items found.")
        sys.exit(1)

    print("### 🚀 Next item in queue:\n")
    
    # X formatting
    print("#### X (Twitter) Post - Copy & Paste:")
    print("```text")
    print(pending_item.get("text", ""))
    print("```\n")
    
    # Reddit formatting
    print("#### Reddit Post - Copy & Paste:")
    print(f"**Subreddit**: `r/{pending_item.get('reddit_subreddit', 'Unknown')}`")
    print(f"**Type**: `{pending_item.get('reddit_post_type', 'self')}`\n")
    print("**Title**:")
    print("```text")
    title = pending_item.get("reddit_title", pending_item.get("text", "")[:50] + "...")
    print(title)
    print("```\n")
    
    if pending_item.get("reddit_post_type") == "self":
        print("**Body**:")
        print("```text")
        print(pending_item.get("text", ""))
        print("```\n")
    elif pending_item.get("reddit_post_type") == "link":
        print("**Link**:")
        print("```text")
        print(pending_item.get("url", ""))
        print("```\n")
    elif pending_item.get("media_urls"):
        print("**Media URLs**:")
        for url in pending_item.get("media_urls", []):
            print(f"- {url}")
        print()

if __name__ == "__main__":
    main()
