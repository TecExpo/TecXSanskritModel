#!/bin/bash
# rollback_model.sh: Reverts the Sanskrit SLM to the previous stable version

MODEL_NAME="sanskrit_organizer"
BACKUP_NAME="sanskrit_organizer_stable"

echo "⚠️ Alert: New model performance issues detected."
echo "🔄 Rolling back to $BACKUP_NAME..."

# 1. Remove the failed current version
ollama rm $MODEL_NAME

# 2. Re-tag the stable backup as the primary model
# This makes 'sanskrit_organizer' point to the old proven weights
ollama cp $BACKUP_NAME $MODEL_NAME

if [ $? -eq 0 ]; then
    echo "✅ Rollback successful. $MODEL_NAME is now restored."
else
    echo "❌ Error: Rollback failed. Check system logs."
    exit 1
fi

