# Paddle OCR Web Service

Paddle OCR app provides OCR (Optical Character Recognition) service via web service based on Python API service and PaddleOCR library.

## Features

- **RESTful API Service**: Provides OCR functionality through HTTP API endpoints
- **Multi-language Support**: Supports Chinese, English, French, German, Korean, Japanese and more
- **Image Upload**: Accepts image files for text recognition
- **JSON Response**: Returns recognized text with confidence scores in JSON format

## Service Information

- **Protocol**: RESTful API
- **Port**: 8888
- **Host**: 0.0.0.0 (accessible from all network interfaces)

## Dependencies

- FastAPI - Modern web framework for building APIs
- Uvicorn - ASGI server implementation
- PaddleOCR - OCR library by PaddlePaddle
- PIL (Pillow) - Python Imaging Library
- python-multipart - For handling file uploads

## Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the service:
```bash
python main_ocr.py
```

The service will start on `http://localhost:8888`

## API Endpoints

### POST /image2text/

Uploads an image file and returns recognized text with confidence scores.

#### Request

```bash
curl --location 'http://localhost:8888/image2text/' \
--form 'file=@"/path/to/your/image.png"'
```

#### Response

```json
{
    "message": {
        "0": {
            "rec_texts": [
                "@iisayao7692年前",
                "如燕的声音真好听，真清脆。上次听到这种声音还是康熙王朝中的蓝齐儿。"
            ],
            "rec_scores": [
                0.9049592018127441,
                0.9814294576644897
            ]
        }
    }
}
```

#### Response Fields

- `message`: Object containing OCR results
  - `{index}`: Sequential index for each detected text region
    - `rec_texts`: Array of recognized text strings
    - `rec_scores`: Array of confidence scores (0.0 to 1.0) for each recognized text

### POST /image2text2/

Alternative endpoint for processing image data directly (binary data).

## Supported Image Formats

- PNG
- JPG/JPEG
- BMP
- TIFF
- And other common image formats supported by PIL

## Language Support

The OCR service currently uses Chinese (`ch`) as the default language. You can modify the language parameter in `ocr_paddle.py` to support other languages:

- `ch` - Chinese
- `en` - English  
- `fr` - French
- `german` - German
- `korean` - Korean
- `japan` - Japanese

## File Structure

```
paddle_ocr/
├── Dockerfile          # Docker configuration
├── VERSION             # Version information
├── README.md           # This file
└── ocr/
    ├── main_ocr.py     # Main FastAPI application
    ├── ocr_paddle.py   # PaddleOCR wrapper functions
    └── requirements.txt # Python dependencies
```

## Error Handling

The API returns appropriate HTTP status codes:

- `200` - Success
- `400` - Invalid file format (non-image files)
- `500` - Internal server error

## CORS Configuration

The service is configured with CORS middleware to allow cross-origin requests from any domain (`*`).

## Docker Support

A Dockerfile is provided for containerized deployment. The service can be built and run using Docker for consistent deployment across different environments.

## Usage Notes

- Uploaded images are temporarily saved to the `./uploads/` directory
- The service supports real-time OCR processing
- Text orientation detection is enabled for better accuracy
- Confidence scores help evaluate the reliability of recognized text
