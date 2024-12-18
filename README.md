# some python tools

### Install
```
pip install -e .
```

### Usage
Agent
```python
from my_own_tools import *

api_keys = load_json("config/api_keys.json")
agent = Agent("openai/gpt-4o-mini", "openrouter", api_keys)
print(agent.chat_completion("who are you?"))
```

Batch Completion
```python
from my_own_tools import *

api_keys = load_json("config/api_keys.json")
agent = Agent("openai/gpt-4o-mini", "openrouter", api_keys)
print(agent.batch_completion(["who are you?", "what is your name?"]))
```

Batch API request
see `scripts/api_parallel/`