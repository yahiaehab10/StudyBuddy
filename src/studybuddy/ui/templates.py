"""HTML templates and CSS styles for StudyBuddy UI."""

# CSS styles for the application
CSS_STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Global Styles with terra cotta color scheme */
.stApp {
    font-family: 'Inter', sans-serif;
    background: #eeece2 !important;
    color: #3d3929;
}

/* Custom Header Styling with terra cotta */
.main-header {
    background: linear-gradient(135deg, #da7756 0%, #bd5d3a 100%);
    padding: 1.5rem 1rem;
    border-radius: 12px;
    margin-bottom: 1.5rem;
    text-align: center;
    box-shadow: 0 4px 20px rgba(218, 119, 86, 0.3);
}

.main-header h1 {
    color: white;
    font-size: 2rem;
    font-weight: 600;
    margin: 0;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
}

.main-header p {
    color: rgba(255,255,255,0.95);
    font-size: 1rem;
    margin: 0.25rem 0 0 0;
    font-weight: 300;
}

/* Chat Container */
.chat-container {
    background: white;
    border-radius: 12px;
    padding: 1rem;
    margin: 1rem 0;
    box-shadow: 0 2px 12px rgba(61, 57, 41, 0.1);
    border: 1px solid rgba(61, 57, 41, 0.1);
    max-height: 50vh;
    overflow-y: auto;
    scrollbar-width: thin;
    scrollbar-color: #da7756 #eeece2;
}

/* Message styling */
.message {
    display: flex;
    align-items: flex-start;
    gap: 8px;
    margin-bottom: 0.75rem;
    animation: fadeInUp 0.3s ease-out;
}

.user-message-container {
    justify-content: flex-end;
}

.bot-message-container {
    justify-content: flex-start;
}

.message-avatar {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 500;
    font-size: 0.875rem;
    color: white;
    box-shadow: 0 1px 4px rgba(0,0,0,0.1);
    flex-shrink: 0;
}

.user-avatar {
    background: linear-gradient(135deg, #da7756 0%, #bd5d3a 100%);
    order: 2;
}

.bot-avatar {
    background: linear-gradient(135deg, #3d3929 0%, #000000 100%);
}

.message-content {
    max-width: 75%;
    padding: 0.75rem 1rem;
    border-radius: 16px;
    position: relative;
    line-height: 1.4;
    word-wrap: break-word;
    font-size: 0.95rem;
}

.user-message {
    background: linear-gradient(135deg, #da7756 0%, #bd5d3a 100%);
    color: white;
    border-bottom-right-radius: 4px;
    margin-left: auto;
    box-shadow: 0 2px 8px rgba(218, 119, 86, 0.3);
}

.bot-message {
    background: #eeece2;
    color: #3d3929;
    border: 1px solid rgba(61, 57, 41, 0.1);
    border-bottom-left-radius: 4px;
    box-shadow: 0 1px 4px rgba(61, 57, 41, 0.05);
}

/* Status indicators */
.status-indicator {
    display: inline-flex;
    align-items: center;
    gap: 0.375rem;
    padding: 0.375rem 0.75rem;
    border-radius: 16px;
    font-size: 0.8rem;
    font-weight: 500;
    margin: 0.5rem 0;
}

.status-ready {
    background: rgba(218, 119, 86, 0.1);
    color: #bd5d3a;
    border: 1px solid rgba(218, 119, 86, 0.3);
}

.status-error {
    background: rgba(189, 93, 58, 0.1);
    color: #3d3929;
    border: 1px solid rgba(189, 93, 58, 0.3);
}

/* Welcome screen */
.welcome-screen {
    text-align: center;
    padding: 2rem 1rem;
    color: rgba(61, 57, 41, 0.8);
    background: white;
    border-radius: 12px;
    margin: 1rem 0;
    border: 1px solid rgba(61, 57, 41, 0.1);
}

.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}

.feature-card {
    background: white;
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid rgba(61, 57, 41, 0.1);
    box-shadow: 0 2px 8px rgba(61, 57, 41, 0.06);
    transition: all 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 16px rgba(61, 57, 41, 0.12);
}

.feature-icon {
    font-size: 2rem;
    margin-bottom: 1rem;
}

/* Input and button styling */
.stTextInput > div > div > input {
    border-radius: 20px !important;
    border: 1px solid #da7756 !important;
    padding: 0.625rem 1rem !important;
    font-size: 0.95rem !important;
    transition: all 0.2s ease !important;
    background: white !important;
    color: #3d3929 !important;
}

.stTextInput > div > div > input:focus {
    border-color: #bd5d3a !important;
    box-shadow: 0 0 0 2px rgba(218, 119, 86, 0.2) !important;
}

.stButton > button {
    background: linear-gradient(135deg, #da7756 0%, #bd5d3a 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.625rem 1.25rem !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 2px 8px rgba(218, 119, 86, 0.3) !important;
}

.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 12px rgba(218, 119, 86, 0.4) !important;
    background: linear-gradient(135deg, #bd5d3a 0%, #a04d2e 100%) !important;
}

/* Animations */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(5px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Hide Streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""

# HTML template for bot messages
BOT_MESSAGE_TEMPLATE = """
<div class="message bot-message-container">
    <div class="message-avatar bot-avatar">🤖</div>
    <div class="message-content bot-message">
        {{MSG}}
    </div>
</div>
"""

# HTML template for user messages
USER_MESSAGE_TEMPLATE = """
<div class="message user-message-container">
    <div class="message-content user-message">
        {{MSG}}
    </div>
    <div class="message-avatar user-avatar">👤</div>
</div>
"""
