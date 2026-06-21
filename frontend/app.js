document.addEventListener('DOMContentLoaded', () => {
    const startBtn = document.getElementById('start-btn');
    const topicInput = document.getElementById('topic-input');
    const arenaSection = document.getElementById('arena');
    const personaA = document.getElementById('persona-a');
    const personaB = document.getElementById('persona-b');
    const chatWindow = document.getElementById('chat-window');

    let currentAborts = null;

    startBtn.addEventListener('click', async () => {
        const topic = topicInput.value.trim();
        if (!topic) {
            alert('Please enter a debate topic!');
            return;
        }

        // Disable input during debate
        startBtn.disabled = true;
        startBtn.textContent = 'Generating Debate... 🧠';
        arenaSection.classList.add('hidden');
        chatWindow.innerHTML = '';

        try {
            // We request relative /api/debate. Nginx will reverse proxy this to backend:8000!
            const response = await fetch('/debate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ topic }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            
            // Set personas
            personaA.textContent = data.persona_a;
            personaB.textContent = data.persona_b;

            // Show Arena
            arenaSection.classList.remove('hidden');

            // Play the rounds with a delayed simulation for conversational effect
            startBtn.textContent = 'Debate in Progress... ⚔️';
            await playDebateRounds(data.rounds, data.persona_a);

        } catch (error) {
            console.error('Error fetching debate:', error);
            alert('Failed to generate debate. Is the backend running?');
        } finally {
            startBtn.disabled = false;
            startBtn.textContent = 'Start Debate ⚔️';
        }
    });

    async function playDebateRounds(rounds, personaAName) {
        for (const round of rounds) {
            const isPersonaA = round.speaker === personaAName;
            
            // Create bubble
            const bubble = document.createElement('div');
            bubble.className = `bubble ${isPersonaA ? 'bubble-a' : 'bubble-b'}`;

            // Create speaker label
            const label = document.createElement('span');
            label.className = `speaker-label ${isPersonaA ? 'label-a' : 'label-b'}`;
            label.textContent = round.speaker;

            // Create text
            const textNode = document.createTextNode(round.text);

            bubble.appendChild(label);
            bubble.appendChild(textNode);
            chatWindow.appendChild(bubble);

            // Auto-scroll chat
            chatWindow.scrollTop = chatWindow.scrollHeight;

            // Wait before presenting the next reply to make it feel natural
            await new Promise(resolve => setTimeout(resolve, 2000));
        }
    }
});
