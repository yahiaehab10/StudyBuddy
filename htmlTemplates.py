css = """
<style>
.chat-messages {
    display: flex;
    flex-direction: column;
    gap: 10px;
    max-height: 80vh;
    overflow-y: auto;
}
.bot, .user {
    display: flex;
    align-items: center;
    gap: 10px;
}
.bot-header, .user-header {
    display: flex;
    align-items: center;
    gap: 5px;
    font-weight: bold;
}
.bot-icon, .user-icon {
    width: 30px;
    height: 30px;
    border-radius: 50%;
}
.user-message, .bot-message {
    background-color: #f1f1f1;
    padding: 10px;
    border-radius: 5px;
    max-width: 70%;
}
.chat-container {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
}
.chat-container .bot {
    align-self: flex-start;
}
.chat-container .user {
    align-self: flex-end;
}
</style>
"""


bot_template = """
<div class="bot">
    <div class="bot-header">
        <img src="https://cdn-icons-png.flaticon.com/512/1055/1055646.png" alt="Bot Icon" class="bot-icon">
        <span class="bot-name">Study Buddy</span>
    </div>
    <div class="bot-message">
        {{MSG}}
    </div>
</div>
"""
user_template = """
<div class="user">
    <div class="user-header">
        <img src="https://cdn-icons-png.flaticon.com/512/1055/1055646.png" alt="User Icon" class="user-icon">
        <span class="user-name">You</span>
    </div>
    <div class="user-message">
        {{MSG}}
    </div>
</div>
"""
