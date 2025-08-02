
# 🛠 3D Print AI Fix App – Contractor Onboarding

## 🚀 Project Overview

This app helps users diagnose 3D print failures by uploading photos. The system detects common issues (like warping, stringing, etc.) and generates explanations + suggested fixes using AI (image classifier + GPT-4).

MVP is anonymous, web-based, and supports multiple photo uploads.

---

## 🔧 Key Roles

### 🔍 AI / ML Engineer
- Build image classifier (YOLOv8 / EfficientNet)
- Input: 1–5 images → Output: 1–3 failure types
- Labels: warping, stringing, under-extrusion, etc.
- Dataset: Start with ~200 labeled images (CSV provided)
- Framework: Python, PyTorch or TensorFlow

### 🤖 LLM Prompt Engineer
- Prompt GPT-4 to generate failure explanation + fixes
- Input: failure labels + optional metadata
- Output: JSON with diagnosis and 2–3 actionable suggestions
- Examples provided

### 🧪 Backend Developer (FastAPI)
- Endpoint: `POST /diagnose` (images + optional metadata)
- Steps:
  1. Save images temporarily
  2. Run classifier
  3. Call LLM
  4. Return JSON response
- Framework: FastAPI, Python
- API ready for frontend consumption

### 🖼 Frontend Developer (Next.js)
- Build UI:
  - Image upload (max 5)
  - Metadata fields: printer, filament, bed surface
  - Show diagnosis + suggestions
- Stack: Next.js, Tailwind CSS, Axios

---

## 🧪 Testing Flow

1. Upload 1–5 images + optional metadata
2. Backend classifies failure types
3. LLM generates:
   - Explanation
   - Suggested fixes
4. Display results in UI

---

## 🗃 Resources

- 🧾 Dataset Template: `3dprint_failure_dataset_template.csv`
- 💻 Frontend Boilerplate: `3d-fix-app-boilerplate.zip`
- 🤖 GPT Prompt Examples: see project README
- 🧠 LLM API: OpenAI GPT-4 (via `text-davinci` or `gpt-4` endpoint)

---

## 🎯 MVP Goal (2 Weeks)

- ✅ Upload + Diagnose Flow Working
- ✅ 5+ Failure Types Detected
- ✅ GPT-generated Fix Suggestions
- ✅ Testable UI
