import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Mock Debate Arena API")

# Allow all origins for our local sandbox development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class DebateRequest(BaseModel):
    topic: str

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Welcome to the Mock Debate Arena API!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/debate")
def generate_debate(request: DebateRequest):
    topic = request.topic.strip() or "Whether technology makes us lonely"
    
    # Pre-defined humorous templates for different perspectives
    debates_pool = [
        {
            "persona_a": "Socrates (The Philosopher)",
            "persona_b": "Chef Gordon (The Pragmatist)",
            "rounds": [
                {
                    "speaker": "Socrates (The Philosopher)",
                    "text": f"Let us first examine the essence of '{topic}'. If we dissect its core, does it serve the human soul, or is it merely an illusion of progress that distracts us from true virtue?"
                },
                {
                    "speaker": "Chef Gordon (The Pragmatist)",
                    "text": f"Virtue? Distraction? Look, we don't have time for a three-hour symposium! '{topic}' is practical, it's raw, and frankly, it gets the job done. You're overcomplicating a simple dish, Socrates!"
                },
                {
                    "speaker": "Socrates (The Philosopher)",
                    "text": "But Gordon, a dish prepared without understanding its impact on the body is mere catering, not art. Is action without contemplation not the definition of folly?"
                },
                {
                    "speaker": "Chef Gordon (The Pragmatist)",
                    "text": "Contemplation won't pay the suppliers! We execute, we adapt, and we make it delicious. That is the ultimate truth of '{topic}'!"
                }
            ]
        },
        {
            "persona_a": "C-3PO (The Neurotic Robot)",
            "persona_b": "Captain Rex (The Action Hero)",
            "rounds": [
                {
                    "speaker": "C-3PO (The Neurotic Robot)",
                    "text": f"Oh dear, oh dear! The probability of '{topic}' leading to a catastrophic system failure is approximately 98.3%! We should immediately retreat and recalculate our options!"
                },
                {
                    "speaker": "Captain Rex (The Action Hero)",
                    "text": f"Belay that, Goldenrod. In my experience, '{topic}' is the only tactical advantage we've got. We lock and load, adapt on the fly, and push through the noise."
                },
                {
                    "speaker": "C-3PO (The Neurotic Robot)",
                    "text": "But sir! My sensors indicate that the emotional and physical strain of such an endeavor is highly illogical! Why must humans always seek conflict?"
                },
                {
                    "speaker": "Captain Rex (The Action Hero)",
                    "text": "It's not about seeking conflict, 3PO. It's about taking a stand. '{topic}' is worth fighting for, and we're not backing down now."
                }
            ]
        },
        {
            "persona_a": "The Optimistic Futurist",
            "persona_b": "The Grumpy Historian",
            "rounds": [
                {
                    "speaker": "The Optimistic Futurist",
                    "text": f"Imagine the possibilities! With '{topic}', we are standing on the precipice of a glorious new era. We will transcend our historical limitations and unlock infinite potential!"
                },
                {
                    "speaker": "The Grumpy Historian",
                    "text": f"Unlock infinite potential? More like repeating the exact same mistakes we made in 1848, 1929, and 1974. '{topic}' is just a shiny new wrapper on old human greed and short-sightedness."
                },
                {
                    "speaker": "The Optimistic Futurist",
                    "text": "You are blinded by past failures. Technology and human cooperation are compounding exponentially. This time is different!"
                },
                {
                    "speaker": "The Grumpy Historian",
                    "text": "It is never different. The technology changes, but the human brain remains exactly the same. We will stumble, we will overreach, and then we will write history books about it."
                }
            ]
        }
    ]
    
    selected_debate = random.choice(debates_pool)
    return {
        "topic": topic,
        "persona_a": selected_debate["persona_a"],
        "persona_b": selected_debate["persona_b"],
        "rounds": selected_debate["rounds"]
    }
