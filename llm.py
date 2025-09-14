# --- DeepSeek R1 via GitHub Marketplace API Key ---
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import UserMessage
from azure.core.credentials import AzureKeyCredential

# Import configurations
from config import ENDPOINT, CREDENTIAL, MODEL, MAX_TOKENS
from config import SUGGEST_CATEGORY_PROMPT, MERGE_DECISION_PROMPT, ADJUST_THRESHOLD_PROMPT

client = ChatCompletionsClient(
	endpoint="https://models.github.ai/inference",
	credential=AzureKeyCredential(os.environ.get("GITHUB_TOKEN"))
)

def call_llm(prompt, max_tokens=MAX_TOKENS):
	response = client.complete(
		messages=[UserMessage(prompt)],
		model="openai/gpt-4.1",
		max_tokens=max_tokens,
	)
	return response.choices[0].message.content


def llm_suggest_category_name(tickets):
	prompt = SUGGEST_CATEGORY_PROMPT.format(tickets=tickets)
	print(f"[llm_suggest_category_name] Tickets: {tickets}")
	return call_llm(prompt)

def llm_merge_decision(name_a, examples_a, name_b, examples_b):
	prompt = MERGE_DECISION_PROMPT.format(
		name_a=name_a,
		examples_a=examples_a,
		name_b=name_b,
		examples_b=examples_b
	)
	print(f"[llm_merge_decision] A: {name_a}, B: {name_b}")
	return call_llm(prompt)

def llm_adjust_threshold(current_threshold, num_categories, avg_tickets_per_category):
	prompt = ADJUST_THRESHOLD_PROMPT.format(
		current_threshold=current_threshold,
		num_categories=num_categories,
		avg_tickets_per_category=avg_tickets_per_category
	)
	print(f"[llm_adjust_threshold] Threshold: {current_threshold}, Categories: {num_categories}, Avg: {avg_tickets_per_category}")
	return call_llm(prompt)


