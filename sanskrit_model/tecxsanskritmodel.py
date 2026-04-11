"""
1. Load your Custom Dataset 
Use the datasets library to load your text files. It is best to split your data into a train set (for learning) and a test set (for checking accuracy). 
"""
from datasets import load_dataset

# Load your custom text file
dataset = load_dataset("text", data_files={"train": "my_sanskrit_texts.txt"})

"""
2. Initialize the Tokenizer
The tokenizer converts your Devanagari text into numerical "tokens" the model can understand. Use the tokenizer that matches your chosen pre-trained model. 
"""
from transformers import AutoTokenizer

model_checkpoint = "OMRIDRORI/sanskrit-bert-from-scratch"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

def tokenize_function(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length")

tokenized_datasets = dataset.map(tokenize_function, batched=True)

"""
3. Load the Pre-trained Model 
Load the model weights. For simple fine-tuning on text patterns, we use AutoModelForMaskedLM. 
"""
from transformers import AutoModelForMaskedLM

model = AutoModelForMaskedLM.from_pretrained(model_checkpoint)
"""
4. Configure Training Arguments
This step defines "how" the model learns—for example, how many times it reads the data (epochs) and how fast it adjusts its internal weights (learning_rate).
"""
from transformers import TrainingArguments, Trainer

training_args = TrainingArguments(
    output_dir="./sanskrit-finetuned",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    weight_decay=0.01,
    num_train_epochs=3, # Number of times to go through your data
)
"""
5. Start the Fine-tuning (The Training Loop) 
The Trainer class handles the heavy lifting of the training process. 
"""
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
)

trainer.train() # This starts the actual fine-tuning

"""
6. Save your New Model
Once finished, save your customized model to use it later without retraining. 
"""
trainer.save_model("./tecx-sanskrit-model")
