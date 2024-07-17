# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import subprocess
# import os
# import uuid

# app = Flask(__name__)
# CORS(app)

# @app.route('/convert', methods=['POST'])
# def convert_pdf():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part'}), 400

#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400

#     if file:
#         # Create a unique temporary directory for the conversion
#         temp_dir = os.path.join('temp', str(uuid.uuid4()))
#         os.makedirs(temp_dir, exist_ok=True)
        
#         input_path = os.path.join(temp_dir, file.filename)
#         output_folder = os.path.join(temp_dir, 'output')
#         os.makedirs(output_folder, exist_ok=True)
        
#         file.save(input_path)
        
#         # Run Marker
#         subprocess.run([
#             'marker_single', input_path, output_folder, '--langs', 'Portuguese'
#         ])
        
#         # Read the converted markdown file
#         output_path = os.path.join(output_folder, os.path.splitext(file.filename)[0] + '.md')
#         if not os.path.exists(output_path):
#             return jsonify({'error': 'Conversion failed'}), 500
        
#         with open(output_path, 'r') as f:
#             markdown_content = f.read()
        
#         # Clean up temporary files
#         os.remove(input_path)
#         os.remove(output_path)
#         os.rmdir(output_folder)
#         os.rmdir(temp_dir)
        
#         return jsonify({'markdown': markdown_content})

# if __name__ == '__main__':
#     app.run(debug=True)