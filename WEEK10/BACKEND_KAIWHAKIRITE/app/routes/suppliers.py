from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.models import Supplier
from app import db

suppliers_bp = Blueprint('suppliers', __name__)

@suppliers_bp.route('/', methods=['GET'])
@jwt_required()
def get_suppliers():
    suppliers = Supplier.query.all()
    return jsonify([{
        'id': s.id,
        'name': s.name,
        'contact_name': s.contact_name,
        'email': s.email,
        'phone': s.phone,
        'address': s.address
    } for s in suppliers]), 200

@suppliers_bp.route('/', methods=['POST'])
@jwt_required()
def create_supplier():
    data = request.get_json()
    
    supplier = Supplier(
        name=data['name'],
        contact_name=data.get('contact_name'),
        email=data.get('email'),
        phone=data.get('phone'),
        address=data.get('address')
    )
    
    db.session.add(supplier)
    db.session.commit()
    
    return jsonify({
        'message': 'Supplier created successfully',
        'supplier_id': supplier.id
    }), 201

@suppliers_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_supplier(id):
    supplier = Supplier.query.get_or_404(id)
    data = request.get_json()
    
    for field in ['name', 'contact_name', 'email', 'phone', 'address']:
        if field in data:
            setattr(supplier, field, data[field])
    
    db.session.commit()
    return jsonify({'message': 'Supplier updated successfully'}), 200

@suppliers_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_supplier(id):
    supplier = Supplier.query.get_or_404(id)
    
    # Check if supplier has associated products
    if supplier.products:
        return jsonify({
            'error': 'Cannot delete supplier with associated products'
        }), 400
    
    db.session.delete(supplier)
    db.session.commit()
    
    return jsonify({'message': 'Supplier deleted successfully'}), 200
