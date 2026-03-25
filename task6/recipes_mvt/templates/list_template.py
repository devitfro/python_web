def render_list(recipes):
    print("\n--- RECIPES LIST ---")
    for r in recipes:
        print(f"{r['id']} | {r['title']}")