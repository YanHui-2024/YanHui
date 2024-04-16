import os
import random
import subprocess

base_path = os.path.dirname(os.path.realpath(__file__))
prompt_path = os.path.join(base_path, 'llm_prompt')
output_path = os.path.join(base_path, 'llm_output')

all_samples = []
for category in ['gpu', 'operator', 'syntax', 'typing']:
    for sample in os.listdir(os.path.join(base_path, category)):
        if not sample.endswith('.txt'):
            continue
        all_samples.append(os.path.join(category, sample))
print(len(all_samples))

test_index = 0

while len(all_samples) > 0:
    sample1 = all_samples.pop(random.randrange(len(all_samples)))
    sample2 = all_samples.pop(random.randrange(len(all_samples)))
    sample3 = all_samples.pop(random.randrange(len(all_samples)))
    sample4 = all_samples.pop(random.randrange(len(all_samples)))
    samples = [sample1, sample2, sample3, sample4]
    print(samples)

    prompt_file = os.path.join(prompt_path, f'test_{test_index}.txt')
    with open(prompt_file, 'w') as f:
        for sample in samples:
            sample_file = os.path.join(base_path, sample)
            with open(sample_file, 'r') as f1:
                snippet = f1.read()
            f.write(f'{snippet}\n\n')

        f.write('# API:')

    out_file = os.path.join(output_path, f'test_{test_index}.txt')
    result = subprocess.run(
        ['/path/to/llama.cpp/main', '-m',
         '/path/to/codellama/CodeLlama-7b-Python/ggml-model-q4_0.gguf',
         '-c', '16000', '-n', '4096', '-ngl', '1', '-f',
         prompt_file], check=True, capture_output=True)

    with open(os.path.join(output_path, out_file), 'w') as f:
        f.write('# API:')
        f.write(result.stdout.decode('utf-8'))

    test_index += 1
