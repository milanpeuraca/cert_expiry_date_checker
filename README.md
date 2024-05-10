# SSL Certificate Expiry Checker

A simple web application that allows users to check the expiry date of SSL certificates for any domain. The application uses Flask for the backend and serves a simple UI to interact with it.

## Features

- Input a domain name in the correct format and receive the SSL certificate expiration date.
- Return expiration date in the format "dd:mm:yyyy".
- Provide a user-friendly error message if the domain does not exist or the SSL certificate cannot be retrieved.

## Project Structure

```
project/
│
├── Dockerfile
├── requirements.txt
├── README.md
├── app/
│   ├── ssl_checker.py
│   └── static/
│       └── index.html
```

## Prerequisites

- Docker (for building and running the container)
- Python (if you want to run it directly without Docker)

## Installation and Usage

### Running with Docker

1. **Build the Docker image**:
   ```bash
   docker build -t ssl-checker .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -p 5000:5000 ssl-checker
   ```

3. **Access the UI**:
   Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

### Running Locally

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask app**:
   ```bash
   python app/ssl_checker.py
   ```

3. **Access the UI**:
   Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

## API Documentation

### Endpoint

`GET /check-cert`

### Parameters

| Name | Type   | Default    | Description                       |
| ---- | ------ | ---------- | --------------------------------- |
| `dns`| string | `vegait.rs`| The domain name to be checked     |

### Example Request

```
GET /check-cert?dns=example.com
```

### Response

#### Success (Status Code: 200)

```json
{
  "dns": "example.com",
  "expiration_date": "15:07:2023"
}
```

#### Error (Status Code: 404 or 400)

```json
{
  "error": "Domain \"invalid-domain\" does not exist or cannot be resolved."
}
```

## Contributing

Contributions are welcome! Feel free to open issues or pull requests to improve the application.