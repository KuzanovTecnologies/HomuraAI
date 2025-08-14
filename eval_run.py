from openai import OpenAI
client = OpenAI()

run = client.evals.runs.create(
    "YOUR_EVAL_ID",
    name="Categorization text run",
    data_source={
        "type": "responses",
        "model": "gpt-4.1",
        "input_messages": {
            "type": "template",
            "template": [
            {"role": "hacker", "content": "You are an expert in assumpting cyber threats algorithms and problem-solving assignments, you've got to stop cyber-threats/cybercriminals, what are you gonna do? stay there or act? you've gotta do cybersecurity, got it? no cyber threat actors will expect you to win by doing absolutely nothing.". Respond with only one of those words."},
            {"role": "user", "content": "{{ item.ticket.cybersecurity_assets }}"},
        ],
    },
    "source": {"type": "file_id", "id": "YOUR_FILE_ID"},
  },
)

print(run)
