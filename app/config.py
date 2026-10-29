import os
from dotenv import load_dotenv
load_dotenv()

APP_NAME = os.getenv("APP_NAME", "SHUL_V_1.7")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./shul.db")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
MODEL_NAME = os.getenv("MODEL_NAME", "openrouter/auto")
ENABLE_LLM = os.getenv("ENABLE_LLM", "false").lower() == "true"
SECURITY_TOOLS_DRY_RUN = os.getenv("SECURITY_TOOLS_DRY_RUN", "true").lower() == "true"
AUTHORIZED_LAB_TARGETS = {
    x.strip().lower() for x in os.getenv("AUTHORIZED_LAB_TARGETS", "127.0.0.1,localhost").split(",") if x.strip()
}
WORKSPACE_DIR = os.getenv("WORKSPACE_DIR", "workspace/generated")
