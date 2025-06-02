"""HTML templates and CSS styles for Study Buddy UI - Simple, clean design."""

# Simplified CSS styles with improved colors
CSS_STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

/* Simple Color Palette with better colors */
:root {
    --primary: #3b82f6;         /* Brighter blue */
    --primary-light: #60a5fa;   /* Lighter blue */
    --primary-dark: #2563eb;    /* Darker blue */
    --success: #10b981;         /* Emerald green */
    --warning: #f59e0b;         /* Amber */
    --error: #ef4444;           /* Red */
    
    --bg: #ffffff;              /* White background */
    --bg-light: #f8fafc;        /* Very light blue gray */
    --card: #ffffff;            /* White cards */
    --border: #e2e8f0;          /* Light blue gray border */
    
    --text: #0f172a;            /* Dark slate blue text */
    --text-light: #64748b;      /* Slate blue text */
    --text-xlight: #94a3b8;     /* Light slate blue text */
    
    --shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    --radius: 8px;
    --spacing: 16px;
}

/* Base */
body, .stApp {
    font-family: 'Inter', sans-serif !important;
    background: var(--bg) !important;
    color: var(--text) !important;
    line-height: 1.5;
}

/* App Header */
.app-header {
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
    color: white;
    padding: var(--spacing);
    border-radius: var(--radius);
    margin-bottom: var(--spacing);
    text-align: center;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

.app-header h1 {
    font-size: 1.75rem;
    font-weight: 600;
    margin: 0 0 8px 0;
}

.app-header p {
    font-size: 1rem;
    margin: 0;
    opacity: 0.9;
}

/* Chat Container */
.chat-container {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: var(--spacing);
    margin: var(--spacing) 0;
    max-height: 60vh;
    overflow-y: auto;
    box-shadow: var(--shadow);
}

/* Messages */
.message {
    padding: 12px;
    border-radius: var(--radius);
    margin-bottom: 12px;
    max-width: 85%;
    font-size: 0.9375rem;
    line-height: 1.5;
}

.user-message {
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
    color: white;
    margin-left: auto;
    border-bottom-right-radius: 2px;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.bot-message {
    background: var(--bg-light);
    color: var(--text);
    border: 1px solid var(--border);
    margin-right: auto;
    border-bottom-left-radius: 2px;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

/* Form Controls */
.stTextInput > div > div > input,
.stSelectbox > div > div > div {
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    padding: 10px 14px !important;
    background: white !important;
    font-family: 'Inter', sans-serif !important;
    transition: border-color 0.2s !important;
    color: var(--text) !important;
}

.stTextInput > div > div > input:focus,
.stSelectbox > div > div > div:focus {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.15) !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(to bottom, var(--primary-light), var(--primary)) !important;
    color: white !important;
    border: none !important;
    border-radius: var(--radius) !important;
    padding: 8px 16px !important;
    font-weight: 500 !important;
    font-family: 'Inter', sans-serif !important;
    transition: all 0.2s !important;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1) !important;
}

.stButton > button:hover {
    background: linear-gradient(to bottom, var(--primary), var(--primary-dark)) !important;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
    transform: translateY(-1px) !important;
}

.stButton > button[kind="secondary"] {
    background: white !important;
    color: var(--text) !important;
    border: 1px solid var(--border) !important;
}

.stButton > button[kind="secondary"]:hover {
    border-color: var(--primary) !important;
    color: var(--primary) !important;
    background: var(--bg-light) !important;
}

/* File Upload */
.stFileUploader > div {
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    background: var(--bg-light) !important;
    padding: var(--spacing) !important;
    transition: all 0.2s ease !important;
}

.stFileUploader > div:hover {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.1) !important;
}

/* Sidebar */
.css-1d391kg {
    background: var(--bg) !important;
    border-right: 1px solid var(--border) !important;
}

/* Alerts */
.status {
    padding: 10px 14px;
    border-radius: var(--radius);
    margin: 8px 0;
    font-size: 0.875rem;
}

.status-success {
    background: #ecfdf5;
    color: #065f46;
    border: 1px solid #a7f3d0;
}

.status-info {
    background: #eff6ff;
    color: #1e40af;
    border: 1px solid #bfdbfe;
}

.status-warning {
    background: #fffbeb;
    color: #92400e;
    border: 1px solid #fde68a;
}

/* Hide Streamlit Elements */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

/* Scrollbar */
::-webkit-scrollbar {
    width: 6px;
}

::-webkit-scrollbar-track {
    background: var(--bg-light);
}

::-webkit-scrollbar-thumb {
    background: var(--primary-light);
    border-radius: 3px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--primary);
}
</style>
"""

# Simple message templates
BOT_MESSAGE_TEMPLATE = """
<div class="message bot-message">{{MSG}}</div>
"""

USER_MESSAGE_TEMPLATE = """
<div class="message user-message">{{MSG}}</div>
"""
