# FounderStack AI — Virtual Startup Assistant

## Build with AI Hackathon 2026
**Team Name:** Code of Duty  
**Team Members:** Zobia Razzaq, Abeeha, Nimrah Shahid

---

## 1. Project Overview
FounderStack AI is an intelligent operations hub designed to help startup founders navigate the high-velocity "chaos phase." It solves the problem of fragmented workflows by automating lead enrichment, monitoring AI infrastructure costs (Cloud Run/Model pricing), and synchronizing cross-founder decisions. Our solution leverages the Gemini API to turn passive data into actionable executive insights, allowing founders to focus on building rather than managing.

## 2. Google AI Tech Stack Implementation
*   **Google AI Studio / Vertex AI**: We utilize **Gemini 1.5 Flash** (via `@google/genai` SDK) to power our natural language Assistant. It performs intent classification for incoming founder requests, generates context-aware follow-up emails for sales leads, and analyzes infrastructure logs to identify cost-saving opportunities.

*   **Hosting & Backend**: The application is deployed on **Google Cloud Run**, ensuring high availability and seamless scaling. We use an **Express.js** backend to proxy secure AI requests and a **React/Vite** frontend for a high-performance user experience.

*   **Integration**: **Firebase** serves as our real-time database and authentication layer. This allows for instant synchronization of the "Decision Sync" log and "Lead Pipeline" across multiple team members, creating a shared source of truth for the founding team.

## 3. Innovation & Impact
FounderStack AI is unique because it bridges the gap between **Sales Pipeline** and **Infrastructure Economics**. While most CRMs focus only on leads, our tool monitors the "AI Bills" in real-time, alerting founders when a model swap (e.g., from Pro to Flash) could save 40% in compute costs. This "CEO-level" holistic view is critical for early-stage startups where burn rate is just as important as sales growth.

**Real-world potential:**
1. Reduces operational overhead by 60%
2. Saves $480/month on AI infrastructure costs
3. Prevents missed follow-ups and lost leads

## 4. Live Demo
🔗 **Google AI Studio Demo:** https://ai.studio/apps/1e6f3da4-e614-4c7c-902f-9cebb5fdf286

## 5. Setup & Installation

### Prerequisites
- Node.js (v18+)
- Gemini API Key (from Google AI Studio)

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Build-with-AI-FAST-CFD-26/ai-hackathon-submission-code-of-duty.git
   cd ai-hackathon-submission-code-of-duty
Python Alternative
pip install -r requirements.txt
python backend_python_example.py
________________________________________
6. How to Use (Demo Instructions)
1.	Open the Google AI Studio link above
2.	Type: "I have a new lead called Acme Corp"
→ AI generates follow-up email
3.	Type: "Gemini 3.1 Flash is 40% cheaper"
→ AI calculates $480/month savings
4.	Type: "Decision: We launch on June 1"
→ AI logs decision for cross-founder sync
________________________________________
7. Technologies Used
•	Google AI Studio / Gemini 1.5 Flash
•	Google Cloud Run (deployment)
•	Firebase (real-time sync)
•	Express.js / React (frontend & backend)
________________________________________
Team Code of Duty | GDG Hackathon 2026 | FAST CFD

