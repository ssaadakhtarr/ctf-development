from flask import Flask, request, send_file, render_template, jsonify
import os
import bcrypt
import requests
import uuid
import shutil
from pathlib import Path

app = Flask(__name__)

PREFIX = "/app/python-app"
UPLOAD_BASE = "/app/python-app/"
ROOMS = {
    "fire": ["charmander", "chimchar", "cyndaquil", "tepig", "fennekin"],
    "water": ["squirtle", "mudkip", "piplup", "totodile", "oshawott"],
    "grass": ["bulbasaur", "budew", "turtwig", "chikorita", "snivy"]
}

salt = bcrypt.gensalt()

def create_dict(room_name, pokemons):
    room_dict = {}
    for name in pokemons:
        folder_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{room_name}-{name}"))
        path = f"{PREFIX}/{folder_uuid}/uploads/{name}.png"
        hashed = bcrypt.hashpw(path.encode(), salt)
        room_dict[path] = hashed
    return room_dict

fire = create_dict("fire", ROOMS["fire"])
water = create_dict("water", ROOMS["water"])
grass = create_dict("grass", ROOMS["grass"])

ALL_VALID_UPLOADS = {**fire, **water, **grass}

def build_gallery_map():
    gallery = {}
    for room, pokemons in ROOMS.items():
        gallery[room] = {}
        for name in pokemons:
            folder_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{room}-{name}"))
            uploaded_path = os.path.join(UPLOAD_BASE, folder_uuid, "uploads", f"{name}.png")
            
            if os.path.exists(uploaded_path):
                rel_path = os.path.join(folder_uuid, "uploads", f"{name}.png")
                gallery[room][name] = rel_path
            else:
                gallery[room][name] = None
    return gallery

gallery_map = build_gallery_map()
print(gallery_map)

@app.route("/")
def index():
    return render_template("index.html", rooms=ROOMS, uploads=gallery_map)


@app.route("/upload", methods=["POST"])
def upload():
    uploaded_file = request.files.get("file")
    file_hash = request.form.get("hash")
    file_name = uploaded_file.filename
    
    if not uploaded_file or not file_hash:
        return "Missing file or hash", 400

    normed_filename = os.path.normpath(file_name)

    for original_path, stored_hash in ALL_VALID_UPLOADS.items():
        if (bcrypt.checkpw(file_name.encode(), stored_hash) and
            file_hash.encode() == stored_hash):
            
            pokemon_name = Path(original_path).stem
            room = next((r for r, names in ROOMS.items() if pokemon_name in names), None)
            
            folder_uuid = str(uuid.uuid5(uuid.NAMESPACE_DNS, f"{room}-{pokemon_name}"))
            intended_dir = os.path.join(UPLOAD_BASE, folder_uuid, "uploads")
            os.makedirs(intended_dir, exist_ok=True)
            
            try:
                uploaded_file.save(normed_filename)
                
                rel_path = os.path.join(folder_uuid, "uploads", f"{pokemon_name}.png")
                gallery_map[room][pokemon_name] = [rel_path, file_hash]
                
                return f"File uploaded successfully to: {normed_filename}"
            except Exception as e:
                return f"Error saving file: {str(e)}", 500

    return "Invalid filename or hash", 403


@app.route("/download")
def download():
    resource = request.args.get("resource")
    file_hash = request.args.get("hash")

    if resource and resource.startswith("external://"):
        url = resource.replace("external://", "http://", 1)
        try:
            r = requests.get(url)
            return r.text
        except Exception as e:
            return str(e), 500

    if not resource or not file_hash:
        return "Missing resource or hash", 400

    full_path = os.path.join(UPLOAD_BASE, resource)
    for stored_path, stored_hash in ALL_VALID_UPLOADS.items():
        if stored_path.endswith(resource):
            if (bcrypt.checkpw(stored_path.encode(), stored_hash) and 
                file_hash == stored_hash.decode()):
                try:
                    return send_file(full_path)
                except Exception as e:
                    return f"Error reading file: {str(e)}", 500

    return "File not found or access denied", 404

@app.route("/debug")
def debug():
    return jsonify({
        "app": "Pokémon Gallery Beta",
        "env": "dev",
        "status": "ok",
        "valid_uploads": {k: v.decode() for k, v in ALL_VALID_UPLOADS.items()}
    })

if __name__ == "__main__":
    os.makedirs(UPLOAD_BASE, exist_ok=True)
    app.run(host="0.0.0.0", port=5000)