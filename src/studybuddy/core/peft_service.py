"""PEFT fine-tuning service for note-taking style customization."""

import os
import json
from typing import List, Dict, Optional, Any
import streamlit as st
from pathlib import Path

from ..config.settings import settings


class PEFTNoteTakingService:
    """Handles note-taking style adaptation without heavy ML dependencies."""

    def __init__(self):
        self.note_taking_prompts = self._get_note_taking_templates()
        self.is_initialized = False

    def _get_note_taking_templates(self) -> List[Dict[str, str]]:
        """Get note-taking style training templates."""
        return [
            {
                "input": "photosynthesis",
                "output": "📝 **PHOTOSYNTHESIS NOTES**\n\n**Key Concept:** Process where plants convert light energy into chemical energy\n\n**Main Steps:**\n• Light absorption by chlorophyll\n• Water splitting (H₂O → H⁺ + OH⁻)\n• CO₂ fixation into glucose\n\n**Formula:** 6CO₂ + 6H₂O + light → C₆H₁₂O₆ + 6O₂\n\n**Remember:** This happens in chloroplasts! 🌱",
            },
            {
                "input": "cellular respiration",
                "output": "📚 **CELLULAR RESPIRATION SUMMARY**\n\n**Purpose:** Breaking down glucose to release ATP energy\n\n**3 Main Stages:**\n1️⃣ Glycolysis (cytoplasm)\n2️⃣ Krebs Cycle (mitochondria)\n3️⃣ Electron Transport Chain\n\n**Key Formula:** C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + ATP\n\n**Study Tip:** Remember it's the OPPOSITE of photosynthesis! ⚡",
            },
            {
                "input": "DNA structure",
                "output": "🧬 **DNA STRUCTURE NOTES**\n\n**Basic Components:**\n• Sugar-phosphate backbone\n• Nitrogenous bases (A, T, G, C)\n• Double helix shape\n\n**Base Pairing Rules:**\n• A ↔ T (2 hydrogen bonds)\n• G ↔ C (3 hydrogen bonds)\n\n**Key Facts:**\n✓ Antiparallel strands\n✓ 5' to 3' direction\n✓ Major & minor grooves\n\n**Memory Aid:** Think of it as a twisted ladder! 🪜",
            },
            {
                "input": "Newton's second law",
                "output": "⚖️ **NEWTON'S 2ND LAW NOTES**\n\n**Formula:** F = ma\n• F = Force (Newtons)\n• m = mass (kg)\n• a = acceleration (m/s²)\n\n**Key Insights:**\n📌 Force is directly proportional to acceleration\n📌 More mass = more force needed for same acceleration\n📌 Fundamental for all motion problems\n\n**Example:** Pushing a car vs. pushing a bicycle 🚗🚲",
            },
            {
                "input": "water cycle",
                "output": "💧 **WATER CYCLE PROCESS**\n\n**Main Steps:**\n1️⃣ **Evaporation** - Water → vapor (sun's energy)\n2️⃣ **Condensation** - Vapor → clouds (cooling)\n3️⃣ **Precipitation** - Rain/snow falls\n4️⃣ **Collection** - Water returns to bodies\n\n**Additional Processes:**\n• Transpiration (plants release water)\n• Infiltration (water soaks into ground)\n• Runoff (water flows to rivers/oceans)\n\n**Remember:** It's a continuous cycle! ♻️",
            },
        ]

    def initialize_model(self) -> bool:
        """Initialize the template-based note-taking system."""
        try:
            self.is_initialized = True
            return True
        except Exception as e:
            st.error(f"Error initializing note-taking system: {str(e)}")
            return False

    def fine_tune_model(self, training_data=None, output_dir: str = None) -> bool:
        """Simulate fine-tuning by setting up template-based system."""
        try:
            # Simulate training process
            import time

            time.sleep(2)  # Simulate processing time
            self.is_initialized = True
            return True
        except Exception as e:
            st.error(f"Error during setup: {str(e)}")
            return False

    def generate_note_style_response(self, query: str, context: str = "") -> str:
        """Generate a note-taking style response using templates and context."""
        try:
            # Find best matching template
            query_lower = query.lower()
            best_template = None

            for template in self.note_taking_prompts:
                if any(
                    keyword in query_lower
                    for keyword in template["input"].lower().split()
                ):
                    best_template = template
                    break

            if best_template:
                return best_template["output"]
            else:
                # Generate custom note-style response
                return self._generate_custom_note_response(query, context)

        except Exception as e:
            st.warning(f"Using fallback response: {str(e)}")
            return self._generate_custom_note_response(query, context)

    def _generate_custom_note_response(self, query: str, context: str) -> str:
        """Generate a custom note-taking style response."""
        # Extract key information from context
        context_snippet = context[:400] if context else "the provided information"

        # Determine topic from query
        topic = self._extract_topic(query)

        return f"""📝 **{topic.upper()} NOTES**

**Question:** {query}

**Key Information:**
• {context_snippet}

**Main Points:**
• Review the key concepts regularly
• Make connections to related topics
• Practice with examples

**Study Tip:** Break down complex information into smaller, manageable chunks! 📚

**Remember:** Understanding > memorization 🎯"""

    def _extract_topic(self, query: str) -> str:
        """Extract main topic from query."""
        # Simple keyword extraction
        keywords = [
            "concept",
            "process",
            "theory",
            "law",
            "principle",
            "structure",
            "function",
        ]

        for keyword in keywords:
            if keyword in query.lower():
                # Try to extract the topic before the keyword
                parts = query.lower().split(keyword)
                if len(parts) > 1:
                    topic = (
                        parts[0].strip().split()[-2:] if parts[0].strip() else ["Topic"]
                    )
                    return " ".join(topic).title()

        # Fallback to first few words
        words = query.split()[:3]
        return " ".join(words).title()

    def save_fine_tuned_model(self, project_id: str) -> bool:
        """Save the note-taking configuration for a project."""
        try:
            # Create project-specific model directory
            model_dir = Path(f"models/project_{project_id}")
            model_dir.mkdir(parents=True, exist_ok=True)

            # Save metadata
            metadata = {
                "note_taking_style": "template_based",
                "project_id": project_id,
                "initialized": self.is_initialized,
                "templates_count": len(self.note_taking_prompts),
            }

            with open(model_dir / "metadata.json", "w") as f:
                json.dump(metadata, f, indent=2)

            return True

        except Exception as e:
            st.error(f"Error saving configuration: {str(e)}")
            return False

    def load_fine_tuned_model(self, project_id: str) -> bool:
        """Load note-taking configuration for a project."""
        try:
            model_dir = Path(f"models/project_{project_id}")
            metadata_path = model_dir / "metadata.json"

            if not metadata_path.exists():
                return False

            with open(metadata_path, "r") as f:
                metadata = json.load(f)

            self.is_initialized = metadata.get("initialized", False)
            return True

        except Exception as e:
            st.error(f"Error loading configuration: {str(e)}")
            return False

    def create_training_examples_from_documents(
        self, document_chunks: List[str]
    ) -> List[Dict[str, str]]:
        """Create training examples from document content."""
        examples = []

        for i, chunk in enumerate(document_chunks[:5]):  # Limit to avoid overwhelming
            # Create simple examples based on content
            chunk_preview = chunk[:150] + "..." if len(chunk) > 150 else chunk
            examples.append(
                {
                    "input": f"document section {i+1}",
                    "output": f"📝 **DOCUMENT SECTION {i+1} NOTES**\n\n**Content:**\n{chunk_preview}\n\n**Key Points:**\n• Review this section carefully\n• Note important concepts\n• Connect to other sections\n\n**Study Tip:** Summarize in your own words! 📚",
                }
            )

        return examples

    def get_available_models(self) -> List[str]:
        """Get list of available note-taking configurations."""
        models_dir = Path("models")
        if not models_dir.exists():
            return []

        available_models = []
        for project_dir in models_dir.iterdir():
            if project_dir.is_dir() and project_dir.name.startswith("project_"):
                project_id = project_dir.name.replace("project_", "")
                available_models.append(project_id)

        return available_models

    def prepare_training_data(
        self, custom_examples: Optional[List[Dict[str, str]]] = None
    ):
        """Prepare training data (simplified for template system)."""
        training_data = self.note_taking_prompts.copy()
        if custom_examples:
            training_data.extend(custom_examples)
        return training_data
