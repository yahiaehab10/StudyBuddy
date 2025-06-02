"""Simple chatbot service for StudyBuddy."""

import os
import json
from typing import List, Dict, Optional, Any
import streamlit as st
from pathlib import Path

from ..config.settings import settings


class ChatbotService:
    """Simple chatbot service for answering questions and providing study assistance."""

    def __init__(self):
        self.is_initialized = True
        self.knowledge_base = self._get_knowledge_base()

    def _get_knowledge_base(self) -> Dict[str, str]:
        """Get basic knowledge base for common study topics."""
        return {
            "photosynthesis": "Photosynthesis is the process by which plants convert light energy into chemical energy. It involves light absorption by chlorophyll, water splitting, and CO₂ fixation into glucose. The formula is: 6CO₂ + 6H₂O + light → C₆H₁₂O₆ + 6O₂",
            "cellular respiration": "Cellular respiration is the process of breaking down glucose to release ATP energy. It has three main stages: Glycolysis (in cytoplasm), Krebs Cycle (in mitochondria), and Electron Transport Chain. Formula: C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + ATP",
            "dna structure": "DNA has a double helix structure with a sugar-phosphate backbone and nitrogenous bases (A, T, G, C). Base pairing rules: A pairs with T (2 hydrogen bonds), G pairs with C (3 hydrogen bonds). The strands are antiparallel.",
            "newton's second law": "Newton's second law states that F = ma, where F is force (Newtons), m is mass (kg), and a is acceleration (m/s²). Force is directly proportional to acceleration, and more mass requires more force for the same acceleration.",
            "water cycle": "The water cycle includes evaporation (water to vapor), condensation (vapor to clouds), precipitation (rain/snow), and collection (water returns to bodies). Additional processes include transpiration, infiltration, and runoff.",
        }

    def generate_response(self, query: str, context: str = "") -> str:
        """Generate a simple chatbot response based on the query and context."""
        try:
            query_lower = query.lower()

            # Check if query matches known topics
            for topic, info in self.knowledge_base.items():
                if topic in query_lower or any(
                    word in query_lower for word in topic.split()
                ):
                    return f"Here's what I know about {topic}:\n\n{info}\n\nIs there anything specific about this topic you'd like me to explain further?"

            # If context is provided, use it to answer
            if context:
                return self._generate_context_based_response(query, context)

            # General response for unknown topics
            return self._generate_general_response(query)

        except Exception as e:
            return f"I apologize, but I encountered an error while processing your question: {str(e)}. Could you please rephrase your question?"

    def _generate_context_based_response(self, query: str, context: str) -> str:
        """Generate a response based on provided context."""
        context_snippet = context[:300] + "..." if len(context) > 300 else context

        return f"""Based on the information provided, here's what I can tell you about your question: "{query}"

**Relevant Information:**
{context_snippet}

**My Analysis:**
This information seems to address your question. Let me know if you need clarification on any specific part, or if you have follow-up questions!

**Study Tip:** Try to break down complex information into smaller parts to better understand the concepts."""

    def _generate_general_response(self, query: str) -> str:
        """Generate a general helpful response for unknown topics."""
        return f"""I'd be happy to help you with your question about "{query}"!

While I don't have specific information about this topic in my knowledge base, here are some suggestions:

• Try breaking down your question into smaller, more specific parts
• Look for key concepts or terms that might be related
• Consider what subject area this falls under (science, math, history, etc.)

If you have any study materials or context about this topic, feel free to share them and I'll do my best to help explain the concepts!

Is there anything else I can assist you with?"""

    def get_study_tips(self) -> List[str]:
        """Get general study tips."""
        return [
            "Break complex topics into smaller, manageable chunks",
            "Use active recall - test yourself without looking at notes",
            "Create connections between different concepts",
            "Take regular breaks to avoid mental fatigue",
            "Teach the concept to someone else or explain it out loud",
            "Use multiple learning methods: reading, writing, visual aids",
            "Practice with examples and real-world applications",
            "Review material regularly, not just before exams",
        ]

    def get_available_topics(self) -> List[str]:
        """Get list of topics in the knowledge base."""
        return list(self.knowledge_base.keys())

    def add_to_knowledge_base(self, topic: str, information: str) -> bool:
        """Add new information to the knowledge base."""
        try:
            self.knowledge_base[topic.lower()] = information
            return True
        except Exception as e:
            st.error(f"Error adding to knowledge base: {str(e)}")
            return False

    def search_knowledge_base(self, search_term: str) -> List[str]:
        """Search for topics containing the search term."""
        search_term_lower = search_term.lower()
        matching_topics = []

        for topic, info in self.knowledge_base.items():
            if search_term_lower in topic or search_term_lower in info.lower():
                matching_topics.append(topic)

        return matching_topics
