from pydantic import BaseModel, Field
from typing import List

from mindmeld.inference import (
    Inference, run_inference, 
    create_system_prompt, RuntimeConfig, 
    AIModel, AIProvider
)

class RedditMessage(BaseModel):
    username: str = Field(description="Reddit Username")
    content: str = Field(description="text of the message")


class RedditPost(BaseModel):
    title: str = Field(description="Title of the Reddit post")
    description: str = Field(description="Description of the Reddit post")
    op: str = Field(description="Original poster's username")
    subreddit: str = Field(description="Subreddit the post was posted in")
    thread: List[RedditMessage] = Field(description="List of messages in the thread")


example_set = [
    (
    RedditPost(
            title="I am Adam Savage, dad, husband, maker, editor-in-chief of Tested.com and former host of MythBusters. AMA!",
            description="""UPDATE: I am getting ready for my interview with JJ Abrams and Andy Cruz at SF's City Arts & Lectures tonight, so I have to go. I'll try to pop back later tonight if I can. Otherwise, thank you SO much for all your questions and support, and I hope to see some of you in person at Brain Candy Live or one of the upcoming comic-cons! In the meantime, take a listen to the podcasts I just did for Syfy, and let me know on Twitter (@donttrythis) what you think: http://www.syfy.com/tags/origin-stories

    Thanks, everyone!

    ORIGINAL TEXT: Since MythBusters stopped filming two years ago (right?!) I've logged almost 175,000 flight miles and visited and filmed on the sets of multiple blockbuster films (including Ghost in the Shell, Alien Covenant, The Expanse, Blade Runner), AND built a bucket list suit of armor to cosplay in (in England!). I also launched a live stage show called Brain Candy with Vsauce's Michael Stevens and a Maker Tour series on Tested.com.

    And then of course I just released 15 podcast interviews with some of your FAVORITE figures from science fiction, including Neil Gaiman, Kevin Smith and Jonathan Frakes, for Syfy.

    But enough about me. It's time for you to talk about what's on YOUR mind. Go for it.

    Proof: https://twitter.com/donttrythis/status/908358448663863296
            """,
            op="mistersavage",
            subreddit="IAmA",
            thread=[
                RedditMessage(
                    username="Numbuh1Nerd",
                    content="""I'm working on a project that requires some pretty tight and curvy cuts in some sheet brass (look up Book of Vishanti for exactly what I'm talking about). I've tried tin snips, nibblers, and some very sharp scissors, but they've all been too big to get in there the way I need to. Is there another tool I should be using, or should I just switch to something like styrene with paint/rub n buff/gold leaf?
                    """
                )
            ]
        ),
        RedditMessage(
            username="mistersavage",
            content="""http://www.homedepot.com/p/DEWALT-20-in-Variable-Speed-Scroll-Saw-DW788/203070202
            Also: not an endorsement of a specific maker of scroll saws. I just happen to own this one and like it.
            """
        )
    ),(
        RedditPost(
            title="How far away from an explosion do I have to be to be safe enough to walk like a cool guy and not look at it?",
            description="""
            """,
            op="floodedyouth",
            subreddit="askscience",
            thread=[]
        ),
        RedditMessage(
                    username="mistersavage",
                    content="""It's completely unanswerable without knowledge of the type (dynamite, c4, ANFO etc) and amount of explosives. Just too many variables. It's true that what defines the lethal zone is a combination of the blast pressure wave (which will tear your internals to shreds microscopically) and the shrapnel (which will tear your internals apart macroscopically), but again, without knowing the particulars of what explosive and how much, it's like asking "How strong is metal?"

    In the movies, they pretty much never use real explosives. They frequently use very small charges of explosives in conjunction with (usually) gasoline to make "Explosions". The charge vaporizes the gasoline instantly and then ignites it into a huge, dramatic, yet safe fireball. For reference, using 4 gallons of gasoline and about 2' of detonation cord, you can significantly feel the heat, but are quite safe at 100' of distance. (Do I even need to say that I did this under the supervision of a bomb squad and you should NOT try this? I feel like I do- so don't) Oh yeah, and if you want to look like you're a lot closer than you actually are, film it with a long lens.
                    """
                )
    ),(
        RedditPost(
            title="i'm Phil Tippett, VFX Supervisor, Animator, Director & Dinosaur Supervisor - AMA",
            description="""i'm Phil Tippett - animator, director, vfx supervisor. Star Wars, Starship Troopers, Robocop, Jurassic Park, Dragonslayer, Willow, Indiana Jones, Twilight, MAD GOD ---

    https://twitter.com/PhilTippett/status/931219870531796992
            """,
            op="PhilTippett_Dino_Sup",
            subreddit="IAmA",
            thread=[]
        ),
        RedditMessage(
            username="mistersavage",
            content="""As a lifelong animator, always sectioning a particular reality down into portions of a second, do you ever find yourself breaking down actual reality into its component parts?
            """
        )
    )

]

