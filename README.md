
# Careumz - AI-Powered Virtual Health Assistant

Careumz is an intelligent virtual health assistant powered by NVIDIA Riva AI that provides speech-to-text conversion and intent recognition capabilities. The application features a user-friendly web interface for seamless interaction with the AI services.

## Features

- 🎤 **Speech-to-Text Conversion**: Convert audio recordings into text with high accuracy
- 💬 **Text Intent Recognition**: Analyze and understand user intentions from text input
- 🩺 **Health Status Monitoring**: Real-time server health checks
- 🔄 **Real-time Processing**: Immediate feedback and results
- 📱 **Responsive Design**: Works seamlessly across different devices

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.8 or higher
- NVIDIA Riva SDK
- Flask
- Node.js (for serving the frontend)
- Modern web browser

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Careumz-AI/Tech-solution/careumz.git
cd careumz
```

2. Install Python dependencies:
```bash
pip install flask grpcio riva-api
```

3. Configure NVIDIA Riva:
- Ensure NVIDIA Riva server is running
- Update the `RIVA_SERVER` variable in `app.py` with your Riva server address

## Project Structure

```
careumz/
├── frontend.html
├── backend.py
├── README.md
└── requirements.txt
```

## Running the Application

1. Start the backend server:
```bash
cd backend
python app.py
```

2. Open the frontend:
- Open `frontend/index.html` in a web browser
- Or serve it using a local HTTP server:
```bash
python -m http.server 8000
```

The application will be available at:
- Backend: `http://localhost:5000`
- Frontend: `http://localhost:8000`

## API Endpoints

### Speech to Text
- **Endpoint**: `/speech-to-text`
- **Method**: POST
- **Input**: Audio file (multipart/form-data)
- **Response**: JSON with transcribed text

### Text Intent Analysis
- **Endpoint**: `/text-to-intent`
- **Method**: POST
- **Input**: JSON with text field
- **Response**: JSON with intent classification

### Health Check
- **Endpoint**: `/health`
- **Method**: GET
- **Response**: Server status information

## Frontend Features

- Clean, intuitive user interface
- Real-time feedback
- Error handling with user-friendly messages
- Responsive design using Bootstrap
- Progress indicators for long-running operations

## Security Considerations

- Implement proper authentication before deployment
- Add rate limiting for API endpoints
- Secure the NVIDIA Riva server connection
- Validate file uploads and input sanitization

## Error Handling

The application includes comprehensive error handling for:
- Invalid audio files
- Empty or irrelevant text input
- Server connection issues
- Low confidence intent detection

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- NVIDIA Riva AI for providing the core AI capabilities
- Bootstrap for the frontend framework
- Axios for handling HTTP requests

## Support

For support, please open an issue in the GitHub repository or contact the maintenance team.
