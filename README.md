## DevOps Assignment 2 – ACEest Fitness CI/CD Pipeline

### Overview

This project implements a complete DevOps CI/CD pipeline for a Flask-based fitness web application — ACEest Fitness.
It demonstrates automation of testing, containerization, image deployment, and continuous integration using Jenkins, Docker, and Kubernetes.

⸻

### Tech Stack
	•	Language: Python 3.x (Flask)
	•	Testing Framework: Pytest
	•	Containerization: Docker
	•	CI/CD Tool: Jenkins
	•	Orchestration: Kubernetes (Minikube)
	•	Version Control: GitHub


⸻

### Setup Instructions

* Clone Repository

git clone https://github.com/2024tm93152-droid/ACEest_Fitness2.git
cd ACEest_Fitness2

* Create Virtual Environment

python3 -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate      # For Windows

* Install Dependencies

pip install -r requirements.txt

* Run Tests

pytest -v


⸻

### Docker Setup

Build Docker Image

docker build -t aceest-fitness-app:latest .

Run Container

docker run -d -p 5000:5000 aceest-fitness-app

Push Image to Docker Hub

docker login -u <your-dockerhub-username>
docker tag aceest-fitness-app <your-dockerhub-username>/aceest-fitness-app:latest
docker push <your-dockerhub-username>/aceest-fitness-app:latest


⸻

### Jenkins Pipeline

Pipeline Stages
	1.	Checkout Code – Clone repository from GitHub
	2.	Setup Virtual Environment – Create and activate venv
	3.	Install Dependencies – Install Python requirements
	4.	Run Unit Tests – Execute Pytest suite
	5.	Build Docker Image – Build container image from Dockerfile
	6.	Push to Docker Hub – Push image to DockerHub registry
	7.	Deploy to Kubernetes – Apply deployment and service manifests

⸻

### Kubernetes Deployment

Start Minikube

minikube start

Deploy Application

kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

Check Deployment Status

kubectl get pods
kubectl get svc

Access the Application

minikube service aceest-fitness-service


