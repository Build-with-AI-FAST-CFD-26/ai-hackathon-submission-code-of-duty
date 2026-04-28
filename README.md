# FounderStack AI — Virtual Startup Assistant

## 1. Project Overview
FounderStack AI is an intelligent operations hub designed to help startup founders navigate the high-velocity "chaos phase." It solves the problem of fragmented workflows by automating lead enrichment, monitoring AI infrastructure costs (Cloud Run/Model pricing), and synchronizing cross-founder decisions. Our solution leverages the Gemini API to turn passive data into actionable executive insights, allowing founders to focus on building rather than managing.

## 2. Google AI Tech Stack Implementation
*   **Google AI Studio / Vertex AI**: We utilize **Gemini 1.5 Flash** (via `@google/genai` SDK) to power our natural language Assistant. It performs intent classification for incoming founder requests, generates context-aware follow-up emails for sales leads, and analyzes infrastructure logs to identify cost-saving opportunities.
*   **Hosting & Backend**: The application is deployed on **Google Cloud Run**, ensuring high availability and seamless scaling. We use an **Express.js** backend to proxy secure AI requests and a **React/Vite** frontend for a high-performance user experience.
*   **Integration**: **Firebase** serves as our real-time database and authentication layer. This allows for instant synchronization of the "Decision Sync" log and "Lead Pipeline" across multiple team members, creating a shared source of truth for the founding team.

## 3. Innovation & Impact
FounderStack AI is unique because it bridges the gap between **Sales Pipeline** and **Infrastructure Economics**. While most CRMs focus only on leads, our tool monitors the "AI Bills" in real-time, alerting founders when a model swap (e.g., from Pro to Flash) could save 40% in compute costs. This "CEO-level" holistic view is critical for early-stage startups where burn rate is just as important as sales growth.

## 4. Setup & Installation
### Prerequisites
*   Node.js (v18+)
*   Gemini API Key (from Google AI Studio)

### Steps
1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd founder-stack-ai
    ```
2.  **Install dependencies**:
    ```bash
    npm install
    ```
3.  **Set up environment variables**:
    Create a `.env` file in the root directory:
    ```env
    GEMINI_API_KEY=your_actual_api_key_here
    VITE_FIREBASE_CONFIG=your_firebase_json_config
    ```
4.  **Run the application**:
    ```bash
    npm run dev
    ```
    The app will be available at `http://localhost:3000`.

---
*Note: A Python-based backend implementation example is also included in `backend_python_example.py` for teams preferring a FastAPI-based AI proxy.*

## 🚀 GitHub Connection Guide

To connect this repository to your official GitHub account, follow these steps:

1. **Create a GitHub Repository**:
   - Go to [GitHub](https://github.com/new) and create a new repository (e.g., `founder-stack-ai`).
   - Do NOT initialize it with a README or .gitignore if you're pushing this existing code.

2. **Initialize Local Git**:
   - Open your terminal in the project root.
   - Run: `git init`
   - Run: `git add .`
   - Run: `git commit -m "Initial commit from FounderStack"`

3. **Link to GitHub**:
   - Run: `git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git`
   - Run: `git branch -M main`
   - Run: `git push -u origin main`

4. **Integration in Dashboard**:
   - Once your repo is on GitHub, go to the **Integration** section in the FounderStack dashboard.
   - Click **Connect** on the GitHub widget.
   - Select your newly created repository from the list (or enter its name) to enable AI sync.
