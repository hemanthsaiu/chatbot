from flask import Flask, render_template, request, jsonify
from tkinter import ttk
import torch
from transformers import AutoModelWithLMHead, AutoTokenizer,AutoModelForCausalLM, AutoModelForSeq2SeqLM
from transformers import BertForSequenceClassification, BertTokenizer,MarianTokenizer, MarianMTModel


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    english_text = request.form['message']
    french_text = translate_english_to_french(english_text)
    return jsonify({'translated_message': french_text})

def translate_english_to_french(text):
    
    model_name = "Helsinki-NLP/opus-mt-en-fr"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    
    inputs = tokenizer.encode("translate English to French: " + text, return_tensors="pt")
    outputs = model.generate(inputs, max_length=40, num_beams=4, early_stopping=True)
    print("New Outputs :"+str(outputs))
    # Decode the translated output
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    final_french = translated_text
    print("New :"+str(translated_text))
    
    
    model_name = 'xlm-mlm-enfr-1024'
    print(text)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    model = AutoModelWithLMHead.from_pretrained(model_name)

    tokenized_text = tokenizer.prepare_seq2seq_batch([text], return_tensors='pt')
    translation = model.generate(**tokenized_text)
    print(translation)
    translated_text = tokenizer.batch_decode(translation, skip_special_tokens=False)[0]
    print("Translated Text: "+str(translated_text))
    print("WORKING................")
    inputs = tokenizer(text, return_tensors='pt')

    outputs = model(**inputs)

    predictions = torch.softmax(outputs.logits, dim=-1)
    
    print(predictions)

    prediction_score, prediction_index = torch.max(predictions, dim=-1)

    print(prediction_score)
    # Here we're assuming that the first translation output is French.

    # If you want to specify French, you can set inputs['labels'] to the French language ID.

    french_text = tokenizer.convert_ids_to_tokens(predictions[0].argmax().item())

    
    return final_french

if __name__ == '__main__':
    app.run(debug=True)
