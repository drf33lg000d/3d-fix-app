
# 🖨️ 3D Print AI Fix App

This project uses AI to diagnose 3D print failures from user-submitted photos. It detects common issues (e.g., warping, stringing, layer shift) and provides fix suggestions using GPT-4.

## 📦 Features

- Upload 1–5 failed print images
- AI image classification of failure types
- LLM-generated explanations and suggested fixes
- No login required

## 🧠 Stack

- Frontend: Next.js + Tailwind CSS
- Backend: FastAPI (Python)
- AI: YOLOv8 or EfficientNet for image classification + GPT-4 for fix generation

## 🚀 Getting Started

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

## 📂 Structure

```
3d-fix-app/
├── backend/
├── frontend/
├── prompts/
├── data/
├── docs/
```

## 🔧 API Reference

### POST `/diagnose`

**Request:**
- `files[]`: up to 5 images
- Optional metadata: printer, filament, bed_surface

**Response:**
```json
{
  "failures": ["Warping", "Stringing"],
  "diagnosis": "...",
  "suggestions": ["..."]
}
```

## 🤝 Contributing

Open a pull request or submit an issue if you want to help!

## 📄 License

MIT
