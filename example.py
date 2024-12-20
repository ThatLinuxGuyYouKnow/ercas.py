from flask import Flask, request, jsonify
from ercaspay_client import ErcasPayClient  

app = Flask(__name__)


api_key = "ercas_pay_key" 
client = ErcasPayClient(api_key)

@app.route('/initiate-payment', methods=['POST'])
def initiate_payment():
    try:
       
        payment_data = request.get_json()

        if not payment_data:
            return jsonify({"error": "Request body must be a valid JSON"}), 400

        
        required_fields = [
            "amount",
            "paymentReference",
            "paymentMethods",
            "customerName",
            "currency",
            "customerEmail",
            "customerPhoneNumber",
            "redirectUrl",
            "description",
            "metadata",
        ]

        for field in required_fields:
          if field not in payment_data:
            return jsonify({"error": f"Missing {field} in payment data"}), 400


        if not isinstance(payment_data["amount"], int):
            return jsonify({"error": "Amount must be an integer"}), 400
        
       
        response = client.initiate_payment(**payment_data)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": f"Error initiating payment: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True) 