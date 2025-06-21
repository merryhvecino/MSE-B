from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.models import Product, Supplier
from app import db

products_bp = Blueprint('products', __name__)

@products_bp.route('/', methods=['GET'])
@jwt_required()
def get_products():
    # Include option to filter deleted products
    include_deleted = request.args.get('include_deleted', 'false').lower() == 'true'
    query = Product.query
    
    if not include_deleted:
        query = query.filter_by(is_deleted=False)
    
    products = query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'description': p.description,
        'quantity': p.quantity,
        'category': p.category,
        'unit': p.unit,
        'threshold': p.threshold,
        'supplier_id': p.supplier_id,
        'barcode': p.barcode,
        'is_deleted': p.is_deleted
    } for p in products]), 200

@products_bp.route('/', methods=['POST'])
@jwt_required()
def create_product():
    data = request.get_json()
    
    # Check if product with barcode already exists
    if Product.query.filter_by(barcode=data['barcode']).first():
        return jsonify({'error': 'Product with this barcode already exists'}), 400
    
    product = Product(
        name=data['name'],
        description=data.get('description'),
        quantity=data.get('quantity', 0),
        category=data.get('category'),
        unit=data.get('unit'),
        threshold=data.get('threshold'),
        supplier_id=data.get('supplier_id'),
        barcode=data['barcode']
    )
    
    db.session.add(product)
    db.session.commit()
    
    return jsonify({
        'message': 'Product created successfully',
        'product_id': product.id
    }), 201

@products_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    
    # Check if updating barcode and if it conflicts with existing product
    if 'barcode' in data and data['barcode'] != product.barcode:
        if Product.query.filter_by(barcode=data['barcode']).first():
            return jsonify({'error': 'Product with this barcode already exists'}), 400
    
    # Update fields
    for field in ['name', 'description', 'quantity', 'category', 'unit', 
                 'threshold', 'supplier_id', 'barcode']:
        if field in data:
            setattr(product, field, data[field])
    
    db.session.commit()
    return jsonify({'message': 'Product updated successfully'}), 200

@products_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_product(id):
    product = Product.query.get_or_404(id)
    
    # Implement soft delete
    product.is_deleted = True
    db.session.commit()
    
    return jsonify({'message': 'Product deleted successfully'}), 200

@products_bp.route('/<int:id>/restore', methods=['POST'])
@jwt_required()
def restore_product(id):
    product = Product.query.get_or_404(id)
    
    # Restore soft deleted product
    product.is_deleted = False
    db.session.commit()
    
    return jsonify({'message': 'Product restored successfully'}), 200

@products_bp.route('/barcode/<barcode>', methods=['GET'])
@jwt_required()
def get_product_by_barcode(barcode):
    product = Product.query.filter_by(barcode=barcode, is_deleted=False).first()
    
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    return jsonify({
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'quantity': product.quantity,
        'category': product.category,
        'unit': product.unit,
        'threshold': product.threshold,
        'supplier_id': product.supplier_id,
        'barcode': product.barcode
    }), 200
