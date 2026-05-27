from flask import Flask, jsonify, request

app = Flask(__name__)

market = {
    1: {"product": "atta 5kg", "person": "Pavan"},
    2: {"product": "suga 5kg", "person": "manikanta"},
}


# ====================CREATE ==================
@app.route("/market", methods=["POST"])
def add_product():
    data = request.json
    new_id = max(market.keys()) + 1 if market else 1
    market[new_id] = {
        "product": data["product"],
        "person": data["person"]
    }
    return jsonify({"message": "product added", "id": new_id})


# ======================= READ ALL ============================
@app.route("/market", methods=["GET"])
def get_products():
    return jsonify(market)


# =======================READ ONE =========================
@app.route("/market/<int:id>", methods=["GET"])
def get_product_by_id(id):
    product = market.get(id)
    if product:
        return jsonify(product)
    return jsonify({"error": "product not found"}), 404


# ================ UPDATE ==================================
@app.route("/market/<int:id>", methods=["PUT"])
def update_product(id):
    if id in market:
        data = request.json
        market[id].update(data)
        return jsonify({"message": "product updated"})
    return jsonify({"error": "product not found"}), 404


# ================ DELETE ================================
@app.route("/market/<int:id>", methods=["DELETE"])
def delete_product(id):
    if id in market:
        del market[id]
        return jsonify({"message": "product deleted"})
    return jsonify({"error": "product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
