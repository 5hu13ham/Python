from ibm_watsonx_orchestrate import Orchestrate

# 🔐 Replace these with your actual values
API_KEY = "your_ibm_cloud_api_key"
ORCHESTRATE_URL = "https://api.us-south.orchestrate.ai.cloud.ibm.com"

# 🔧 Initialize client
client = Orchestrate(api_key=API_KEY, url=ORCHESTRATE_URL)

# 📋 List all available skills
skills = client.skills.list()
print("Available Skills:")
for skill in skills:
    print(f"- {skill.name} (ID: {skill.skill_id})")
