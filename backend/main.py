from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

FAILURE_TYPES = ["Warping", "Stringing", "Under-extrusion", "Over-extrusion", "Layer Shift", "Nozzle Clog"]

@app.post("/diagnose")
async def diagnose(
    images: List[UploadFile] = File(...),
    printer: str = Form(""),
    filament: str = Form(""),
    bed_surface: str = Form("")
):
    detected_failures = random.sample(FAILURE_TYPES, k=random.randint(1, 2))

    response = {
        "failures": detected_failures,
        "diagnosis": f"The print shows signs of {', '.join(detected_failures)}. These issues can be caused by incorrect settings or mechanical problems.",
        "suggestions": [
            "Ensure bed is leveled properly.",
            "Check your slicer settings for retraction and speed.",
            "Make sure filament is dry and extruding cleanly."
        ]
    }
    return response
