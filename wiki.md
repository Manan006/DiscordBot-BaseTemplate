# WIKI and How to use

You need to copy the `sample.env` file as `.env` and fill it in.

The same needs to be added to `env.py` and then can be imported anywhere

---

`logs.py` has the logging configured with discord's logging module.

---

`bot.py` has the code for the `Bot` class which inherits the `discord.Client` class.

If you have things that need to be taken care of, when the bot ends itself then put those in the `Bot.close` function.

---

`main.py` takes the bot (`Bot` object) along with the logging details and runs the bot.

It also has the test commands taken from discord.py's official examples

---
