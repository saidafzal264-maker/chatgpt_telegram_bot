import yaml
import dotenv
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load yaml config
with open(config_dir / "config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

# load .env config
config_env = dotenv.dotenv_values(config_dir / "config.env")

# config parameters
telegram_token = "8576476633:AAFDcSvp82YIx6jwwG6uSd9pueWaDBzsbV0"
openai_api_key = "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"
openai_api_base = None  # agar kerak bo'lsa o'zgartiring
allowed_telegram_usernames = ["username1", "username2"]  # misol uchun
new_dialog_timeout = 300  # misol uchun 5 daqiqa
enable_message_streaming = True
return_n_generated_images = 1
image_size = "512x512"
n_chat_modes_per_page = 5
mongodb_uri = f"mongodb://mongo:{config_env['MONGODB_PORT']}"
# chat_modes
with open(config_dir / "chat_modes.yml", 'r') as f:
    chat_modes = yaml.safe_load(f)

# models
with open(config_dir / "models.yml", 'r') as f:
    models = yaml.safe_load(f)

# files
help_group_chat_video_path = Path(__file__).parent.parent.resolve() / "static" / "help_group_chat.mp4"
