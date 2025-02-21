
# SecretLens - Image Steganography Web Application

A modern web-based steganography tool with a sleek black and white hacker theme that allows users to securely hide and extract messages within images. Built with Flask and featuring real-time message processing.

![SecretLens Demo](demo.gif)

## ✨ Features

### Core Functionality
- Hide text messages within PNG images using LSB technique
- Extract hidden messages with password protection
- Real-time message decoding (no page refresh)
- Secure password-based encryption
- Password strength validation

### UI Features
- Black and white hacker theme
- Matrix rain animation background
- Interactive glitch effects
- Drag & drop image upload
- Real-time image preview
- Password strength indicator
- Loading animations
- Fully responsive design

## 🛠️ Tech Stack

### Backend
- Python 3.x
- Flask
- NumPy
- Pillow (PIL)

### Frontend
- HTML5/CSS3
- JavaScript
- Bootstrap 5
- Font Awesome 6
- AOS (Animate On Scroll)

## 📦 Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/secretlens.git
cd secretlens
```

2. Install required packages
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
python steg.py
```

4. Visit `http://localhost:5000` in your browser

## 💻 Usage

### Hiding a Message
1. Click "Encrypt Message" on the home page
2. Upload an image (drag & drop supported)
3. Enter your secret message
4. Create a strong password
5. Click "Encrypt Message"
6. Download your encoded image

### Extracting a Message
1. Click "Decrypt Message" on the home page
2. Upload the encoded image
3. Enter the password
4. The hidden message will appear on the same page

## 📁 Project Structure
```
secretlens/
├── templates/
│   ├── index.html      # Landing page with matrix effect
│   ├── encode.html     # Message encoding page
│   └── decode.html     # Message decoding page
├── steg.py            # Flask app & steganography logic
└── README.md
```

## 🔒 Security Features

- LSB (Least Significant Bit) steganography
- Password protection for message access
- Password strength requirements:
  - Minimum 8 characters
  - Numbers and letters
  - Special characters
- Real-time strength feedback
- Secure message encoding/decoding

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Important Notes

- Supports PNG image format
- Maximum message size depends on image dimensions
- Keep your password safe - it cannot be recovered
- For educational purposes only

## 🙏 Acknowledgments

- Matrix rain animation inspired by cyberpunk themes
- Steganography implementation using NumPy and PIL
- Modern UI design with Bootstrap and custom CSS
```

