css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* Global Styles */
.stApp {
    font-family: 'Inter', sans-serif;
}

/* Custom Header Styling */
.main-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 2rem 1rem;
    border-radius: 15px;
    margin-bottom: 2rem;
    text-align: center;
    box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
}

.main-header h1 {
    color: white;
    font-size: 2.5rem;
    font-weight: 700;
    margin: 0;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
}

.main-header p {
    color: rgba(255,255,255,0.9);
    font-size: 1.1rem;
    margin-top: 0.5rem;
    font-weight: 300;
}

/* Chat Container */
.chat-container {
    background: #f8fafc;
    border-radius: 20px;
    padding: 1.5rem;
    margin: 1rem 0;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    border: 1px solid #e2e8f0;
    min-height: 400px;
}

.chat-messages {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    max-height: 60vh;
    overflow-y: auto;
    padding: 1rem;
    scrollbar-width: thin;
    scrollbar-color: #cbd5e0 #f7fafc;
}

.chat-messages::-webkit-scrollbar {
    width: 6px;
}

.chat-messages::-webkit-scrollbar-track {
    background: #f7fafc;
    border-radius: 3px;
}

.chat-messages::-webkit-scrollbar-thumb {
    background: #cbd5e0;
    border-radius: 3px;
}

.chat-messages::-webkit-scrollbar-thumb:hover {
    background: #a0aec0;
}

/* Message Styling */
.message {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    margin-bottom: 1rem;
    animation: fadeInUp 0.3s ease-out;
}

.user-message-container {
    justify-content: flex-end;
}

.bot-message-container {
    justify-content: flex-start;
}

.message-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 600;
    font-size: 1rem;
    color: white;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    flex-shrink: 0;
}

.user-avatar {
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
    order: 2;
}

.bot-avatar {
    background: linear-gradient(135deg, #059669 0%, #0d9488 100%);
}

.message-content {
    max-width: 70%;
    padding: 1rem 1.25rem;
    border-radius: 18px;
    position: relative;
    line-height: 1.5;
    word-wrap: break-word;
}

.user-message {
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
    color: white;
    border-bottom-right-radius: 6px;
    margin-left: auto;
    box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
}

.bot-message {
    background: white;
    color: #374151;
    border: 1px solid #e5e7eb;
    border-bottom-left-radius: 6px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

.message-time {
    font-size: 0.75rem;
    color: #9ca3af;
    margin-top: 0.25rem;
    text-align: right;
}

/* Input Styling */
.stTextInput > div > div > input {
    border-radius: 25px !important;
    border: 2px solid #e2e8f0 !important;
    padding: 0.75rem 1.25rem !important;
    font-size: 1rem !important;
    transition: all 0.3s ease !important;
    background: white !important;
}

.stTextInput > div > div > input:focus {
    border-color: #4f46e5 !important;
    box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1) !important;
}

/* Sidebar Styling */
.sidebar .sidebar-content {
    background: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%);
    border-radius: 15px;
    padding: 1.5rem;
}

/* Button Styling */
.stButton > button {
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.75rem 1.5rem !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3) !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 20px rgba(79, 70, 229, 0.4) !important;
}

/* File Uploader Styling */
.uploadedFile {
    background: white !important;
    border: 2px dashed #cbd5e0 !important;
    border-radius: 12px !important;
    padding: 2rem !important;
    text-align: center !important;
    transition: all 0.3s ease !important;
}

.uploadedFile:hover {
    border-color: #4f46e5 !important;
    background: #f8fafc !important;
}

/* Success/Error Messages */
.stSuccess {
    background: linear-gradient(90deg, #10b981 0%, #059669 100%) !important;
    color: white !important;
    border-radius: 12px !important;
    padding: 1rem !important;
    border: none !important;
}

.stError {
    background: linear-gradient(90deg, #ef4444 0%, #dc2626 100%) !important;
    color: white !important;
    border-radius: 12px !important;
    padding: 1rem !important;
    border: none !important;
}

.stWarning {
    background: linear-gradient(90deg, #f59e0b 0%, #d97706 100%) !important;
    color: white !important;
    border-radius: 12px !important;
    padding: 1rem !important;
    border: none !important;
}

/* Loading Spinner */
.stSpinner {
    color: #4f46e5 !important;
}

/* Animations */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes pulse {
    0%, 100% {
        opacity: 1;
    }
    50% {
        opacity: .5;
    }
}

.typing-indicator {
    display: flex;
    align-items: center;
    gap: 4px;
    padding: 1rem;
}

.typing-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background-color: #9ca3af;
    animation: pulse 1.4s ease-in-out infinite;
}

.typing-dot:nth-child(1) { animation-delay: -0.32s; }
.typing-dot:nth-child(2) { animation-delay: -0.16s; }

/* Status Indicators */
.status-indicator {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-size: 0.875rem;
    font-weight: 500;
    margin: 0.5rem 0;
}

.status-ready {
    background: #dcfce7;
    color: #166534;
    border: 1px solid #bbf7d0;
}

.status-processing {
    background: #fef3c7;
    color: #92400e;
    border: 1px solid #fde68a;
}

.status-error {
    background: #fee2e2;
    color: #991b1b;
    border: 1px solid #fecaca;
}

/* Welcome Screen */
.welcome-screen {
    text-align: center;
    padding: 3rem 2rem;
    color: #6b7280;
}

.welcome-screen h3 {
    color: #374151;
    margin-bottom: 1rem;
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
    border: 1px solid #e5e7eb;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    transition: all 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 16px rgba(0,0,0,0.12);
}

.feature-icon {
    font-size: 2rem;
    margin-bottom: 1rem;
}

/* Responsive Design */
@media (max-width: 768px) {
    .main-header h1 {
        font-size: 2rem;
    }
    
    .message-content {
        max-width: 85%;
    }
    
    .feature-grid {
        grid-template-columns: 1fr;
    }
}
</style>
"""

bot_template = """
<div class="message bot-message-container">
    <div class="message-avatar bot-avatar">🤖</div>
    <div class="message-content bot-message">
        {{MSG}}
    </div>
</div>
"""

user_template = """
<div class="message user-message-container">
    <div class="message-content user-message">
        {{MSG}}
    </div>
    <div class="message-avatar user-avatar">👤</div>
</div>
"""
