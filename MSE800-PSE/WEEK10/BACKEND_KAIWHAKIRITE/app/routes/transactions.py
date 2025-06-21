from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.models import StockTransaction, Product
from app import db

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('/', methods=['POST'])
@jwt_required()
def create_transaction():
    data = request.get_json()
    current_user = get_jwt_identity()
    
    product = Product.query.get_or_404(data['product_id'])
    
    # Validate transaction
    if data['type'] not in ['in', 'out']:
        return jsonify({'error': 'Invalid transaction type'}), 400
    
    if data['type'] == 'out' and product.quantity < data['quantity']:
        return jsonify({'error': 'Insufficient stock'}), 400
    
    # Create transaction
    transaction = StockTransaction(
        product_id=data['product_id'],
        user_id=current_user['user_id'],
        type=data['type'],
        quantity=data['quantity'],
        notes=data.get('notes')
    )
    
    # Update product quantity
    if data['type'] == 'in':
        product.quantity += data['quantity']
    else:
        product.quantity -= data['quantity']
    
    db.session.add(transaction)
    db.session.commit()
    
    return jsonify({
        'message': 'Transaction created successfully',
        'new_quantity': product.quantity
    }), 201

@transactions_bp.route('/', methods=['GET'])
@jwt_required()
def get_transactions():
    # Support filtering by date range and transaction type
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    trans_type = request.args.get('type')
    product_id = request.args.get('product_id')
    
    query = StockTransaction.query
    
    if start_date:
        query = query.filter(StockTransaction.date >= start_date)
    if end_date:
        query = query.filter(StockTransaction.date <= end_date)
    if trans_type:
        query = query.filter_by(type=trans_type)
    if product_id:
        query = query.filter_by(product_id=product_id)
    
    transactions = query.all()
    
    return jsonify([{
        'id': t.id,
        'product_id': t.product_id,
        'user_id': t.user_id,
        'type': t.type,
        'quantity': t.quantity,
        'date': t.date.isoformat(),
        'notes': t.notes
    } for t in transactions]), 200


@transactions_bp.route('/low-stock', methods=['GET'])
@jwt_required()
def get_low_stock_products():
    # Get products where quantity is below threshold
    products = Product.query.filter(
        Product.quantity <= Product.threshold,
        Product.is_deleted == False
    ).all()
    
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'quantity': p.quantity,
        'threshold': p.threshold,
        'supplier_id': p.supplier_id
    } for p in products]), 200
