# TecXSanskritCleaner
TecX Sanskrit Cleaner

```
TecXSanskritCleaner/
├── setup.py                # Configuration for the library
├── README.md               # Documentation for users
├── requirements.txt        # External dependencies
└── sanskrit_cleaner/       # The core package folder
    ├── __init__.py         # Makes this folder a package
    └── master_cleaner.py   # Your actual cleaning script
```

In the context of computational linguistics and Natural Language Processing (NLP) for Sanskrit, the difference lies in their specific roles in the data processing pipeline: a Sanskrit Cleaner prepares raw text, while a Sanskrit Model understands or generates the language. 

Sanskrit Cleaner (Data Pre-processing)
A cleaner is a utility or script used to normalize and "clean" raw Sanskrit text before it is analyzed by a computer. Its primary goal is to remove noise and standardize the input.
Standardization: Converts different encodings (like ITRANS, SLP1, or Velthuis) into a uniform format, typically Devanagari or IAST.
Noise Removal: Removes non-Sanskrit characters, extra whitespace, or modern punctuation that might interfere with traditional analysis.
Sandhi Handling: Some cleaners may perform basic Sandhi splitting (breaking joined words) to make the text more readable for other tools.
Purpose: To ensure high-quality, consistent data for training or testing NLP systems. 
