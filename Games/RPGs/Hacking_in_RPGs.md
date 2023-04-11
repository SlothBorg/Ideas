RPGs and Hacking/CyberSecurity two of my main passions.

I have a lot to say on the topic but first, why should you listen to me?


TL:DR: This is the intersection of what I get paid to do, and what I do for fun.

* I've been doing CyberSecurity from over a decade.
  * I've conducted [PenTests](https://en.wikipedia.org/wiki/Penetration_test)
  * I've also responded to PenTest findings and worked to remediate them.
  * I've responded to [ransomware](https://en.wikipedia.org/wiki/Ransomware) and spamware
* I've done red team (hacking into things) and blue team (protecting things) engagements.
* I do [CTFs](https://medium.com/@isaacwangethi30/beginners-guide-to-web-hacking-ctfs-9ef04e7c5df5) with friends for fun. 
* This is a passion of mine, and something I take very seriously.
* I also love RPGs and play a lot of them, so would like to think I can see how the two would intersect.

## What is a Hack and Hacker.

The [Jargon File](http://www.catb.org/jargon/html/meaning-of-hack.html/) has a whole section on what a Hack is. While a great real world definitions it is not as helpful within the context of an RPG.

So for the purposes of this a hack within the context of an RPG is:

> an action to gain control of a device, devices, network or other technological entity, to a degree that is narrative important or interesting.    

Using this definition it's easy to see how a player could hack a robot, a factory, a data pad, a drone, a spaceship, a cybernetic arm etc.

I find it important to note this is fundamentally different than the "real world" definition which is more in line with `a clever solution to a challange/problem` and is more in line with how media portrays Hacks and Hackers in action movies. But I digress.

## So Hacking in an RPG

There are two ways to approach implementing hacking in an RPG, "realistic" and abstracted.  

I can only recommend an abstracted system.

### Realistic hacking.

To talk about the issues with implementing "realistic" hacking, we first need to talk about what Hacking is within the context of the above definition of a Hack.

For example there is a server (the target) with some data on it, and we (the players) want to get that data for what ever reason.

In the real world a lot of people like to map hacks to a framework like [The Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html), for our purposes we can generalize a Hack as falling into 5 broad steps:

1. **Reconnaissance**: Finding out as much information as you can about your target. This involves scanning the target, learning what kind of software it is running, any [OSINT](https://en.wikipedia.org/wiki/Open-source_intelligence) who runs the server, where is it located, who is responsible for it etc.
2. **Weaponization**: Taking all the information from the Reconnaissance step, and finding a weakness, something to exploit. Maybe there is an older version of software running with a known vulnerability, maybe you have a [zero day](https://en.wikipedia.org/wiki/Zero-day_(computing)), maybe you have to develop some software, maybe you can [Socially Engineer](https://en.wikipedia.org/wiki/Social_engineering_(security)) someone into giving you accses.
3. **Gaining Access**: Taking the exploit developed in the Weaponization step and using it. This is where theory meets reality and often requires going back to the beginning. 
4. **Exploitation**: You are in! now you have to do the thing. Maybe it's grab some data, maybe it's pivot to a new machine (Repeat all the Steps), maybe it's launch your code.
5. **Clearing Tracks**: Optional but really recommended, you don't want anyone knowing it was you right? Cleaning up traces of your activity, scrubbing log files, deleting code etc.

You can see how this might be gamified into an interesting mechanic where each step requires some player interaction and choice. Each step has a different level of risk, and diffrent outcomes from failure.

You can, also, start to see how this might take some time, an issue we will return to.

#### Example

Let's look at this 5-step process in the context of a recent security engagement contract I was involved in.

We (the group I was part of, 3 members total) was hired to evaluate the security of a server and application, and provided guidance on how to improve it's security. We were asked to write a file on the server in a specific directory to prove we could gain full control over the server. 

* **Reconnaissance**: We had the target and the client did tell us some software running on it. We ran a bunch of scans to learn more, what versions of software, what ports were open, etc.
  This took 40-60 hours spread over a week. There were a lot of hiccups and issues, as the client wanted us to use specific software for the scan and assessment.   
* **Weaponization**: We didn't find an easy way into the server, and had to look at the custom application running on the server. Through that we found a way to get into the server if a bunch of different things happened in just the right way.
  Another 20 - 40 hours were spent spread across two developers to write some code to pull off the hack.
* **Gaining Access**: It didn't work, turns out the client had updated something and the attack we'd developed no longer worked.
* **Reconnaissance (round 2)**: More scans, more research this time pretty focused as we knew the server wasn't our way in. Another 40 or so hours and we had an idea.   
* **Weaponization (round 2)**: Another 20ish hours of pair development and we had a working exploit. 
* **Gaining Access (round 2)**: It worked! Such an amazing rush!
* **Exploitation**: We were on the server, we did not however have the needed permissions to write the file to prove we had gotten in and could exploit the server. So we needed to [Escalate Privileges](https://en.wikipedia.org/wiki/Privilege_escalation)
* **Reconnaissance (round 3)**: We knew what OS we were on, so some quick research found a Privilege Escalation exploit that would work.
* **Weaponization (round 3)**: This had already been down by prior researchers.
* **Gaining Access**: 2 minutes to copy paste a script and run it, and we now had the privileges we needed.
* **Exploitation (round 2)**: Write the file with the specified information in the specified place.
* **Clearing Tracks**: Not strictly necessary but a fun enough challenge, only took a few hours.

To recap, it took 3 professionals, about 145 hours, and several circling back to the first stage to gain access to one server running a custom application.

In terms of difficulty, i'd say it was moderate, and it was a relatively short engagement.

So again we come back to the issue of time.

#### Time scale

Hacking takes time, a lot of time. Taking a look at some examples from games and media:

> Hacking a combat drone during a firefight to get it to fire at your enemies.

This isn't happening. There just isn't a "realistic" way to do this in the middle of combat. There are some ways to pull something like this off in a more "realistic" model, more on that later.

> Hacking the doors open, during a firefight.

Again not something that is going to "realistically" work. You could force them open, or if you know a bit about the doors, and how they were wired over ride them or hotwire them. Pretty damn risky.

> Hacking into a server and steal data, before the guards break down a door.

Not as stated.

> Copying someone's phone as you walk by them.

Honestly this is the most realistic of all the options, as in movies and media it's often depicted as having a tool to do it and not sitting down at a laptop and typing away furiously and then yelling *"i'm in"*.
There are real world examples and tools that are pretty cheap (sub $1,000usd) to do this kind of attack.

So in general, if you had time beforehand, and were able to do all the research and development you needed, you could have an exploit in place and ready to go and then activate it at the right moment. 

### Abstracted hacking.

There are generally three ways of handling this, as a skill, as a mini-game or as a downtime project. Depending on the type of game you are playing they all have strengths and weaknesses.

Since the goal here is to talk about realistic hacking, 

* A lot of TTRPGs implement hacking as a single skill, sometimes as a few different skills.
  * If the point of the game has little to do with technology, hacking and does not try to be simulationist or "realistic", then this is fine, probably even the best option. 
* Video games are big fans of the mini-game solution, and in a video game it tends to work well.
  * Personally I'm not a fan of a mini-game based solution, Shadowrun rather infamously has the "Decker Problem", where there are separate rules for how to handel hacking and events in cyberspace. There are some interesting and I would say good ideas here, depending on edition turns are a different time scale in cyberspace than in the real world. 
* Some more recent TTRPGs take the approach of Hacking as a downtime project
  * I've mostly encountered this in PBTA and FitD games. 

It is this last one that I think makes for the best implementation.

### How would I run Hacking in an RPG

#### Guiding principals:

* Hacking is more about resources, how much do I want to spend (time, effort, contacts, etc) to gain access to a thing.
  * *Are you willing to spend 100s of hours, 10,000s of dollars to develop a perfect exploit to break into the facility? or you willing to go in guns a blazing?*
* Social engineering is generally the easy route. 
  * *get enough info to impersonate the head of security, call up the front desk and have them unlock the roof access for the CEO who is landing in 10 minutes via helicopter*
* Hacking is preparatory, you are hacking to prepare the battle field, or alter it.
  * *ensure doors are unlocked for example*

#### How i'd implement it

* Hacking is not a skill, if the system has skills then any number of applicable skills can be used in your hacking attempt. For example, Research, Computers, Socializing could all be used in a Hacking attempt.
* Hacking is a project, I use [clock like those Blades in the Dark](https://bladesinthedark.com/progress-clocks).
  * One clock each for **R&D**, **Exploitation**, and **Cleanup**, I combine **Reconnaissance** and **Weaponization** into R&D and **Gaining Access** and **Exploitation** into **Exploitation** to help stream line things.
  * After the R&D clock is filled, players make a Hack roll, where they roll all applicable dice, for skills, resources etc. Pass or fail they move on to **Exploitation**
  * IF players pass, nothing complicated happens in the **Exploitation** phase.
  * IF players fail, there is at least one complication in the **Exploitation** phase.
  * Pass or Fail in **Exploitation** determines if the players meet the goal and how hard the **Cleanup** phase is.
* Hacking would be a resource.
* You could then use skills like *computers*, *physics*, *business* etc to help with your hacking attempt.
* Unless you got really really really lucky you aren't hacking shit when bullets are flying.

---

**Second TL:DR** 

Realistic hacking doesn't work in cyberpunk RPGs where you have people shooting guns in the same scene.

---

*edited* for clarity, formatting and added some examples.

