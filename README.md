📄 README.md
markdown
Copy code
# React CI/CD with Docker & GitHub Actions 🚀

This project demonstrates a complete **CI/CD pipeline** for a React-based login/signup app using:

- 🐳 Docker & Docker Hub
- 🛠️ GitHub Actions for CI/CD
- 🧪 Simple static React app testing
- 🚀 Local deployment via Minikube or Docker

---

## 🖥️ Project Features

- ReactJS app with:
  - Sign In / Sign Up UI
  - Welcome page with motivational quote
  - Stylish UI with gradients, shadows, and responsiveness
- CI/CD Pipeline:
  - GitHub Actions workflow to test, build & push Docker image
  - Docker Hub integration
- Local Deployment using Minikube or Docker

---

## 📁 Project Structure

ci-cd-docker/
├── public/
│ └── index.html
├── src/
│ ├── App.js
│ ├── App.css
│ └── index.js
├── .github/
│ └── workflows/
│ └── ci-cd.yml
├── Dockerfile
├── docker-compose.yml
├── package.json
├── README.md
└── .dockerignore

yaml
Copy code

---

## 🚀 How to Run Locally

### ✅ Prerequisites

- [Node.js](https://nodejs.org/)
- [Docker](https://www.docker.com/products/docker-desktop)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/) *(optional)*

### 🔧 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/your-username/ci-cd-docker.git
cd ci-cd-docker

# Install dependencies
npm install

# Start the React App
npm start
🐳 Docker Setup
🏗️ Build Docker Image
bash
Copy code
docker build -t react-app .
▶️ Run the App
bash
Copy code
docker run -p 3000:80 react-app
Now open http://localhost:3000 🎉

⚙️ GitHub Actions CI/CD
A .github/workflows/ci-cd.yml file automates:

React build

Docker image creation

Pushing to Docker Hub

Example Workflow Highlights
yaml
Copy code
- name: Build & Push Docker Image
  run: |
    docker build -t your-dockerhub-username/react-app .
    echo "${{ secrets.DOCKER_PASSWORD }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin
    docker push your-dockerhub-username/react-app
🚀 Minikube Deployment (Optional)
bash
Copy code
# Start Minikube
minikube start

# Enable Docker inside Minikube
eval $(minikube docker-env)

# Build image inside Minikube Docker
docker build -t react-app .

# Run it using a deployment
kubectl create deployment react-app --image=react-app
kubectl expose deployment react-app --type=NodePort --port=80

# Access the app
minikube service react-app

🔐 Environment Variables
No external env vars used in this simple static demo. Future versions can add:

JWT_SECRET

API_URL for auth backend, etc.

📦 Technologies Used
React.js

CSS (with gradients & animations)

Docker

GitHub Actions

Minikube (optional)

🤝 Author
👤 Jay
📧 Reach me via GitHub https://github.com/JAYPORWAL/ or www.linkedin.com/in/jay-gupta-1b0a79259

