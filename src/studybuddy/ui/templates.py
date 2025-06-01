"""HTML templates and CSS styles for StudyBuddy UI."""

# Enhanced CSS styles for the application
CSS_STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Modern Variables */
:root {
    --primary: #6366f1;
    --primary-dark: #4f46e5;
    --secondary: #8b5cf6;
    --accent: #06b6d4;
    --success: #10b981;
    --warning: #f59e0b;
    --error: #ef4444;
    --bg-primary: #ffffff;
    --bg-secondary: #f8fafc;
    --text-primary: #0f172a;
    --text-secondary: #475569;
    --text-muted: #94a3b8;
    --border: #e2e8f0;
    --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
    --radius: 0.75rem;
}

/* Base App Styling */
.stApp {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    background: linear-gradient(135deg, var(--bg-secondary) 0%, #e2e8f0 100%) !important;
    color: var(--text-primary) !important;
}

/* Header */
.main-header {
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    padding: 2rem;
    border-radius: var(--radius);
    margin-bottom: 2rem;
    color: white;
    box-shadow: var(--shadow);
    text-align: center;
}

.main-header h1 {
    font-size: 2.5rem;
    font-weight: 700;
    margin: 0 0 0.5rem 0;
    letter-spacing: -0.025em;
}

.main-header p {
    font-size: 1.125rem;
    margin: 0;
    opacity: 0.9;
}

/* Chat Container */
.chat-container {
    background: var(--bg-primary);
    border-radius: var(--radius);
    padding: 2rem;
    margin: 2rem 0;
    border: 1px solid var(--border);
    max-height: 70vh;
    overflow-y: auto;
    box-shadow: var(--shadow);
}

/* Messages */
.message {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    margin-bottom: 2rem;
    animation: slideIn 0.3s ease-out;
}

.user-message-container {
    justify-content: flex-end;
    margin-left: 15%;
}

.bot-message-container {
    justify-content: flex-start;
    margin-right: 15%;
}

.message-avatar {
    width: 40px;
    height: 40px;
    border-radius: var(--radius);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
    font-weight: 600;
    flex-shrink: 0;
    box-shadow: var(--shadow);
}

.user-avatar {
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
    color: white;
    order: 2;
}

.bot-avatar {
    background: linear-gradient(135deg, var(--accent) 0%, var(--secondary) 100%);
    color: white;
}

.message-content {
    flex: 1;
    padding: 1.25rem 1.5rem;
    border-radius: var(--radius);
    line-height: 1.6;
    box-shadow: var(--shadow);
}

.user-message {
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
    color: white;
    border-bottom-right-radius: 0.25rem;
}

.bot-message {
    background: var(--bg-primary);
    color: var(--text-primary);
    border: 1px solid var(--border);
    border-bottom-left-radius: 0.25rem;
}

/* Status Indicators */
.status-indicator {
    display: inline-flex;
    align-items: center;
    gap: 0.75rem;
    padding: 1rem 1.25rem;
    border-radius: var(--radius);
    font-weight: 500;
    margin: 1rem 0;
    box-shadow: var(--shadow);
}

.status-ready {
    background: linear-gradient(135deg, var(--success) 0%, #059669 100%);
    color: white;
}

.status-error {
    background: linear-gradient(135deg, var(--warning) 0%, #d97706 100%);
    color: white;
}

/* Cards */
.info-card, .project-selector, .metric-card {
    background: var(--bg-primary);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1.5rem;
    margin: 1rem 0;
    box-shadow: var(--shadow);
    transition: all 0.2s ease;
}

.info-card {
    text-align: center;
    background: linear-gradient(135deg, #fef7ff 0%, #f3e8ff 100%);
    border-color: #e9d5ff;
}

.metric-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px -8px rgb(0 0 0 / 0.2);
}

/* Form Controls */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div > div {
    border: 2px solid var(--border) !important;
    border-radius: var(--radius) !important;
    padding: 0.875rem 1rem !important;
    background: var(--bg-primary) !important;
    color: var(--text-primary) !important;
    box-shadow: var(--shadow) !important;
    transition: all 0.2s ease !important;
    font-family: 'Inter', sans-serif !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus,
.stSelectbox > div > div > div:focus {
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1) !important;
    outline: none !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: var(--radius) !important;
    padding: 0.875rem 1.5rem !important;
    font-weight: 600 !important;
    transition: all 0.2s ease !important;
    box-shadow: var(--shadow) !important;
    font-family: 'Inter', sans-serif !important;
}

.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 25px -8px rgb(0 0 0 / 0.3) !important;
}

.stButton > button[kind="secondary"] {
    background: var(--bg-primary) !important;
    color: var(--text-primary) !important;
    border: 2px solid var(--border) !important;
}

.stButton > button[kind="secondary"]:hover {
    background: var(--bg-secondary) !important;
    border-color: var(--primary) !important;
}

/* Sidebar */
.css-1d391kg {
    background: var(--bg-primary) !important;
    border-right: 1px solid var(--border) !important;
    box-shadow: var(--shadow) !important;
}

/* File Upload */
.stFileUploader > div {
    border: 2px dashed var(--border) !important;
    border-radius: var(--radius) !important;
    background: var(--bg-secondary) !important;
    padding: 2rem !important;
    transition: all 0.2s ease !important;
}

.stFileUploader > div:hover {
    border-color: var(--primary) !important;
    background: #fef7ff !important;
}

/* Progress Bar */
.stProgress > div > div > div {
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%) !important;
    border-radius: 0.25rem !important;
}

/* Section Headers */
.section-header {
    font-size: 1.125rem;
    font-weight: 700;
    color: var(--text-primary);
    margin: 1.5rem 0 1rem 0;
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

/* Checkbox */
.stCheckbox > label {
    font-weight: 500 !important;
    color: var(--text-primary) !important;
}

/* Animations */
@keyframes slideIn {
    from { 
        opacity: 0; 
        transform: translateY(10px);
    }
    to { 
        opacity: 1; 
        transform: translateY(0);
    }
}

/* Utilities */
.text-sm { 
    font-size: 0.875rem; 
    color: var(--text-secondary); 
}

/* Remove Streamlit branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display: none;}

/* Scrollbar */
::-webkit-scrollbar {
    width: 6px;
}

::-webkit-scrollbar-track {
    background: var(--bg-secondary);
}

::-webkit-scrollbar-thumb {
    background: var(--border);
    border-radius: 3px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--text-muted);
}

/* Mobile responsive */
@media (max-width: 768px) {
    .main-header {
        padding: 1.5rem;
    }
    
    .main-header h1 {
        font-size: 2rem;
    }
    
    .chat-container {
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .user-message-container {
        margin-left: 5%;
    }
    
    .bot-message-container {
        margin-right: 5%;
    }
}

/* Error prevention */
.stApp * {
    box-sizing: border-box;
}
</style>
"""

# Clean HTML template for bot messages
BOT_MESSAGE_TEMPLATE = """
<div class="message bot-message-container">
    <div class="message-avatar bot-avatar">🤖</div>
    <div class="message-content bot-message">
        {{MSG}}
    </div>
</div>
"""

# Clean HTML template for user messages
USER_MESSAGE_TEMPLATE = """
<div class="message user-message-container">
    <div class="message-content user-message">
        {{MSG}}
    </div>
    <div class="message-avatar user-avatar">👤</div>
</div>
"""
