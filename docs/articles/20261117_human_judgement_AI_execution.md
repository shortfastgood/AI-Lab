# Human Judgement, AI Execution: From an Idea to a Working Web App

How much programming experience do you need to turn a useful idea into a working web application?

AI is opening up new possibilities for people who understand a problem but have limited experience in the programming languages and infrastructure needed to solve it. Making the most of that opportunity requires human judgement throughout the project.

Andrej Karpathy’s HackerTube provides an interesting starting point.

In his account, Karpathy describes using an AI coding agent to build a website around YouTube videos recommended in Hacker News discussions. The agent processed the comments, filtered the material and assembled the application. Karpathy set the objective, obtained the necessary access credentials, arranged the hosting and bought the domain. He then instructed the agent to deploy the application. [Karpathy’s account of building HackerTube.](https://karpathy.bearblog.dev/hacker-tube/)

The speed of implementation attracts attention. I find the role of human experience just as significant.

Someone recognised a need, decided what a better experience should offer and chose the source of information on which to build it. Those decisions gave the project its purpose and direction.

The choice of data is particularly interesting. HackerTube draws on recommendations that people posted in actual discussions. Its starting point is a collection of expressed human opinions about videos worth watching. AI helped extract and organise those recommendations. The site also includes its own personalised recommendation features. [How HackerTube’s collection was assembled.](https://karpathy.bearblog.dev/hacker-tube/)

This gives the collection a meaningful basis: people sharing something they consider worth another person’s time. It also makes the origin of the recommendations easier to understand than a feed whose selection rules are hidden from the user.

Community recommendations will naturally reflect the interests and preferences of that community. Understanding that context is part of deciding whether the collection suits our own needs.

Karpathy also makes the site’s data available for export, allowing others to give it to an AI agent and create their own version. [Data export and reuse.](https://karpathy.bearblog.dev/hacker-tube/)

That makes a personal “fork” an appealing next step: a new application built from the same collection, with its own purpose, interface and selection criteria. We could decide which subjects deserve attention, how to organise the material and what information should explain each recommendation.

This is the possibility I would like to explore: building and deploying a focused web utility without first acquiring extensive experience in a particular programming language or in setting up a production environment.

The necessary competence in AI includes being able to define a clear brief, provide context, assess proposed solutions and ask for evidence that the result works. It also means recognising the limits of our own knowledge and knowing when a decision needs further investigation or specialist review.

Human responsibility continues through deployment. We need to decide what is ready to publish, understand the running costs and establish how the application will be maintained.

Karpathy brings considerable technical experience to those decisions. His example gives us a useful reference, while leaving an important practical question to explore: how can someone with less implementation experience guide and verify the same kind of work?

For me, that is the most interesting part of this experiment. AI can help us translate an intention into working software. Our experience, choices and judgement determine what we ask it to build, whose knowledge we draw on and whether the result is useful.
