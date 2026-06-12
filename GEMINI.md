# Project Debating: Local DevOps Learning Sandbox

Welcome to **Project Debating**! This workspace is dedicated to learning DevOps hands-on, completely locally, and at zero cost.

---

## Core Vision & Goal

*   **Primary Objective:** Gain a deep, production-grade understanding of CI/CD pipelines, containerization, orchestration, GitOps, and Infrastructure as Code (IaC).
*   **Budget Constraint:** **$0.00 (Zero Cost).** Everything must run on the local machine (macOS / Darwin) using local virtualization, emulation, and free tier automation.
*   **Core Philosophy:** Keep the application code extremely simple so 90% of our focus is directed toward DevOps infrastructure, configurations, and pipeline automation.

---

## The Sandbox Application: "Mock Debate Arena"

To learn multi-service DevOps concepts (networking, service discovery, ingresses, state, scaling), we will build a lightweight, two-tier application:

### Architecture
1.  **Frontend (UI):** A single-page application (e.g., React or Vanilla JS) where users enter a debate topic and watch two personas debate.
2.  **Backend (API):** A lightweight API (e.g., Python FastAPI or Node.js Express) that:
    *   Generates templated, humorous, or rule-based debates locally (100% free, no API keys needed).
    *   *(Optional Future Extension):* Connects to a local **Ollama** instance (running a model like Llama3/Phi3) or the **Gemini API Free Tier** for real-time AI generation.

---

## DevOps Roadmap

We will tackle our learning objectives incrementally across two distinct phases:

### Phase 1: Local Containerization & Orchestration (Current Focus)
*   [ ] **Docker:** Containerize both the Frontend and Backend services. Create a `docker-compose.yml` for rapid local multi-container development.
*   [ ] **GitHub Actions (CI):** Write workflows to lint, test, build, and push Docker images (using GitHub's free tier and free package registry/Docker Hub).
*   [ ] **Kind (Kubernetes in Docker):** Spin up a local multi-node Kubernetes cluster.
    *   Deploy Frontend and Backend services manually using vanilla Kubernetes manifests (`Deployment`, `Service`, `ConfigMap`, `Secret`).
    *   Configure a local **Ingress Controller** (e.g., NGINX Ingress) to access the app via a custom domain (e.g., `debating.local`) mapped in `/etc/hosts`.

### Phase 2: GitOps, Packaging & Infrastructure as Code
*   [ ] **Helm:** Package our Kubernetes manifests into customizable Helm charts to simplify deployments.
*   [ ] **ArgoCD:** Install ArgoCD in our Kind cluster and configure GitOps-driven continuous deployment (CD). Code changes pushed to Git will automatically sync to the cluster.
*   [ ] **Terraform:** Use Terraform locally (e.g., with the Helm and Kubernetes providers) to automate cluster setup and software installations, keeping infrastructure completely version-controlled.

---

## Workspace Rules & Best Practices

1.  **Local-First Guardrail:** Never use cloud provider modules (AWS, GCP, Azure) or paid external services. All configurations must target local Kind clusters, local networks, or free tier endpoints.
2.  **Step-by-Step Validation:** Before automating with CI/CD or ArgoCD, ensure commands/configurations run successfully manually.
3.  **Lightweight Development:** Do not over-engineer the frontend or backend features. If we need a feature, implement the simplest version to support the corresponding DevOps deployment pattern.
4.  **No Committed Secrets:** Ensure `.env` files, kubeconfigs, and local access keys are strictly git-ignored.
