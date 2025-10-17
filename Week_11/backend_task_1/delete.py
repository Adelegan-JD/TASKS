from http.server import BaseHTTPRequestHandler, HTTPServer
import json
data = [
    {'personal_info' : {
        'Name' : 'Deborah Adelegan',
        'Track': 'AI Engineer',
        'Course': 'Backend Engineering'},
    'scores' : {
        'MCQ': '95',
        'Applied Theory': '90'
    }
    },
    {'personal_info' : {
        'Name' : 'Deborah Adelegan',
        'Track': 'AI Engineer',
        'Course': 'Backend Engineering'},
    'scores' : {
        'MCQ': '95',
        'Applied Theory': '90'
    }
    }
]

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, data, status = 200):
        self.send_response(status)
        self.send_header('content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode())

    def do_DELETE(self):
        record_id = int(self.path.split('/')[-1])
        content_size = int(self.headers.get('Content-Length', 0))
        parsed_data = self.rfile.read(content_size)

        deleted_data = json.loads(parsed_data)


        if record_id >= len(data) or record_id < 0:
            self.send_data({'error': 'Record not found'}, status=404)
            return
        
        else:
            deleted_data = data.remove(data[record_id])
            self.send_data({'message': 'Record deleted successfully', "content": deleted_data}, status=200)
        
        self.send_data(data)
