import re

class SanskritMasterCleaner:
    def __init__(self, db_conn):
        self.db = db_conn

    def validate_word(self, word):
        """Verifies if a word exists in the local SQL dictionary."""
        query = "SELECT 1 FROM inflections WHERE surface_form = %s LIMIT 1"
        with self.db.cursor() as cursor:
            cursor.execute(query, (word,))
            return cursor.fetchone() is not None

    def clean_text(self, text):
        # 1. Expand Avagraha (ऽ -> अ)
        text = re.sub(r'(\w+)ऽ(\w+)', r'\1 अ\2', text)
        
        # 2. Restore s/sh Visarga (e.g., Namaste -> Namah te)
        vis_rules = {r'(\w+)स्([तथ]\w+)': r'\1ः \2', r'(\w+)श्([चछ]\w+)': r'\1ः \2'}
        for pattern, repl in vis_rules.items():
            text = re.sub(pattern, repl, text)

        # 3. Visarga Lopa (The Ghost Restorer)
        words = text.split()
        final_output = []
        for word in words:
            # Check if adding 'ः' creates a valid dictionary entry
            restored_candidate = word + "ः"
            if self.validate_word(restored_candidate):
                final_output.append(restored_candidate)
            else:
                final_output.append(word)
        
        return " ".join(final_output)

