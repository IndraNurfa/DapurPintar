# DapurPintar

DapurPintar adalah chatbot asisten memasak berbasis AI yang membantu pengguna menemukan resep, memahami teknik memasak, dan memanfaatkan bahan yang tersedia di rumah dengan lebih efektif.

Chatbot ini ditujukan untuk siapa saja yang ingin memasak di rumah, mulai dari pemula yang baru belajar hingga pengguna yang sudah terbiasa memasak tetapi membutuhkan inspirasi resep baru atau solusi saat bahan yang tersedia terbatas.

## Features

- Menemukan resep berdasarkan bahan yang tersedia.
- Memberikan panduan memasak langkah demi langkah.
- Menyarankan alternatif atau pengganti bahan.
- Memperkirakan waktu memasak dan jumlah porsi.
- Memberikan tips penyimpanan makanan dan keamanan pangan.

## Tech Stack

- Python
- Streamlit
- Groq API
- python-dotenv

## Installation

Clone repository:

```bash
git clone https://github.com/IndraNurfa/DapurPintar.git
cd DapurPintar
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root directory and add your Groq API key:

```env
GROQ_API_KEY=YOUR_API_KEY
```

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

After the application starts, open the local URL displayed in the terminal.

## Example Questions

- Saya punya telur, nasi, dan bawang. Bisa dibuat masakan apa?
- Apa pengganti santan untuk resep ini?
- Bagaimana cara menggoreng ayam agar tetap renyah?
- Berapa lama waktu yang dibutuhkan untuk memasak sup ayam?
- Bagaimana cara menyimpan makanan sisa dengan aman?

## Project Goal

DapurPintar dirancang untuk membantu pengguna memasak dengan lebih mudah melalui rekomendasi resep yang relevan, panduan yang jelas, serta informasi praktis seputar pengolahan dan penyimpanan makanan.

## License

This project is available for educational and personal use.
