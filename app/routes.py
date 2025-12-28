from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import db, Task

task_bp = Blueprint('tasks', __name__)

@task_bp.route('/', methods=['GET'])
@jwt_required()
def get_tasks():
    current_user_id = get_jwt_identity()
    
    status = request.args.get('status')
    category = request.args.get('category')
    
    query = Task.query.filter_by(user_id=current_user_id)
    
    if status:
        query = query.filter_by(status=status)
    if category:
        query = query.filter_by(category=category)
        
    tasks = query.all()
    return jsonify([{
        "id": t.id, 
        "title": t.title, 
        "description": t.description,
        "category": t.category,
        "status": t.status
    } for t in tasks]), 200

@task_bp.route('/', methods=['POST'])
@jwt_required()
def create_task():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    
    new_task = Task(
        title=data.get('title'),
        description=data.get('description'),
        category=data.get('category', 'General'),
        user_id=current_user_id
    )
    
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task created", "id": new_task.id}), 201

@task_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_task(id):
    current_user_id = get_jwt_identity()
    task = Task.query.filter_by(id=id, user_id=current_user_id).first_or_404()
    
    return jsonify({
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "status": task.status
    }), 200

@task_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_task(id):
    current_user_id = get_jwt_identity()
    task = Task.query.filter_by(id=id, user_id=current_user_id).first_or_404()
    data = request.get_json()
    
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.category = data.get('category', task.category)
    task.status = data.get('status', task.status)
    
    db.session.commit()
    return jsonify({"message": "Task updated"}), 200

@task_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_task(id):
    current_user_id = get_jwt_identity()
    task = Task.query.filter_by(id=id, user_id=current_user_id).first_or_404()
    
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"}), 200