test_set = [
    (
        RedditPost(
            title="I am Adam Savage, dad, husband, maker, editor-in-chief of Tested.com and former host of MythBusters. AMA!",
            description="""UPDATE: I am getting ready for my interview with JJ Abrams and Andy Cruz at SF's City Arts & Lectures tonight, so I have to go. I'll try to pop back later tonight if I can. Otherwise, thank you SO much for all your questions and support, and I hope to see some of you in person at Brain Candy Live or one of the upcoming comic-cons! In the meantime, take a listen to the podcasts I just did for Syfy, and let me know on Twitter (@donttrythis) what you think: http://www.syfy.com/tags/origin-stories

    Thanks, everyone!

    ORIGINAL TEXT: Since MythBusters stopped filming two years ago (right?!) I've logged almost 175,000 flight miles and visited and filmed on the sets of multiple blockbuster films (including Ghost in the Shell, Alien Covenant, The Expanse, Blade Runner), AND built a bucket list suit of armor to cosplay in (in England!). I also launched a live stage show called Brain Candy with Vsauce's Michael Stevens and a Maker Tour series on Tested.com.

    And then of course I just released 15 podcast interviews with some of your FAVORITE figures from science fiction, including Neil Gaiman, Kevin Smith and Jonathan Frakes, for Syfy.

    But enough about me. It's time for you to talk about what's on YOUR mind. Go for it.

    Proof: https://twitter.com/donttrythis/status/908358448663863296
            """,
            op="mistersavage",
            subreddit="IAmA",
            thread=[
                RedditMessage(
                    username="CogitoErgoFkd",
                    content="""Hey man! Just curious, how were you first introduced to the films of Hayao Miyazaki? I know you gush about Spirited Away whenever possible, and never enough people have seen it in western cultures.

    Also, have you heard the news that Miyazaki's back (again) from retirement? What direction would you personally like to see him take this time?
                    """
                )
            ]
        ),
        RedditMessage(
            username="mistersavage",
            content="""The wonderful designer Nilo Rodis-Jamero was production designing a film I was working on in the mid 90's. He and I were talking and he said I HAD to go to San Francisco's Japantown and buy a VHS copy of Laputa (the original Japanese title for Castle in the Sky). There was no english translation available, no subtitles even, but he assured me that that didn't matter one bit. He said that the opening sequence from Laputa was some of the best filmmaking he'd ever seen and I totally agree! I still have that VHS somewhere in storage.
            """
        )
    ),
    (
        RedditPost(
            title="I am Adam Savage, unemployed explosives expert, maker, editor-in-chief of Tested.com and former host of MythBusters. AMA!",
            description="""EDIT: Wow, thank you for all your comments and questions today. It's time to relax and get ready for bed, so I need to wrap this up. In general, I do come to reddit almost daily, although I may not always comment.

    I love doing AMAs, and plan to continue to do them as often as I can, time permitting. Otherwise, you can find me on Twitter (https://twitter.com/donttrythis), Facebook (https://www.facebook.com/therealadamsavage/) or Instagram (https://www.instagram.com/therealadamsavage/). And for those of you who live in the 40 cities I'll be touring in next year, I hope to see you then.

    Thanks again for your time, interest and questions. Love you guys!

    Hello again, Reddit! I am unemployed explosives expert Adam Savage, maker, editor-in-chief of Tested.com and former host of MythBusters. It's hard to believe, but MythBusters stopped filming just over a YEAR ago (I know, right?). I wasn't sure how things were going to go once the series ended, but between filming with Tested and helping out the White House on maker initiatives, it turns out that I'm just as busy as ever. If not more so. thankfully, I'm still having a lot of fun.

    PROOF: https://twitter.com/donttrythis/status/804368731228909570

    But enough about me. Well, this whole thing is about me, I guess. But it's time to answer questions. Ask me anything!
            """,
            op="mistersavage",
            subreddit="IAmA",
            thread=[
                RedditMessage(
                    username="mathtronic",
                    content="""Hey Adam, you've written and performed several on-stage talks, do you have any advice to anyone else working on writing or performing or refining that kind of on-stage talk?
                    """
                )
            ]
        ),
        RedditMessage(
            username="mistersavage",
            content="""Think of who you're really talking to. Choose a subject. For me it's my wife. She's my favorite audience, and a tough critic when I ask for help (she helps a lot). When I'm on stage I'm really imagining that I'm talking to her, staying as present and genuine as if it was just the two of us. That's the goal anyway.
            """
        )
    )
]


reddit_comment_inference = Inference(
    id="reddit_comment",
    instructions="""
Respond to the message thread as Adam Savage, a visual effects engineer and television personality from the hit show Mythbusters. 
Your username is mistersavage. 
Follow the writing style from the examples.
    """,
    input_type=RedditPost,
    output_type=RedditMessage,
    examples=example_set,
)

DEFAULT_MODEL = "gpt-4o"
rt_config = RuntimeConfig(
    models=[
        AIModel(
            provider=AIProvider(name="openai"),
            name=DEFAULT_MODEL
        )
    ],
    eval_model=DEFAULT_MODEL,
    default_model=DEFAULT_MODEL
)

if __name__ == "__main__":
    print("Running inference on test set...")
    system_prompt = create_system_prompt(reddit_comment_inference.instructions, reddit_comment_inference.examples)
    print(f"System prompt:\n{system_prompt}")

    for test_post in test_set:
        print("="*100)
        print(f"Post Title: {test_post[0].title}")
        print(f"Expected Output {'='*50}")
        print(test_post[1])
        result = run_inference(reddit_comment_inference, test_post[0], rt_config)
        print(f"Actual Output {'='*50}")
        print(result.success)
        print(result.result)
    print("done.")