import os
import sys
import subprocess

base_path = sys.argv[1]
input_category = sys.argv[2]

context = os.path.join(base_path, 'context.txt')
input_path = os.path.join(base_path, input_category)

intermidiate_path = os.path.join(base_path, 'full_context')
output_path = os.path.join(base_path, 'llm_output')

with open(context, 'r') as f:
    context = f.read()

for file in os.listdir(input_path):
    if not file.endswith(".txt"):
        continue

    if os.path.exists(os.path.join(output_path, file)):
        continue

    print(file)

    with open(os.path.join(input_path, file), 'r') as f:
        snippet = f.read()

    while '\n\n' in snippet:
        snippet = snippet.replace('\n\n', '\n')

    with open(os.path.join(intermidiate_path, file), 'w') as f:
        f.write(f'{context}\n{snippet}# API:')

    result = subprocess.run(
        ['/path/to/llama.cpp/main', '-m',
         '/path/to/codellama/CodeLlama-7b-Python/ggml-model-q4_0.gguf',
         '-c', '16000', '-n', '2048', '-ngl', '1', '-f',
         os.path.join(intermidiate_path, file)], check=True, capture_output=True)

    with open(os.path.join(output_path, file), 'w') as f:
        f.write(result.stdout.decode('utf-8'))
