from nomic import atlas
import numpy as np
from datasets import load_dataset

dataset = load_dataset('wikipedia', '20220301.en')['train']

max_documents = 100000
subset_idxs = np.random.choice(len(dataset), size=max_documents, replace=False).tolist()
documents = [dataset[i] for i in subset_idxs]

response = atlas.map_data(data=documents,
                          indexed_field='text',
                          identifier='Wiki 100K',
                          description='A 10,0000 point sample of the huggingface wikipedia dataset embedded with Nomic\'s Embed v0.0.13 model.',
                          topic_model=True)
print(response)