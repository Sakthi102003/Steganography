import os

import numpy as np
from flask import (Flask, jsonify, redirect, render_template, request,
                   send_file, url_for)
from PIL import Image

app = Flask(__name__)

# Function to convert a text message into binary
def text_to_binary(message):
    return ''.join(format(ord(char), '08b') for char in message)

# Function to convert binary to text
def binary_to_text(binary_data):
    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    return ''.join(chr(int(byte, 2)) for byte in chars if byte != '11111110')

# Function to encode a message into an image
def encode_message(image_path, message, output_path):
    # Load the image
    img = Image.open(image_path)
    img_array = np.array(img)

    # Convert message to binary and add delimiter
    binary_message = text_to_binary(message) + '1111111111111110'  # End marker

    message_index = 0
    height, width, _ = img_array.shape

    # Check if the image can store the message
    if len(binary_message) > height * width * 3:
        raise ValueError("Message is too large for the given image.")

    # Embed message in LSB of pixels
    for i in range(height):
        for j in range(width):
            for k in range(3):  # RGB channels
                if message_index < len(binary_message):
                    img_array[i, j, k] = (img_array[i, j, k] & ~1) | int(binary_message[message_index])
                    message_index += 1

    # Save the encoded image
    encoded_img = Image.fromarray(img_array)
    encoded_img.save(output_path)
    print(f"Message successfully hidden in {output_path}")

# Function to decode a hidden message from an image
def decode_message(image_path):
    # Load the stego image
    img = Image.open(image_path)
    img_array = np.array(img)

    binary_message = ''
    
    # Extract LSBs from pixels
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            for k in range(3):
                binary_message += str(img_array[i, j, k] & 1)

    # Find end marker and extract message
    end_marker = '1111111111111110'
    if end_marker in binary_message:
        binary_message = binary_message[:binary_message.index(end_marker)]
    
    return binary_to_text(binary_message)

# Store passwords in a dictionary for simplicity
passwords = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['GET', 'POST'])
def encode():
    if request.method == 'POST':
        image = request.files['image']
        message = request.form['message']
        password = request.form['password']
        output_path = 'encoded.png'

        if image and message and password:
            image_path = 'input.png'
            image.save(image_path)
            try:
                encode_message(image_path, message, output_path)
                passwords[output_path] = password  # Store the password for the encoded image
                return send_file(output_path, as_attachment=True)
            except Exception as e:
                return str(e)
        return 'Failed to encode message. Missing data.'
    return render_template('encode.html')

@app.route('/decode', methods=['GET', 'POST'])
def decode():
    if request.method == 'POST':
        if 'image' not in request.files:
            return jsonify({'error': 'No image uploaded'})
        
        image = request.files['image']
        password = request.form['password']
        
        if image.filename == '':
            return jsonify({'error': 'No image selected'})
        
        try:
            if passwords.get('encoded.png') == password:  # Check against the correct key
                secret_message = decode_message(image.filename)
                return jsonify({'message': secret_message})
            else:
                return jsonify({'error': 'Incorrect password.'})
        except Exception as e:
            return jsonify({'error': str(e)})
    return render_template('decode.html')

if __name__ == "__main__":
    app.run(debug=True)
