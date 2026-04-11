
from transformers import pipeline

fill_mask = pipeline("fill_mask", model="./tecx_sanskrit_model")
# "dharma-kshetre kuru-kshetre [MASK] yuyutsavah"
result = fill_mask("धर्मक्षेत्रे कुरुक्षेत्रे [MASK] युयुत्सवः।")
print(result[0]['token_str']) # Should predict 'समवेता'
