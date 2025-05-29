"""HTML templates and CSS styles for StudyBuddy UI."""

# CSS styles for the application
CSS_STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

/* Balanced Modern Styles */
.stApp {
    font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%) !important;
    color: #2d3748;
}

/* Enhanced Header with Gradient */
.main-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 1.5rem 2rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    color: white;
    position: relative;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(102, 126, 234, 0.3);
}

.main-header::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="20" cy="20" r="2" fill="rgba(255,255,255,0.1)"/><circle cx="80" cy="40" r="1.5" fill="rgba(255,255,255,0.1)"/><circle cx="40" cy="70" r="1" fill="rgba(255,255,255,0.1)"/></svg>');
    opacity: 0.6;
}

.main-header h1 {
    color: white;
    font-size: 1.75rem;
    font-weight: 600;
    margin: 0;
    position: relative;
    z-index: 1;
}

.main-header p {
    color: rgba(255,255,255,0.9);
    font-size: 1rem;
    margin: 0.5rem 0 0 0;
    font-weight: 400;
    position: relative;
    z-index: 1;
}

/* Modern Chat Container */
.chat-container {
    background: white;
    border-radius: 16px;
    padding: 1.5rem;
    margin: 1.5rem 0;
    border: 1px solid rgba(226, 232, 240, 0.6);
    max-height: 65vh;
    overflow-y: auto;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.08);
    backdrop-filter: blur(10px);
}

/* Enhanced Message Styling */
.message {
    display: flex;
    align-items: flex-start;
    gap: 0.875rem;
    margin-bottom: 1.5rem;
    animation: messageSlideIn 0.3s ease-out;
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
    width: 36px;
    height: 36px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.875rem;
    font-weight: 600;
    flex-shrink: 0;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.user-avatar {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    order: 2;
}

.bot-avatar {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    color: white;
}

.message-content {
    flex: 1;
    padding: 1rem 1.25rem;
    border-radius: 16px;
    font-size: 0.9rem;
    line-height: 1.6;
    position: relative;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
}

.user-message {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-bottom-right-radius: 6px;
}

.bot-message {
    background: white;
    color: #2d3748;
    border: 1px solid #e2e8f0;
    border-bottom-left-radius: 6px;
}

/* Enhanced Status Indicators */
.status-indicator {
    display: inline-flex;
    align-items: center;
    gap: 0.625rem;
    padding: 0.75rem 1rem;
    border-radius: 10px;
    font-size: 0.875rem;
    font-weight: 500;
    margin: 0.75rem 0;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.status-ready {
    background: linear-gradient(135deg, #4ade80 0%, #22c55e 100%);
    color: white;
    border: none;
}

.status-error {
    background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
    color: white;
    border: none;
}

/* Beautiful Project Selector */
.project-selector {
    background: white;
    border-radius: 12px;
    padding: 1rem;
    margin-bottom: 1.5rem;
    border: 1px solid #e2e8f0;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
}

/* Enhanced Cards */
.info-card {
    background: linear-gradient(135deg, #fef7ff 0%, #f3e8ff 100%);
    border: 1px solid #e9d5ff;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1rem 0;
    text-align: center;
    box-shadow: 0 2px 12px rgba(139, 92, 246, 0.1);
}

.metric-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 1rem;
    margin: 0.5rem 0;
    box-shadow: 0 1px 6px rgba(0, 0, 0, 0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.metric-card:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

/* Modern Form Styling */
.stTextInput > div > div > input {
    border: 2px solid #e2e8f0 !important;
    border-radius: 10px !important;
    padding: 0.75rem 1rem !important;
    font-size: 0.9rem !important;
    background: white !important;
    color: #374151 !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1) !important;
    transition: all 0.2s ease !important;
}

.stTextInput > div > div > input:focus {
    border-color: #667eea !important;
    box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1) !important;
    outline: none !important;
}

.stSelectbox > div > div > div {
    border: 2px solid #e2e8f0 !important;
    border-radius: 10px !important;
    background: white !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1) !important;
}

.stTextArea > div > div > textarea {
    border: 2px solid #e2e8f0 !important;
    border-radius: 10px !important;
    background: white !important;
    font-size: 0.9rem !important;
}

/* Enhanced Button Styling */
.stButton > button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.75rem 1.25rem !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 2px 8px rgba(102, 126, 234, 0.3) !important;
}

.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 16px rgba(102, 126, 234, 0.4) !important;
}

.stButton > button[kind="secondary"] {
    background: white !important;
    color: #4a5568 !important;
    border: 2px solid #e2e8f0 !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1) !important;
}

.stButton > button[kind="secondary"]:hover {
    background: #f7fafc !important;
    border-color: #cbd5e0 !important;
    transform: translateY(-1px) !important;
}

/* Enhanced Sidebar */
.css-1d391kg {
    background: white !important;
    border-right: 1px solid #e2e8f0 !important;
    box-shadow: 2px 0 8px rgba(0, 0, 0, 0.05) !important;
}

/* File Upload Enhancement */
.stFileUploader > div {
    border: 2px dashed #cbd5e0 !important;
    border-radius: 12px !important;
    background: #f8fafc !important;
    padding: 1rem !important;
    transition: all 0.2s ease !important;
}

.stFileUploader > div:hover {
    border-color: #667eea !important;
    background: #fef7ff !important;
}

/* Progress Bar Enhancement */
.stProgress > div > div > div {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    border-radius: 6px !important;
}

/* Metric Enhancement */
.metric-container {
    background: white;
    border-radius: 10px;
    padding: 1rem;
    border: 1px solid #e2e8f0;
    box-shadow: 0 1px 6px rgba(0, 0, 0, 0.05);
    margin: 0.5rem 0;
}

/* Remove Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display: none;}

/* Enhanced Animations */
@keyframes messageSlideIn {
    from { 
        opacity: 0; 
        transform: translateX(-10px) translateY(5px);
    }
    to { 
        opacity: 1; 
        transform: translateX(0) translateY(0);
    }
}

@keyframes fadeInScale {
    from {
        opacity: 0;
        transform: scale(0.95);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

/* Spacing Utilities */
.space-y-2 > * + * { margin-top: 0.5rem; }
.space-y-4 > * + * { margin-top: 1rem; }
.space-y-6 > * + * { margin-top: 1.5rem; }

/* Typography Enhancements */
.text-sm { font-size: 0.875rem; color: #6b7280; }
.text-xs { font-size: 0.75rem; color: #9ca3af; }
.font-medium { font-weight: 500; }
.font-semibold { font-weight: 600; }

/* Section Headers */
.section-header {
    font-size: 1rem;
    font-weight: 600;
    color: #374151;
    margin: 1rem 0 0.5rem 0;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
</style>
"""

# Enhanced HTML template for bot messages
BOT_MESSAGE_TEMPLATE = """
<div class="message bot-message-container">
    <div class="message-avatar bot-avatar">🤖</div>
    <div class="message-content bot-message">
        {{MSG}}
    </div>
</div>
"""

# Enhanced HTML template for user messages
USER_MESSAGE_TEMPLATE = """
<div class="message user-message-container">
    <div class="message-content user-message">
        {{MSG}}
    </div>
    <div class="message-avatar user-avatar">👤</div>
</div>
"""
