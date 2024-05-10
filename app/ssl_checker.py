from flask import Flask, request, jsonify, send_from_directory
from OpenSSL import crypto
from datetime import datetime
import ssl
import socket
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/check-cert', methods=['GET'])
def check_cert():
    # Default DNS to check
    dns = request.args.get('dns', default='vegait.rs', type=str)
    try:
        cert = ssl.get_server_certificate((dns, 443))
        x509 = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
        exp_date = datetime.strptime(x509.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')
        formatted_exp_date = exp_date.strftime('%d:%m:%Y')  # Format in "dd:mm:yyyy"

        return jsonify({
            'dns': dns,
            'expiration_date': formatted_exp_date
        })
    except socket.gaierror:
        return jsonify({'error': f'Domain "{dns}" does not exist or cannot be resolved.'}), 404
    except ssl.SSLError as e:
        return jsonify({'error': f'Could not fetch certificate for domain "{dns}". SSL Error: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'Unexpected error fetching certificate for domain "{dns}". Error: {str(e)}'}), 500

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
