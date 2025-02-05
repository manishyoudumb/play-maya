
## MAKE A COPY OF THIS CALLED config.py
VERBOSE = True
USE_GPU = False  # Set to True to use GPU acceleration. Refer to the README for instructions on installing PyTorch with CUDA support.


## OLLAMA COMPLETIONS API EXAMPLE ##
COMPLETIONS_API = "ollama"
COMPLETION_MODEL = "sparksammy/samantha-v3-uncensored"
OLLAMA_API_BASE_URL = "http://localhost:11434" #This should be the defualt
OLLAMA_KEEP_ALIVE = "5m" # The duration that models stay loaded in memory (default "5m"). Set to "-1" to keep models loaded indefinitely


## Faster Whisper local transcription ###
TRANSCRIPTION_API = "FasterWhisper" # this will use the local whisper model
WHISPER_MODEL = "tiny.en" # If you prefer not to use english set it to "tiny", if the transcription quality is too low then set it to "base" but this will be a little slower
BEAM_SIZE = 5


### Piper TTS SETTINGS ###
TTS_ENGINE="piper" 
PIPER_VOICE = "default_female_voice" # You can add more voices to the piper_tts/voices folder
PIPER_VOICE_INDEX = 0 # For multi-voice models, select the index of the voice you want to use
PIPER_VOICE_SPEED = 1.0 # Speed of the TTS, 1.0 is normal speed, 2.0 is double speed, 0.5 is half speed

### OPENAI TTS SETTINGS ###
# TTS_ENGINE="openai" 
# OPENAI_VOICE = "nova"

### PROMPTS ###
# Options: "default_prompt", "chat_prompt"
# - "default_prompt": Straight to the point assistant that can write to your clipboard when requested.
# - "chat_prompt": Simple prompt for a friendly back-and-forth chat. Does NOT support writing to clipboard.
# - None: No system prompt, for the raw out-of-the-box model behavior.
# Or create your own prompt in the "system_prompts" folder, then put the name of the file here.
ACTIVE_PROMPT = "default_prompt"

### HOTKEYS ###
# Hotkeys can be set to None to disable them
CANCEL_HOTKEY = 'alt+ctrl+e'
CLEAR_HISTORY_HOTKEY = 'alt+ctrl+w'
RECORD_HOTKEY = 'alt+ctrl+r' # Press to start, press again to stop, or hold and release. Double tap to include clipboard

RECORD_HOTKEY_DELAY = 0.7 # Seconds to wait it listen for the double tap of the hotkey, outside of this time window the second tap will stop recording
SUPPRESS_NATIVE_HOTKEYS = True # Suppress the native system functionality of the defined hotkeys above (Windows only)
ALWAYS_INCLUDE_CLIPBOARD = False # Always include the clipboard content without having to double tap the record hotkey


### MISC ###
AUDIO_FILE_DIR = "audio_files"
MAX_TOKENS = 8000 #Max tokens allowed in memory at once
START_SEQ = "[CLIPSTART]" #the model is instructed to place any text for the clipboard between the start and end seq
END_SEQ = "[CLIPEND]" #the model is instructed to place any text for the clipboard between the start and end seq


### AUDIO SETTINGS ###
BASE_VOLUME = 1 
START_SOUND_VOLUME = 0.05
END_SOUND_VOLUME = 0.05
CANCEL_SOUND_VOLUME = 0.09
MIN_RECORDING_DURATION = 0.3
MAX_RECORDING_DURATION= 600 # If you record for more than 10 minutes, the recording will stop automatically

