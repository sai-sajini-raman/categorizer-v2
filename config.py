import os
import dotenv

# LLM Configuration
ENDPOINT = "https://models.github.ai/inference"
CREDENTIAL = os.environ.get("GITHUB_TOKEN")
MODEL = "openai/gpt-4.1"
MAX_TOKENS = 2048

# Paths
DATA_DIR = 'data'
TICKETS_FILE = os.path.join(DATA_DIR, 'tickets.xlsx')
MEMORY_FILE = os.path.join(DATA_DIR, 'category_memory.json')
OUTPUT_FILE = os.path.join(DATA_DIR, 'tickets_categorized.xlsx')



# Prompts
SUGGEST_CATEGORY_PROMPT = (
		"You are an AI that helps categorize IT incident tickets concisely."
		"Given the following ticket(s):"
		"{tickets}"
		"Respond as follows:"
		"- If you can confidently assign a category, reply with a short, specific category name (maximum 3 words, no quotes, no extra text)."
		"- If you cannot confidently assign a category, reply with exactly this word: Uncategorized"
		"- Do NOT explain, apologize, repeat the prompt, or add any other information."
		"- Reply with only the category name or 'Uncategorized', nothing else."
		# "Examples:"
		# "Correct: Network Issue"
		# "Correct: Performance"
		# "Correct: Uncategorized"
		# "Incorrect: Sorry, I cannot categorize this."
		# "Incorrect: This ticket seems to be about..."
		# "Incorrect: 'Network Issue'"
		# "Incorrect: Category: Network Issue"
		"Now, what is the best category for these tickets?"
	)

MERGE_DECISION_PROMPT = (
        "Given two categories with their example tickets, decide if they should be merged."
        "Respond with exactly one word: YES or NO."
        "Do NOT explain, apologize, repeat the prompt, or add any other information."
        "Examples:"
        "Correct: YES"
        "Correct: NO"
        "Incorrect: Yes, they should be merged."
        "Incorrect: No, they are distinct."
        "Category A: {name_a}, Tickets: {examples_a} | Category B: {name_b}, Tickets: {examples_b}. Should these be merged?"
    )

ADJUST_THRESHOLD_PROMPT = (
        "Given the current similarity threshold, number of categories, and average tickets per category, decide if the threshold should be increased, decreased, or kept the same."
        "Respond with exactly one word: INCREASE, DECREASE, or KEEP."
        "Do NOT explain, apologize, repeat the prompt, or add any other information."
        "Examples:"
        "Correct: INCREASE"
        "Correct: DECREASE"
        "Correct: KEEP"
        "Incorrect: Increase it."
        "Incorrect: Decrease the threshold."
        "Incorrect: Keep it the same."
        "Current similarity threshold: {current_threshold}. Categories: {num_categories}, Avg tickets/category: {avg_tickets_per_category}. Respond with INCREASE / DECREASE / KEEP."
    )