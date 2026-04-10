import pandas as pd
from sqlalchemy import create_engine
import sys

def migrate_csv_to_sql(csv_file, table_name):
    # Database connection parameters (from your Docker Compose)
    DB_URI = "postgresql://sanskrit_user:securepassword@localhost:5432/dictionary_db"
    
    try:
        engine = create_engine(DB_URI)
        
        # Load the CSV into a DataFrame
        # Sanskrit data must be read with UTF-8 encoding to preserve Devanagari
        df = pd.read_csv(csv_file, encoding='utf-8')
        
        # Ingest data into SQL
        # 'append' ensures you don't delete existing dictionary entries
        df.to_sql(table_name, engine, if_exists='append', index=False)
        
        print(f"Successfully migrated {len(df)} records from {csv_file} to {table_name}")
        
    except Exception as e:
        print(f"Migration Error: {e}", file=sys.stderr)

# Usage:
# migrate_csv_to_sql('monier_williams_stems.csv', 'stems')
# migrate_csv_to_sql('inflected_forms.csv', 'inflections')

